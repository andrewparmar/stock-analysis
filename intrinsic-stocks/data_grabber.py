# from pattern.web import URL
import pandas as pd

def extract_data(stk_ticker):

	# url_base = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB"
	# url_base = "http://financials.morningstar.com/ajax/exportKR2CSV.html?&callback=?&t=XNAS:FB&region=usa&culture=en-US&cur=&order=asc"
	url_base = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t=AAPL"

	# Using pattern.web
	# test = URL(url_base)
	# print test.download()

	# Using pandas
	# 
	# data = pd.read_csv(url_base, header=2,thousands =',', index_col=False)
	# data = pd.read_csv(url_base, header=3,thousands =',',index_col=1,skiprows=[3,19,20,31,32,41,42,43,44,49,54,59,64,65,66,72,73,74,95,96,101,102,103])
	data = pd.read_csv(url_base, header=2,thousands =',',index_col=0,skiprows=[3,19,20,31,32,41,42,43,44,49,54,59,64,65,66,72,73,74,95,96,101,102,103])
	data_t = data.transpose()

	return data_t

extract_data("AAPL")