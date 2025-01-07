import yfinance as yf#api has been discontinued 
import pandas as pd
import streamlit as st

#heading
st.write("""
# Simple Stock Price App

Shown Are the stock closing price and volume of Google 

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get ticker data
tickerData = yf.Ticker(tickerSymbol)
#get historical prices for ticker 
tickerDf = tickerData.history(period = 'id', start= '2010-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
