import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import yfinance as yf

def classify_trend(symbol:str, period:str) -> dict:
    ticker = yf.Ticker(symbol)
    history = ticker.history
    df = history.copy()


