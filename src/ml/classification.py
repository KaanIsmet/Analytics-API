import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import yfinance as yf

def classify_trend(symbol:str, period:str) -> dict:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)

    #differences and percentage change
    df["returns"] = df["Close"].pct_change()
    df["open_close_diff"] = df["Open"] - df["Close"]
    df["high_low_diff"] = df["High"] - df["Low"]

    #small moving averages
    df["sma_10"] = df["Close"].rolling(10).mean()
    df["sma_30"] = df["Close"].rolling(30).mean()
    df["sma_ratio"] = df["sma_10"] / df["sma_30"]

    df["volatility"] = df["returns"].rolling(10).std()

    df["volume_change"] = df["Volume"].pct_change()
    df["volume_sma"] = df["Volume"].rolling(10).mean()

    df["target"] = (df["Close"][-1] > df["Close"]).astype(int)

    features = ["returns",
                "open_close_diff",
                "high_low_diff", 
                "sma_10", "sma_30",  
                "volatility", 
                "volume_change", 
    ]

    X = df[features]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    prediction = model.predict(X.iloc[[-1]])[0]
    probability = model.predict_proba(X.iloc[[-1]])[0]

    return {
        "symbol": symbol,
        "period": period,
        "trend": "bullish" if prediction == 1 else "bearish",
        "confidence": round(max(probability) * 100, 2),
        "accuracy": round(accuracy * 100, 2),
        "probabilities": {
            "bearish": round(probability[0] * 100, 2),
            "bullish": round(probability[1] * 100, 2)
        },
        "note": "This is for educational purposes"
    }






