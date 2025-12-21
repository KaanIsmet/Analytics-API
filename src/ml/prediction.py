import numpy as np
from sklearn.linear_model import LinearRegression
import yfinance as yf


def next_day_prediction(symbol:str,  period:str) -> dict:
    ticker = yf.Ticker(symbol)
    history = ticker.history(period=period)
    closes = history["Close"].values
    
    X = np.arange(len(closes)).reshape(-1, 1)
    y = closes

    model = LinearRegression()
    model.fit(X, y)

    next_day = len(closes)
    prediction = model.predict([[next_day]])[0]
    last_price = closes[-1]

    return {
        "symbol": symbol,
        "period": period,
        "predicted_price": round(prediction, 2),
        "trend": "up" if prediction > last_price else "down"
    }
    