import pandas as pd
import numpy as np
import math
import datetime
import sys
from pandas_datareader import data
# import matplotlib.pyplot as plt

# Preping Data

# get ticker data
start_date = datetime.datetime(2010, 1, 1)
# end_date = datetime.datetime(2017, 6, 30)
end_date = datetime.datetime.today()

symbol = str(sys.argv[1])
ticker = pd.DataFrame(data.DataReader(symbol, 'yahoo', start_date, end_date))
# print ticker

# calculate Compound Annual Growth Rate (CAGR). CAGR = mu (mean return)
days = (ticker.index[-1] - ticker.index[0]).days		# using (a=b).days from datetime
# print days
cagr = ((ticker['Adj Close'][-1] / ticker['Adj Close'][0]) **
        (365.0 / days)) - 1
print 'CAGR=', str(round(cagr, 4) * 100) + "%"
mu = cagr

# create series of percentage daily returns and calculate volatility
ticker['Returns'] = ticker['Adj Close'].pct_change()
vol = ticker['Returns'].std() * math.sqrt(252)
print "Annual Volatility=", str(round(vol, 4) * 100) + "%"

# Monte Carlo Simulation

S = ticker['Adj Close'][-1] 	# starting stock price ie. last close
T = 252 						# Total nbumber of trading days
t = 10							# number of trading days (10 = 2 weeks)

simulation_end_price = []

for count in range(100):
    daily_return = np.random.normal(mu / T, vol / math.sqrt(T), t) + 1
    # print daily_return

    price_list = [S]

    for x in daily_return:
        price_list.append(price_list[-1] * x)

    simulation_end_price.append(price_list[-1])
	
# print simulation_end_price

collection = []
target_price = float(sys.argv[2])
print target_price

for price in simulation_end_price:
    if (price >= target_price):
        collection.append(price)

# print collection
print len(collection), len(simulation_end_price)
# print 32/100

percent_hit = float(len(collection)) / len(simulation_end_price) * 100
percenr_miss = 100 - percent_hit

print "percent_hit", percent_hit
print "percent_miss", percenr_miss


# print len(sys.argv)
print 