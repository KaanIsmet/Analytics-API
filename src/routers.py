from fastapi import APIRouter
from schemas import StockInfo, StockHistory, StockStats
from yfinance_service import get_stock_history, get_stock_info, get_stock_stats
from ml import next_day_prediction

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.get("/{symbol:str}")
def stock(symbol:str):
    stock = get_stock_info(symbol)
    return stock


@router.get("/{symbol:str}/{period:str}")
def stock_history(symbol:str, period:str):
    stock_history = get_stock_history(symbol, period)
    return stock_history


@router.get("/{symbol:str}/{period:str}/stats")
def stock_stats(symbol:str, period:str):
    stock_stats = get_stock_stats(symbol, period)
    return stock_stats


@router.get("/{symbol:str}/{period:str}/predict")
def prediction(symbol:str, period:str):
    stock_prediction = next_day_prediction(symbol, period)
    return stock_prediction