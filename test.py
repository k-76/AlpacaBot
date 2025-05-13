
from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient as StockData
from alpaca.data.historical import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, StockLatestBarRequest, StockQuotesRequest, CryptoBarsRequest, CryptoLatestBarRequest, CryptoLatestQuoteRequest
from alpaca.data import StockTradesRequest
from alpaca.data.live import StockDataStream
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.timeframe import TimeFrame
from datetime import datetime


#_trade = trade(id, 1, 2)
#print(_trade)
#strategy.trades.append(_trade)
for i in strategy.trades:
    print(i.contracts, i.id, i.entry_price, i.exit_price)
    #trade().
#print(strategy.trades)
#print(close[0])
########################################
apiEndpoint = 'https://paper-api.alpaca.markets/v2'
paperKey ='PKBMV49WHXM49V5BJORP'
paperSecret = '8nQer0U0jlFhYSvFPqDRzcDtKii7JCLBqnlRmaz1'

trading_client = TradingClient(paperKey, paperSecret)

################### get historical data ######################
#print(trading_client.get_account().account_number)
#print(trading_client.get_account().buying_power)
dataClient = StockData(paperKey, paperSecret)

requestParams = StockTradesRequest(
    symbol_or_symbols = "AAPL",
    start = datetime(2024, 1, 30, 14, 30 ),
    end = datetime(2024, 1, 30, 14, 45 )
)

trades = dataClient.get_stock_trades(requestParams)

################### set market order ######################
market_order_data = MarketOrderRequest(
    symbol=ticker,
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)
#market_order = trading_client.submit_order(market_order_data)


################### cancel open orders ######################
requestParams2 = GetOrdersRequest(
    status=QueryOrderStatus.OPEN
)

orders = trading_client.get_orders(requestParams2)
#for order in orders:
#    trading_client.cancel_order_by_id(order.id)

################### get current position ######################
#positions = trading_client.get_all_positions()
#for position in positions:
#    print(position.qty, position.symbol, position.current_price, position.avg_entry_price, mul1(position.unrealized_plpc, 100))

################### live data ######################

stream = StockDataStream(paperKey, paperSecret)

async def handleTrade(data):
    print(data)
#stream.subscribe_trades(handleTrade, "SPY")

#stream.run()