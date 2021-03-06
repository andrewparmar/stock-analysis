import pandas as pd
import numpy as np
import math
import datetime as dt
import sys
from pandas_datareader import data
# import matplotlib.pyplot as plt

# Preping Data

def monte_carlo(ticker_symbol, target_price, exp_date):
	# get ticker data
	start_date = dt.datetime(2010, 1, 1)
	# end_date = dt.datetime(2017, 6, 30)
	end_date = dt.datetime.today()

	symbol = str(ticker_symbol)
	ticker = pd.DataFrame(data.DataReader(symbol, 'yahoo', start_date, end_date))
	# print ticker

	# calculate Compound Annual Growth Rate (CAGR). CAGR = mu (mean return)
	days = (ticker.index[-1] - ticker.index[0]).days
	# print days
	cagr = ((ticker['Adj Close'][-1] / ticker['Adj Close'][0]) **
	        (365.0 / days)) - 1
	print("CAGR= {} %".format(str(round(cagr, 4) * 100)))
	mu = cagr

	# create series of percentage daily returns and calculate volatility
	ticker['Returns'] = ticker['Adj Close'].pct_change()
	vol = ticker['Returns'].std() * math.sqrt(252)
	print("Annual volatility= {} %".format(str(round(vol, 4) * 100)))

	# Monte Carlo Simulation

	S = ticker['Adj Close'][-1] 	# starting stock price ie. last close
	T = 252 						# Total nbumber of trading days

	# number of trading days
	dt_arg = exp_date
	# dt_arg = '20170817'
	start_date = dt.date.today()
	end_date = dt.date(int(dt_arg[0:4]),int(dt_arg[4:6]),int(dt_arg[6:]))
	t = np.busday_count(start_date, end_date)
	print("\nTrading days left: {}".format(t))

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
	target_price = float(target_price)
	print("Target price: {}\n".format(target_price))

	for price in simulation_end_price:
	    if (price >= target_price):
	        collection.append(price)

	# print collection
	# print len(collection), len(simulation_end_price)

	percent_hit = float(len(collection)) / len(simulation_end_price) * 100
	percenr_miss = 100 - percent_hit

	print("Percent_hit 	: {:.2f}".format(percent_hit))
	print("Percent_miss	: {:.2f}".format(percenr_miss))


	# print len(sys.argv)
	# print 

if __name__ == "__main__":

	monte_carlo(sys.argv[1],sys.argv[2],sys.argv[3])
