#
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
start = dt.datetime(1990, 1, 1)
end = dt.datetime.today()
stock = input("Enter required symbol from yahoo finance: ")
print(stock)
df = web.DataReader(stock, 'yahoo', start, end)
df['30ma'] = df['Adj Close'].rolling(window=30).mean()
df['50ma'] = df['Adj Close'].rolling(window=50).mean()
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df['200ma'] = df['Adj Close'].rolling(window=200).mean()
df.to_csv(stock + '.csv')
