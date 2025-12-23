import yfinance as yf
import numpy as np

def detect_anomalies(symbol:str, period:str, threshold:float = 2.0) -> dict:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)

    df["returns"] = df["Close"].pct_change()

    mean = df["returns"].mean()
    std = df["returns"].std()

    df["z_score"] = (df["returns"] - mean) / std
    df["is_anomaly"] = abs(df["z_score"]) > threshold

    anomalies = df[df["is_anomaly"]].copy()

    anomaly_list = [
        {
            "date": str(index.date()),
            "close": round(row["Close"], 2),
            "return_pct": round(row["returns"] * 100, 2),
            "z_score": round(row["z_score"], 2),
            "type": "spike" if row["returns"] > 0 else "drop"
        }
        for index, row in anomalies.iterrows()
    ]
    
    return {
        "symbol": symbol,
        "period": period,
        "threshold": threshold,
        "total_anomalies": len(anomaly_list),
        "anomalies": anomaly_list,
        "note": "This is for educational purposes"
    }
