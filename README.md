# Stock Analytics API

A FastAPI-powered REST API for stock market analysis with machine learning features. Fetches real-time data from Yahoo Finance and provides price predictions, trend classification, and anomaly detection.

## Features

- **Real-time Stock Data** — Fetch current stock info and historical prices via yfinance
- **Price Prediction** — Linear regression model to predict next-day closing price
- **Trend Classification** — Random Forest classifier to identify bullish/bearish trends
- **Anomaly Detection** — Z-score analysis to flag unusual price movements

## Tech Stack

- **Framework:** FastAPI
- **ML:** scikit-learn (Linear Regression, Random Forest)
- **Data:** yfinance, pandas
- **Server:** Gunicorn + Uvicorn
- **Deployment:** Docker, Railway

## Live Demo

**Production URL:** https://analytics-api-production-f8f1.up.railway.app

Try it:
- [Health Check](https://analytics-api-production-f8f1.up.railway.app/health)
- [AAPL Stock Info](https://analytics-api-production-f8f1.up.railway.app/stocks/AAPL)
- [AAPL 1 Month History](https://analytics-api-production-f8f1.up.railway.app/stocks/AAPL/1mo)
- [AAPL Prediction](https://analytics-api-production-f8f1.up.railway.app/stocks/AAPL/1mo/predict)
- [AAPL Classification](https://analytics-api-production-f8f1.up.railway.app/stocks/AAPL/6mo/classify)
- [AAPL Anomalies](https://analytics-api-production-f8f1.up.railway.app/stocks/AAPL/6mo/anomaly)
- [API Docs](https://analytics-api-production-f8f1.up.railway.app/docs)

## Endpoints

### Health Check

```
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

---

### Stock Info

```
GET /stocks/{symbol}
```

**Example:** `GET /stocks/AAPL`

**Response:**
```json
{
  "symbol": "AAPL",
  "short_name": "Apple Inc.",
  "long_name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "current_price": 273.12,
  "market_cap": 4200000000000,
  "currency": "USD",
  "fifty_two_week_high": 280.50,
  "fifty_two_week_low": 164.08
}
```

---

### Price History

```
GET /stocks/{symbol}/{period}
```

**Example:** `GET /stocks/AAPL/1mo`

**Valid periods:** `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "1mo",
  "prices": [
    {
      "date": "2024-12-01T00:00:00",
      "open": 270.00,
      "high": 275.50,
      "low": 269.25,
      "close": 273.12,
      "volume": 45000000
    }
  ]
}
```

---

### Stock Stats

```
GET /stocks/{symbol}/{period}/stats
```

**Example:** `GET /stocks/AAPL/1mo/stats`

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "1mo",
  "avg_price": 268.45,
  "percentage_change": 5.2,
  "high": 280.50,
  "low": 255.00,
  "volatile": 8.32
}
```

---

### Price Prediction

```
GET /stocks/{symbol}/{period}/predict
```

**Example:** `GET /stocks/AAPL/1mo/predict`

Predicts next-day closing price using Linear Regression.

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "1mo",
  "current_price": 273.12,
  "predicted_price": 276.24,
  "trend": "up"
}
```

---

### Trend Classification

```
GET /stocks/{symbol}/{period}/classify
```

**Example:** `GET /stocks/AAPL/6mo/classify`

Classifies stock trend using Random Forest.

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "6mo",
  "trend": "bullish",
  "confidence": 68.0,
  "accuracy": 88.46,
  "probabilities": {
    "bearish": 32.0,
    "bullish": 68.0
  }
}
```

---

### Anomaly Detection

```
GET /stocks/{symbol}/{period}/anomaly
```

**Example:** `GET /stocks/AAPL/6mo/anomaly`

Detects unusual price movements using z-score analysis.

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "6mo",
  "threshold": 2.0,
  "total_anomalies": 10,
  "anomalies": [
    {
      "date": "2024-11-15",
      "close": 225.50,
      "return_pct": -4.2,
      "z_score": -2.8,
      "type": "drop"
    }
  ],
  "note": "For educational purposes only"
}
```

## Quick Start

### Local Development

```bash
# Clone the repo
git clone https://github.com/KaanIsmet/Analytics-API.git
cd Analytics-API

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .

# Run the server
uvicorn main:app --reload
```

### Docker

```bash
docker build -t stock-analytics-api .
docker run -p 8000:8000 stock-analytics-api
```

### Docker Compose

```bash
docker compose up
```

## Disclaimer

This API is for educational purposes only. The predictions and analysis provided should not be used for actual trading decisions.

## License

MIT
