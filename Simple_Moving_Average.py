import yfinance as yf
import pandas as pd



ticker = input("What stock do ypu want to backtest a Simple Moving Average Strategy on?")
data = yf.download(ticker, start='1970-01-01', end='2025-07-01') 
window = 100
data['MA20'] = data['Close'].rolling(window=window).mean()