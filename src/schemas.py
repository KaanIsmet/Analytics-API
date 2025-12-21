from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
    status: str

class StockInfo(BaseModel):
    symbol: str
    short_name: str | None
    long_name: str | None
    sector: str | None
    industry: str | None
    current_price: float | None
    market_cap: int | None
    currency: str | None
    fifty_two_week_high: float | None
    fifty_two_week_low: float | None

class PriceData(BaseModel):
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockHistory(BaseModel):
    symbol: str
    period: str
    prices: list[PriceData]

class StockStats(BaseModel):
    symbol: str
    period: str
    avg_price: float
    percent_change: float
    high: float
    low: float
    volatility: float











    