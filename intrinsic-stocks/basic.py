import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('whitegrid')

import pandas_datareader.data as web
import datetime

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime.today()

APPL = pd.DataFrame(web.DataReader('AAPL', 'google', start_date, end_date))
# print APPL
# APPL = web.DataReader('AAPL')
# APPL.sort_values()
# APPL.loc[2] = [1,1,1,1,np.NaN]
# s = APPL.iloc[3]
# # print s
# APPL.append(s, ignore_index=True)
print APPL

plt.plot(APPL['Close'])

plt.title('Apple Inc Ticker Price')
plt.show()
