import yfinance as yf
import streamlit as st

st.title("5_years Monthly Sharpe Ratio for MFST")

# Define the ticker and risk-free rate
ticker = 'MSFT'
rf_monthly = 0.0025 # 0.25% per month

# Download monthly stock price data for the past 5 years
data = yf.download(ticker, period='5y', interval='1mo')
close_prices = data['Close'][ticker]

# Calculate monthly returns
monthly_returns = close_prices.pct_change().dropna()

# Calculate average excess return and standard deviation of returns
excess_returns = monthly_returns - rf_monthly
mean_excess_return = excess_returns.mean()
std_dev_return = monthly_returns.std()

# Calculate the Monthly Sharpe Ratio
monthly_sharpe_ratio = mean_excess_return / std_dev_return

st.metric(label="Monthly Sharpe Ratio", value=f"{monthly_sharpe_ratio:.2f}")
