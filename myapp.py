import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
         # this is title
         ## simple stock price app
         ### this is much smaller text here
         show are the stock **closing price** and ***volume*** of apple !
         """
         )

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="1mo", start="2010-5-31", end="2020-5-31")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
html = pd.read_html(url, header=0)
df = html[0]

df
