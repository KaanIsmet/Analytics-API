import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf


def next_day_prediction(symbol:str,  period:str) -> dict:
    ticker = yf.Ticker(symbol)
    history = ticker.history(period=period)
    history["returns"] = history["Close"].pct_change()

    columns = [ 'returns' ]
    features = history[columns].dropna()
    target = history.loc[features.index, 'Close']
    X = features.values
    y = target.values
    

    split_idx = int(len(X) * 0.8)
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    last_features = X[-1].reshape(1, -1)
    prediction = model.predict(last_features)[0]
    last_price = history['Close'].iloc[-1]

    return {
        "symbol": symbol,
        "period": period,
        "last_price": round(last_price, 2),
        "predicted_price": round(prediction, 2),
        "change": round(prediction - last_price, 2),
        "percentage change": round(((prediction - last_price) / last_price) * 100, 2),
        "trend": "up" if prediction > last_price else "down",
        "note": "This is for educational purposes"
    }
    