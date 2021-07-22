import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt

start = dt.datetime(2021,1,29)
end = dt.datetime(2021,7,22)
df = pdr.DataReader('BTC-USD','yahoo',start,end)
df2 = pd.DataFrame(df)
print(df2['Adj Close'])
