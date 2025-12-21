import yfinance as yf
from schemas import PriceData, StockInfo, StockHistory, StockStats

def get_stock_info(symbol: str) -> StockInfo:
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return StockInfo(
        symbol=symbol,
        short_name=info.get("shortName"),
        long_name=info.get("longName"),
        sector=info.get("sector"),
        industry=info.get("industry"),
        current_price=info.get("currentPrice") or info.get("regularMarketPrice"),
        market_cap=info.get("marketCap"),
        currency=info.get("currency"),
        fifty_two_week_high=info.get("fiftyTwoWeekHigh"),
        fifty_two_week_low=info.get("fiftyTwoWeekLow"),
    )

def get_stock_history(symbol: str, period: str) -> StockHistory:
    ticker = yf.Ticker(symbol)
    history = ticker.history(period=period)

    prices = [
        PriceData(
            date=index,
            open=row["Open"],
            high=row["High"],
            low=row["Low"],
            close=row["Close"],
            volume=int(row["Volume"]),
        )
        for index, row in history.iterrows()
    ]

    return StockHistory(
        symbol=symbol,
        period=period,
        prices=prices
    )

def get_stock_stats(symbol: str, period: str) -> StockStats:
    ticker = yf.Ticker(symbol)
    stats = ticker.history(period=period)

    closes = stats["Close"]
    avg_price = closes.mean()
    percent_change = ((closes.iloc[-1] - closes.iloc[0]) / closes.iloc[0]) * 100
    high = stats["High"].max()
    low = stats["Low"].min()
    volatility = closes.std()

    return StockStats(
        symbol=symbol,
        period=period,
        avg_price=round(avg_price, 2),
        percent_change=round(percent_change, 2),
        high=round(high, 2),
        low=round(low, 2),
        volatility=round(volatility, 2)
    )



    
