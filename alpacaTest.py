import pandas as pd
import numpy as np
import ta.trend
import yfinance as yf
from decimal import Decimal
import ta
#from backtesting import Backtest, Strategy
from backtesting.lib import crossover

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
################ math library #########################

class indicator():
    def __init__(self):
        self.data = []
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
    def __len__(self):
        return len(self.data)
    def append(self, value):
        self.data.append(value)
    def extend(self, values):
        self.data.extend(values)
    def insert(self, index, value):
        self.data.insert(index, value)
    def remove(self, value):
        self.data.remove(value) 
    def pop(self, index=-1):
        return self.data.pop(index)
    def prepend(self, app):
        if len(self.data) == 0:
            self.data.append(app)
        else:
            self.data = [app] + self.data

def add1(a, b):
    c = Decimal(str(a)) + Decimal(str(b))
    return c

def sub1(a, b):
    c = Decimal(str(a)) - Decimal(str(b))
    return c

def div1(a, b):
    c = Decimal(str(a)) / Decimal(str(b)) #safe div?
    return c

def mul1(a, b):
    c = Decimal(str(a)) * Decimal(str(b))
    return c

def mod1(a, b):
    c = Decimal(str(a)) % Decimal(str(b))
    return c

def lt1(a, b):
    c = (a < b)
    return c

def eq1(a, b):
    c = (a == b)
    return c

def gt1(a, b):
    c = (a > b)
    return c

def and1(a, b):
    c = a and b
    return c

def or1(a, b):
    c = a or b
    return c

def not1(a):
    c = not(a)
    return c

def xor1(a, b):
    x = not(a and b)
    c = (a or b) and x
    return c

def nand1(a, b):
    c = not(a and b)
    return c

def nor1(a, b):
    c = not(a or b)
    return c

def xnor1(a, b):
    x = not(a and b)
    c = not((a or b) and x)
    return c
def add2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = add1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = add1(a, b)
    return c

def sub2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = sub1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = sub1(a, b)
    return c

def div2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = div1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = div1(a, b)
    return c

def mul2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = mul1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = mul1(a, b)
    return c

def mod2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = mod1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = mod1(a, b)
    return c

def lt2(array):
    index = 0
    c = False
    length = len(array)-1
    #print(array)
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            #print([a, b])
            c = lt1(a, b)
        elif index > 0 and c == True:
            a =  array[index]
            index += 1
            b = array[index]
            #print([a, b])
            c = lt1(a, b)
            if c == False:
                return c
        elif index > 0 and c == False:
            return c
    return c

def eq2(array):
    index = 0
    c = False
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = eq1(a, b)
        elif index > 0 and c == True:
            a = array[index]
            index += 1
            b = array[index]
            c = eq1(a, b)
        elif c == False:
            return c
    return c
    
def gt2(array):
    index = 0
    c = False
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = gt1(a, b)
        elif index > 0 and c == True:
            a =  array[index]
            index += 1
            b = array[index]
            c = gt1(a, b)
        elif c == False:
            return c
    return c

def and2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = and1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = and1(a, b)
    return c

def or2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = or1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = or1(a, b)
    return c

def not2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            c = []
            a = array[index]
            index += 1
            c.append(not1(a))
        elif index > 0:
            a = array[index]
            index += 1
            b = array[index]
            c.append(not1(a))
            c.append(not1(b))
    return c

def xor2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = xor1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = xor1(a, b)
    return c

def nand2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = nand1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = nand1(a, b)
    return c

def nor2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = nor1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = nor1(a, b)
    return c

def xnor2(array):
    index = 0
    out = 0.0
    length = len(array)-1
    while index < length:
        if index == 0:
            a = array[index]
            index += 1
            b = array[index]
            c = xnor1(a, b)
        elif index > 0:
            a = c
            index += 1
            b = array[index]
            c = xnor1(a, b)
    return c

def SMA(data, period):
    i = 0
    _data = []
    if gt1(len(data), period):
        while lt1(i,period):
            _data.append(Decimal(data[i]))
            i += 1
        return (div1(add2(_data),period))
    else:
        return Decimal(0)
def EMA(_this, src, length):
    alpha = div1(2, add1(length, 1))
    this = _this
    # Check if 'this' has any previous EMA values
    if len(this) == 0:
        # Initialize the first EMA value to the first source value
        this.prepend(src[0])
        return src[0]
    else:
        # Calculate the current EMA
        current_ema = add1(mul1(alpha, src[0]), mul1(sub1(1, alpha), this[0]))
        this.prepend(current_ema)
        return current_ema
        
def MF(this, src):
    i = 0
    arr = []
    if src[0] > src[1]:
        if (src[0] < 0) or (src[0] > 0 and src[1] < 0):
            a = src[1]*-1
            b = a+src[0]
        return this[0] - b

    elif src[1] > src[0]:
        if (src[1] < 0) or (src[1] > 0 and src[0] < 0):
            a = src[0]*-1
            b = a+src[1]
        return this[0] + b
    else:
        x = Decimal(0)
        return x

def qtyHigherCloses(lookback):
    result = Decimal(0)
    result2 = Decimal(0)
    i = 1
    if gt1(len(v2), lookback):
        while lt1(i, len(v2)-1):
            if gt1(v2[i], 0):
                result += 1
            if and1(lt1(v2[i], 0), gt1(result, 0)):
                #print(result)
                result2 +=  div1(result, 100000)
            i += 1
        return result2
    else:
        return result
def qtyLowerCloses(lookback):
    result = Decimal(0)
    result2 = Decimal(0)
    i = 1
    if gt1(len(v2), 1):
        while lt1(i, lookback):
            if lt1(v2[0], 0):
                result = add1(result, 1)
            if and1(lt1(v2[0], 0), gt1(result, 0)):
                result2 = add1(result2, div1(result, 100000))
            i += 1
        return result2
    else:
        return result

def reverse(arr):
    i = 0
    arr2 = []
    while i < len(arr)-1:
        if (arr[i] == np.nan):
            break
        else:
            arr2.append(arr[len(arr)-(1+i)])
        i += 1
    return arr2
################### Statistics ######################

class trade():
    def __init__(self, id,  contracts, entry_price):
        self.id = id
        #self.trade_number = trade_number
        self.closed = False
        self.contracts = contracts
        self.entry_price = entry_price
        self.exit_price = Decimal()
        #self.date_time = date_time
class Strat():
    def __init__(self, title, pyramiding, initial_capital):
        self.alpaca = False
        self.title = title
        self.pyramiding = pyramiding
        self.initial_capital = initial_capital
        self.trades = []
        self.constructor()
    def constructor(self):
        self.position_avg_price = indicator()
        self.equity = indicator()   #(strategy.initial_capital + strategy.netprofit + strategy.openprofit)
        self.avg_trade = indicator()  #div1(sum2(trades), len(trades))
        self.grossloss = indicator()
        self.max_runup = indicator()
        self.netprofit = indicator()
        self.wintrades = indicator()
        self.eventrades = indicator() #
        self.losstrades = indicator() #
        self.openprofit = indicator() #
        self.opentrades = indicator() #
        self.grossprofit = indicator() #
        self.closedtrades = indicator() #
        self.max_drawdown = indicator() #
        self.position_size = indicator() #
        self.avg_losing_trade = indicator() #
        self.avg_losing_trade_percent = indicator() #
        self.avg_trade_percent = indicator() #
        self.avg_winning_trade = indicator() #
        self.avg_winning_trade_percent = indicator() #
        self.grossloss_percent = indicator() #
        self.grossprofit_percent = indicator() #
        #self.initial_capital = indicator() #
        self.margin_liquidation_price = indicator() #
        self.max_contracts_held_all = indicator() #
        self.max_contracts_held_long = indicator() #
        self.max_contracts_held_short = indicator() #
        self.max_drawdown_percent = indicator() #
        self.max_runup_percent = indicator() #
        self.netprofit_percent = indicator() #
        self.openprofit_percent = indicator() #openPL / realizedEquity * 100
        self.opentrades.capital_held = indicator() #
        self.position_avg_price = indicator() #
        self.position_entry_name = indicator()
    def calc(self):
        #self.equity.prepend(interface.equity())   #(strategy.initial_capital + strategy.netprofit + strategy.openprofit)
        self.avg_trade.prepend(interface.avg_trade())  #div1(sum2(trades), len(trades))
        self.grossloss.prepend(interface.grossloss())
        self.max_runup.prepend(interface.max_runup())
        self.netprofit.prepend(interface.netprofit())
        self.wintrades.prepend(interface.wintrades())
        self.eventrades.prepend(interface.eventrades()) #
        self.losstrades.prepend(interface.losstrades()) #
        self.openprofit.prepend(interface.openprofit()) #
        self.opentrades.prepend(interface.opentrades()) #
        self.grossprofit.prepend(interface.grossprofit()) #
        self.closedtrades.prepend(interface.closedtrades()) #
        self.max_drawdown.prepend(interface.max_drawdown()) #
        self.position_size.prepend(interface.position_size()) #
        self.avg_losing_trade.prepend(interface.avg_losing_trade()) #
        self.avg_losing_trade_percent.prepend(interface.avg_losing_trade_percent()) #
        self.avg_trade_percent.prepend(interface.avg_trade_percent()) #
        self.avg_winning_trade.prepend(interface.avg_winning_trade()) #
        self.avg_winning_trade_percent.prepend(interface.avg_winning_trade_percent()) #
        self.grossloss_percent.prepend(interface.grossloss_percent()) #
        self.grossprofit_percent.prepend(interface.grossprofit_percent()) #
        self.initial_capital.prepend(interface.initial_capital()) #
        self.margin_liquidation_price.prepend(interface.margin_liquidation_price()) #
        self.max_contracts_held_all.prepend(interface.max_contracts_held_all()) #
        self.max_contracts_held_long.prepend(interface.max_contracts_held_long()) #
        self.max_contracts_held_short.prepend(interface.max_contracts_held_short()) #
        self.max_drawdown_percent.prepend(interface.max_drawdown_percent()) #
        self.max_runup_percent.prepend(interface.max_runup_percent()) #
        self.netprofit_percent.prepend(interface.netprofit_percent()) #
        self.openprofit_percent.prepend(interface.openprofit_percent()) #openPL / realizedEquity * 100
        self.opentrades.capital_held.prepend(interface.opentrades.capital_held()) #
        self.position_avg_price.prepend(interface.position_avg_price()) #
        self.position_entry_name.prepend(interface.position_entry_name())
    def close(self, id):
        i = sub2(len(self.trades), 1, self.opentrades)
        contracts = Decimal(0)
        while lt1(i, self.trades):
            if eq1(self.trades[i].signal, id):
                self.trades[i].close_price = close
                self.trades[i].closed = True
                self.opentrades = sub1(self.opentrades, 1)
                if eq1(self.alpaca, True):
                    contracts = add1(contracts, self.trades[i].contracts)
        #(id, comment, qty, qty_percent, alert_message, immediately, disable_alert)
    def entry(self, id, qty, limit, stop, currentprice):
        #(id, direction, qty, limit, stop, oca_name, oca_type, comment, alert_message, disable_alert)
        #if lt1(self.pyramiding, len(self.trades)-1):#self.opentrades[0]):
        _trade = trade(id, qty, currentprice)
        self.trades.append(_trade)
        if eq1(self.alpaca, True): #it also needs to be the current date and price
            a = False#send the trade to alpaca API
    def cancel(self, id):
        if eq1(self.alpaca, True): #it also needs to be the current date and price
            cancel = True#
            _id = id
    def close_all(self):
        if eq1(self.alpaca, True): #it also needs to be the current date and price
            close_all = True
    def cancel_all(self):
        if eq1(self.alpaca, True): #it also needs to be the current date and price
            cancel_all = True

class Interface():
    def equity():
        return add2(strategy.initial_capital, strategy.netprofit[0], strategy.openprofit[0])
    def avg_trade(a):
        i = 0
        avg = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            avg = add1(avg, sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price))
            i += 1
        return div1(avg, i)
    def grossloss():
        i = 0
        gross = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
                if lt1(a, 0):
                    gross = add1(gross, a)
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
                if lt1(a, 0):
                    gross = add1(gross, a)
            i += 1
        return gross
        #
    def grossprofit():
        i = 0
        gross = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
                if gt1(a, 0):
                    gross = add1(gross, a)
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
                if gt1(a, 0):
                    gross = add1(gross, a)
            i += 1
        return gross
        #
    def max_drawdown():#THIS FUNCTION SHOULD loop over price data to determine lowest point while a trade is open
        i = 0
        gross = Decimal(0)
        streaks = []
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            if lt1(a, 0):
                add1(gross, a)
            else:
                streaks.append(gross)
                gross = Decimal(0)
            i += 1
        i = 0
        while lt1(i, sub1(len(streaks), 2)):
            if lt1(streaks[i], streaks[add1(i,1)]):
                gross = streaks[i]
            else:
                gross = streaks[add1(i,1)]
        return gross
        #
    def max_runup():
        i = 0
        gross = Decimal(0)
        streaks = []
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            if gt1(a, 0):
                add1(gross, a)
            else:
                streaks.append(gross)
                gross = Decimal(0)
            i += 1
        i = 0
        while lt1(i, sub1(len(streaks), 2)):
            if gt1(streaks[i], streaks[add1(i,1)]):
                gross = streaks[i]
            else:
                gross = streaks[add1(i,1)]
        return gross
        #
    def netprofit():
        return sub1(strategy.grossprofit[0], strategy.grossloss[0])
    def wintrades():
        i = 0
        wins = 0
        a = Decimal(0)
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
            if gt1(a, 0):
                add1(wins, 1)
            i += 1
        return wins
        #
    def eventrades():
        i = 0
        evens = 0
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            if eq1(a, 0):
                add1(evens, 1)
            i += 1
        return evens
        #
    def losstrades():
        i = 0
        losses = 0
        a = Decimal(0)
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
            if lt1(a, 0):
                add1(losses, 1)
            i += 1
        return losses
        #
    def openprofit():
        i = 0
        profit = Decimal(0)
        while lt1(i, sub2(len(strategy.trades), 1, strategy.opentrades[0])):
            a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            if and1(lt1(a, 0), not1(strategy.trades[i].closed)):
                profit = add1(profit, a)
            i += 1
        return profit
        #
    def opentrades():
        i = 0
        trades_open = 0
        while lt1(i, sub1(len(strategy.trades), 1)):
            if not1(strategy.trades[i].closed):
                trades_open = add1(trades_open, 1)
            i += 1
        return trades_open
        #
    def closedtrades():
        i = 0
        trades_closed = 0
        while lt1(i, sub1(len(strategy.trades), 1)):
            if strategy.trades[i].closed:
                trades_closed = add1(trades_closed, 1)
            i += 1
        return trades_closed
        #
    def position_size():
        i = 0
        position = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), 1)):
            if not1(strategy.trades[i].closed):
                add1(position, strategy.trades[i].contracts)
            i += 1
        return position
        #
    def avg_losing_trade():
        i = 0
        gross = Decimal(0)
        losses = 0
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
            if lt1(a, 0):
                add1(gross, a)
                add1(losses, 1)
            i += 1
        return div1(gross, losses)
        #
    def avg_losing_trade_percent(self):
        #losing_trade_position
        return div1(self.avg_losing_trade(), 100)
        #
    def avg_winning_trade():
        i = 0
        gross = Decimal(0)
        percent = Decimal(0)
        wins = 0
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
                c = strategy.trades[i].contracts
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
                c = strategy.trades[i].contracts
            if gt1(a, 0):
                gross = add1(gross, mul1(a, c))
                wins = add1(wins, 1)
            i += 1
        return div1(gross, wins)
        #
    def avg_winning_trade_percent(self):
        i = 0
        gross = Decimal(0)
        percent = Decimal(0)
        wins = 0
        while lt1(i, sub1(len(strategy.trades), strategy.opentrades[0])):
            if eq1(strategy.trades[i].direction, 'long'):
                a = sub1(strategy.trades[i].close_price, strategy.trades[i].entry_price)
                c = strategy.trades[i].contracts
                if gt1(a, 0):
                    cost_basis = mul1(strategy.trades[i].entry_price, c)
                    gross = add1(gross, mul1(a, c))
                    percent = add1(div1(gross, cost_basis))
                    wins = add1(wins, 1)
            elif eq1(strategy.trades[i].direction, 'short'):
                a = sub1(strategy.trades[i].entry_price, strategy.trades[i].close_price)
                c = strategy.trades[i].contracts
                if gt1(a, 0):
                    cost_basis = mul1(strategy.trades[i].entry_price, c)
                    gross = add1(gross, mul1(a, c))
                    percent = add1(div1(gross, cost_basis))
                    wins = add1(wins, 1)
            i += 1
        return mul1(div1(percent, wins), 100)
        #
    def grossloss_percent(self):
        return div1(self.grossloss(), strategy.initial_capital)
        #
    def grossprofit_percent(self):
        return div1(self.grossprofit(), strategy.initial_capital)
        #
    def max_contracts_held_all():
        i = 0
        contracts = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), 1)):
            if lt1(contracts, trades[i].contracts):
                contracts = trades[i].contracts
            i += 1
        return contracts
        #
    def max_contracts_held_long():
        i = 0
        contracts = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), 1)):
            if and1(lt1(contracts, trades[i].contracts), eq1(trades[i].direction, 'long')):
                contracts = trades[i].contracts
            i += 1
        return contracts
        #
    def max_contracts_held_short():
        i = 0
        contracts = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), 1)):
            if and1(lt1(contracts, trades[i].contracts), eq1(trades[i].direction, 'short')):
                contracts = trades[i].contracts
            i += 1
        return contracts
        '''#
    def max_drawdown_percent():
        #
    def max_runup_percent():
        #
    def netprofit_percent():
        #
    def openprofit_percent():
        #openPL / realizedEquity * 100
        '''
    def position_avg_price():
        i = 0
        contracts = Decimal(0)
        price = Decimal(0)
        a = Decimal(0)
        b = Decimal(0)
        count = Decimal(0)
        while lt1(i, sub1(len(strategy.trades), 1)):
            if not1(strategy.trades[i].closed):
                contracts = trades[i].contracts
                count = add1(count, contracts)
                price = trades[i].entry_price
                a = mul1(contracts, price)
                b = add1(b, a)
            i += 1
        return div1(b, count)

class calculate():
    def sma100(globals):
        if gt1(len(W_C), 100):
            sma100.prepend(SMA(W_C, 100))
        else:
            sma100.prepend(Decimal(0))
    def V(globals):
        V.prepend(sub1(W_C[0], sma100[0]))
    def v2(globals):
        if gt1(len(V), 100):
            v2.prepend(SMA(V, 100))
        else:
            v2.prepend(Decimal(0))
    def D(globals):
        D.prepend(sub1(W_C[0], W_O[0]))
    def D1(globals):
        i = 0
        a = []
        while lt1(i, len(W_C)):
            a.append(sub1(W_C[i],W_O[i]))
            i += 1
        D1.prepend(SMA(a, 50))
    def D2(globals):
        i = 0
        a = []
        while i < len(W_C):
            a.append(sub1(W_C[i],W_O[i]))
            i += 1
        D2.prepend(SMA(a, 200))
    def D0(globals):
        i = 0
        a = []
        while i < len(W_C):
            a.append(sub1(W_C[i],W_O[i]))
            i += 1
        D0.prepend(div1(SMA(a, 2), 2))
    def D01(globals):
        D01.prepend(SMA(D0, 25))
    def D02(globals):
        D02.prepend(SMA(D0, 100))
    def D4(globals):
        if len(D4) > 200:
            if len(D2) > 1:
                a = EMA(D4, D2, 200)
                D4.prepend(a)
        else:
            D4.prepend(Decimal(0))
    def D3(globals):
        if len(D1) > 0 and len(D3) > 1:
            a = EMA(D3, D1, 50)
            if a < 0:
                _a =a *-1
                _b = D4[0] - _a
            D3.prepend(a)
        else:
            D3.prepend(D1[0])
        
    def D00(globals):
        D00.prepend(add2([D01[0], D02[0], D3[0]]))
    def DMF(globals):
        if gt1(len(DMF), 0) and gt1(len(D), 1):
            DMF.prepend(Decimal(0))
            a = Decimal(0)
            if D[0] > (D[1] + Decimal(0.001)):
                a = DMF[1] - (D[1] - D[0])
                DMF[0] = a
            elif (D[0] + Decimal(0.001)) < D[1]:
                a = DMF[1] + (D[0] - D[1])
                DMF[0] = a
                
        else:
            DMF.prepend(Decimal(0))
                          
        #print(['DMF', DMF[0]])
    def DMF0(globals):
        if gt1(len(DMF), 14):
            #print(['DMF0', SMA(DMF, 14)])
            DMF0.prepend(SMA(DMF, 14))
        else:
            DMF0.prepend(Decimal(0))
    def DMF00(globals):
        if gt1(len(DMF), 120):
            DMF00.prepend(SMA(DMF, 120))
        else:
            DMF00.prepend((Decimal(0)))
    def hist1(globals):
        if gt1(len(DMF0), 0):
            #print([DMF0[0], D00[0]], sub1(DMF0[0], D00[0]))
            a = sub1(DMF0[0], D00[0])
            hist1.prepend(a)
            #print(hist1[0])
        else:
            hist1.prepend(Decimal(0))
    def CALL(globals):
        if and1(gt1(len(D00), 0), gt1(len(hist1), 1)):
            CALL.prepend(and2([lt1(D00[0], hist1[0]), lt1(hist1[1], D00[0]), lt1(hist1[0], 0)]))
            if and1(CALL[0], True):
                print(['CALL:', price[0]])
        else:
            CALL.prepend(False)
        print(['Call:', CALL[0], price[0]])
    
    def CloseShortTermCall(globals):
        if and1(gt1(len(strategy.position_avg_price), 1), gt1(len(D00), 1)):# and gt1(len(close), 1))
            CloseShortTermCall.prepend(and1(gt1(D00[0], 0), gt1(close[0], mul1(div1(strategy.position_avg_price[0], 100), 101))))
        else:
            CloseShortTermCall.prepend(False)
        #print(['CloseCall:',CloseShortTermCall[0], price[0]])
    def CloseLongTermCall(globals):
        if and2([gt1(len(V), 1), gt1(len(strategy.position_avg_price), 1), gt1(len(D00), 1)]):
            CloseLongTermCall.prepend(and2([crossover(div1(V[0], 10), 0), gt1(D00[0], 0), gt1(close[0], mul1(div1(strategy.position_avg_price[0], 100), 105))]))
        else:
            CloseLongTermCall.prepend(False)
    def vCount(globals):
        if gt1(v2[0], 0):
            vCount.prepend(add1(vCount[1], 1))
        else:
            vCount.prepend(Decimal(1))
    def vCount2(globals):
        if lt1(v2[0], 0):
            vCount2.prepend(add1(vCount2[1], 1))
        else:
            vCount2.prepend(Decimal(1))
    def rT(globals):
        result = Decimal(0)
        result2 = Decimal(0)
        i = 1
        if gt1(len(v2), 100):
            for i in range(100):#while lt1(i, 100):
                if gt1(v2[i], 0):
                    result += 1
                i += 1
            rT.prepend((add1(rT[0],result)))
            i = 1
            for i in range(100):#while lt1(i, 100):
                if and1(lt1(v2[i], 0), gt1(rT[i], 0)):
                    result2 += div1(rT[0], 100000)
                i += 1
            T.prepend((add1(T[0],result2)))
            result3 = Decimal(0)
            result4 = Decimal(0)
            i = 1
            for i in range(100):#while lt1(i, 100):
                if lt1(v2[i], 0):
                    result3 += 1
                i += 1
            rT2.prepend((add1(rT2[0],result3)))
            i = 1
            for i in range(100):#while lt1(i, 100):
                if and1(gt1(v2[i], 0), gt1(rT2[i], 0)):
                    result4 += div1(rT2[0], 100000)
                i += 1
            nT.prepend((add1(nT[0],result4)))

            #print(rT2[0])
            #print(nT[0])
        else:
            rT.prepend(Decimal(0)-9900)
            T.prepend(add1(Decimal(0), 66.9827))
            rT2.prepend(Decimal(0))
            nT.prepend(sub1(Decimal(0), 44.74115))
    def rT2(globals):
        a = Decimal(0)#rT2.prepend(qtyHigherCloses(100))
    def T(globals):
        a = Decimal(0)
    def nT(globals):
        a = Decimal(0)
        #nT.prepend(qtyLowerCloses(100))
    def T0n(globals):
        if and1(gt1(len(nT), 0), gt1(len(T), 0)):
            T0n.prepend(div1(nT[0], T[0]))
        else:
            T0n.prepend(Decimal(0))
    def VcountFlow(globals):
        VcountFlow.prepend(add1(div1(vCount[0], vCount2[0]), 1))
    def closeT0(globals):
        i = 0
        a = Decimal(0)
        if gt1(len(T0n), 100):
            while lt1(i, 100):
                a += div1(close[i], T0n[i])
                i += 1
            closeT0.prepend(div1(a, 100))#this is a problem for sma
        else:
            closeT0.prepend(Decimal(0))
    def Ton(globals):
        if and1(gt1(len(closeT0), 1), gt1(len(sma100), 1)):
            if eq1(sma100[0], 0):
                Ton.prepend(Decimal(0))
            else:
                Ton.prepend(div1(closeT0[0], sma100[0]))
        else:
            Ton.prepend(Decimal(0))
    def TMF(globals):
        if and1(gt1(len(Ton), 2), gt1(len(TMF), 1)):
            if gt1(Ton[0], Ton[1]):
                TMF.prepend(sub1(TMF[1], mul1(1, sub1(Ton[1], Ton[0]))))
            elif and1(lt1(Ton[0], Ton[1]), lt1(Ton[0], 1)):#and1(lt3(Ton[0], [Ton[1], 1]))
                TMF.prepend(add1(TMF[1], mul1(1, sub1(Ton[0], Ton[1]))))
            else:
                TMF.prepend(Decimal(0))
        else:
            TMF.prepend(Decimal(0))
    def TMF0(globals):
        TMF0.prepend(SMA(TMF, 14))
    def PUT(globals):
        PUT.prepend(and2([gt1(DMF00[0], hist1[0]), gt1(hist1[0], 0), gt1(D00[0], 0)]))
        #if and1(PUT[0], True):
        #print(['PUT:', PUT[0], price[0]])
        
    def ClosePUT(globals):
        ClosePUT.prepend(and2([lt1(div1(V[0], 10), hist1[0]), lt1(hist1[0], 0), crossover(DMF0[0], div1(V[0], 10))]))
        #if and1(ClosePUT[0], True):
            #print(['ClosePUT:',  price[0]])
        print(['ClosePUT:',ClosePUT[0], price[0]])
    
    def longOpened(globals):
        if gt1(len(longOpened), 2):
            if or1(gt1(longOpened[1], 1), eq1(longOpened[1], 1)):#these index values need to be fixed
                if gt1(longOpened, 100):
                    longOpened.prepend(Decimal(0))
                else:
                    longOpened.prepend(add1(longOpened[1], 1))
            elif nor1(gt1(longOpened[1], 1), eq1(longOpened[1], 1)):
                longOpened.prepend(Decimal(0))
        else:
            longOpened.prepend(Decimal(0))
    def shortClosed(globals):
        if gt1(len(shortClosed), 2):
            if or1(gt1(shortClosed[1], 1), eq1(shortClosed[1], 1)):
                shortClosed.prepend(add1(shortClosed[1], 1))
                if gt1(shortClosed, 100):  #//and longOpened > 0
                    shortClosed.prepend(Decimal(0))                
            elif nor1(gt1(shortClosed[1], 1), eq1(shortClosed[1], 1)):
                shortClosed.prepend(Decimal(0))
        else:
            shortClosed.prepend(Decimal(0))
    def offDays(globals):
        if and1(gt1(len(strategy.position_size), 1), gt1(len(offDays), 2)):
            if not1(eq1(strategy.position_size[0], 0)):
                offDays.prepend(Decimal(0))
            else:
                offDays.prepend(add1(offDays[1], 1))
        else:
            offDays.prepend(Decimal(0))
    def onDays(globals):
        if and1(gt1(len(strategy.position_size), 1), gt1(len(onDays), 2)):
            if not1(eq1(strategy.position_size[0], 0)):
                onDays.prepend(add1(onDays[1], 1))
            else:
                onDays.prepend(Decimal(0))
        else:
            onDays.prepend(Decimal(0))
    def CumAlpha(globals):
        mod = Decimal(0)
        if and2([gt1(len(strategy.position_size), 1), gt1(len(offDays), 1), gt1(len(CumAlpha), 2), gt1(len(W_C), 2)]):
            if not1(eq1(strategy.position_size[0], 0)):
                mod = Decimal(CumAlpha[1])
                mods += 1
            if or1(eq1(offDays[0], 1), gt1(offDays[0], 1)):
                mod = add1(CumAlpha[1], mul1(div1(sub1(W_C[0], W_C[1]), W_C[offDays[0]])), 100)
                mods += 1
        CumAlpha.prepend(mod)
    def market(globals):
        if eq1(offDays[0], 1):
            market.prepend(mul1(div1(sub1(W_C[0], W_C[1]), W_C[offDays[0]])), 100)
        elif gt1(offDays[0], 1):
            market.prepend(add1(market[1], (mul1(div1(sub1(W_C[0], W_C[1]), W_C[offDays[0]])), 100)))
    def CumVega(globals):
        if eq1(onDays[0], 1):
            CumVega.prepend(add1(CumVega[1], (mul1(div1(sub1(W_C[0], W_C[1]), W_C[onDays[0]])), 100)))
        elif gt1(onDays[0], 1):
            CumVega.prepend(add1(CumVega[1], (mul1(div1(sub1(W_C[0], W_C[1]), W_C[onDays[0]])), 100)))
    def market1(globals):
        if eq1(onDays[0], 1):
            market1.prepend((mul1(div1(sub1(W_C[0], W_C[1]), W_C[onDays[0]])), 100))
        elif gt1(onDays[0], 1):
            market1.prepend(add1(market1[1], (mul1(div1(sub1(W_C[0], W_C[1]), W_C[onDays[0]])), 100)))
    def cc(globals):
        mod = Decimal(0)
        if and1(gt1(len(cc), 2), gt1(len(CloseShortTermCall), 1)):
            if eq1(CALL, 1):
                mod = (add1(cc[1], 1))
            else:
                mod = (cc[1])
            if eq1(CloseShortTermCall[0], True):
                mod =  Decimal(0)
        cc.prepend(mod)

def callChain():
    W_C = SPYclose
    W_O = SPYopen
    calc.sma100()
    calc.V()
    calc.v2()
    calc.D()
    calc.D1()
    calc.D2()
    calc.D0()
    calc.D01()
    calc.D02()
    calc.D4()
    calc.D3()
    

    calc.D00()
    calc.DMF()
    calc.DMF0()
    calc.DMF00()

    calc.hist1()
    calc.CALL()
    calc.CloseShortTermCall()
    #calc.CloseLongTermCall()
    #calc.vCount()
    #calc.vCount2()
    calc.rT()
    #calc.T()

    #calc.rT2()
    #calc.nT()
    calc.T0n()
    #calc.VcountFlow()
    calc.closeT0()
    calc.Ton()
    #calc.TMF()
    #calc.TMF0()
    calc.PUT()
    calc.ClosePUT()
    calc.longOpened()
    calc.shortClosed()
    calc.offDays()
    calc.onDays()
    calc.CumAlpha()
    calc.market()
    calc.CumVega()
    calc.market1()
    calc.cc()
################### Indicators & Data ####################

strategy = Strat('Quantum Simple', 10, 1000000)
interface = Interface()
#NYSElist = ['A','AA','AACG','AACT', 'AADI', 'AAL', 'AAM', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAT', 'AB', 'ABAT', 'ABBV', 'ABCB', 'ABEO', 'ABEV', 'ABG', 'ABL', 'ABLV', 'ABM', 'ABNB', 'ABOS', 'ABR', 'ABSI', 'ABT', 'ABTS', 'ABUS', 'ABVC', 'AC', 'ACA', 'ACAD', 'ACB', 'ACCD', 'ACCO', 'ACDC', 'ACEL', 'ACGL', 'ACHC', 'ACHL', 'ACHR', 'ACHV', 'ACI', 'ACIC', 'ACIW', 'ACLS', 'ACLX', 'ACM', 'ACMR', 'ACN', 'ACNB', 'ACNT', 'ACOG', 'ACP', 'ACR', 'ACRE', 'ACRS', 'ACRV', 'ACT', 'ACTU', 'ACU', 'ACV', 'ACVA', 'ACXP', 'ADAG', 'ADAP', 'ADBE', 'ADC', 'ADD', 'ADEA']
ticker = "UPRO"
priceData = yf.download("SPY", start='2000-01-01')
SPYopen = reverse(pd.Series(priceData.Open))
SPYclose = reverse(pd.Series(priceData.Close))
priceData2 = yf.download(ticker, start='2009-06-25')
open = reverse(pd.Series(priceData2.Open))
high = reverse(pd.Series(priceData2.High))
low = reverse(pd.Series(priceData2.Low))
close = reverse(pd.Series(priceData2.Close))
#print(close[0], close[1]) the price data is now relative to the present

W_C = indicator()
W_O = indicator()
sma100 = indicator()
V = indicator()
v2 = indicator()
D = indicator()
D1 = indicator()
D2 = indicator()
D0 = indicator()
D01 = indicator()
D02 = indicator()
D4 = indicator()
D3 = indicator()
D00 = indicator()
DMF = indicator()
DMF0 = indicator()
DMF00 = indicator()
hist1 = indicator()
CALL = indicator()
CloseShortTermCall = indicator()
CloseLongTermCall = indicator()
vCount = indicator()
vCount2 = indicator()


rT = indicator()
rT2 = indicator()
T = indicator()
nT = indicator()
T0n = indicator()
VcountFlow = indicator()
closeT0 = indicator()
Ton = indicator()
TMF = indicator()
TMF0 = indicator()
PUT = indicator()
ClosePUT = indicator()
longOpened = indicator()
shortClosed = indicator()
offDays = indicator()
onDays = indicator()
CumAlpha = indicator()
market = indicator()
CumVega = indicator()    
market1 = indicator()
cc = indicator()

price = indicator()
calc = calculate()

def backtester():
    #strategy.opentrades.prepend(0)
    priceData2 = yf.download(ticker, start='2009-06-25')
    open = reverse(pd.Series(priceData2.Open))
    #high = reverse(pd.Series(priceData2.High))
    low = reverse(pd.Series(priceData2.Low))
    close = reverse(pd.Series(priceData2.Close))
    SPYopen = reverse(pd.Series(priceData.Open))
    SPYclose = reverse(pd.Series(priceData.Close))
    SPYclose = reverse(SPYclose)
    SPYopen = reverse(SPYopen)

    mintick = Decimal(0.01)
    #close = reverse(close)
    #trade_id = 1
    i = (len(SPYclose) - len(close))
    j = len(close)-1
    #print(j)
    PUTqty = Decimal(0)
    PUTprice = Decimal(0)
    CALLqty = Decimal(0)
    CALLprice = Decimal(0)
    short_pl = Decimal(0)
    long_pl = Decimal(0)
    while lt1(i, len(SPYclose)):
        W_C.prepend(SPYclose[i])
        W_O.prepend(SPYopen[i])
        price.prepend(close[j])
        print(['calc', i, price[0]])
        callChain()
        #strategy.calc()
        if eq1(PUT[0], True):
            if CALLqty > 0:
                strategy.entry('CloseCALL', CALLqty, 0 ,0, price[0])
                strategy.trades[len(strategy.trades)-1].exit_price = div1(CALLprice, CALLqty)
                long_pl = add1(long_pl,  mul1(sub1(price[0], div1(CALLprice, CALLqty)), CALLqty))
                CALLqty = Decimal(0)
                CALLprice = Decimal(0)
            qty = div2([strategy.initial_capital, close[j], 3])
            stop = sub1(open[j], mul1(6, mintick))
            strategy.entry('PUT', qty, 0, stop, price[0])
            PUTqty = add1(PUTqty, qty)
            PUTprice = add1(PUTprice, mul1(qty, price[0]))
        if eq1(ClosePUT[0], True):
            strategy.entry('ClosePUT', PUTqty, 0 ,0, price[0])
            PUTqty = Decimal(0)
            PUTprice = Decimal(0)
        if eq1(CALL[0], True):
            if PUTqty > 0:
                strategy.entry('ClosePUT', PUTqty, 0 ,0, price[0])
                strategy.trades[len(strategy.trades)-1].exit_price = div1(PUTprice, PUTqty)
                short_pl = add1(short_pl,  mul1(sub1(div1(PUTprice, PUTqty), price[0]), PUTqty))
                PUTqty = Decimal(0)
                PUTprice = Decimal(0)
            qty = div2([strategy.initial_capital, close[j], 3])
            stop = sub1(low[j], mul1(6, mintick))
            strategy.entry('CALL', qty, 0, stop, price[0])
            CALLqty = add1(CALLqty, qty)
            CALLprice = add1(CALLprice, mul1(qty, price[0]))
        if eq1(CloseShortTermCall[0], True):
            if CALLqty > 0:
                strategy.entry('CloseCALL', CALLqty, 0 ,0, price[0])
                strategy.trades[len(strategy.trades)-1].exit_price = div1(CALLprice, CALLqty)
                long_pl = add1(long_pl,  mul1(sub1(price[0], div1(CALLprice, CALLqty)), CALLqty))
                CALLqty = Decimal(0)
                CALLprice = Decimal(0)
            strategy.close('CALL')
            #CALLqty = Decimal(0)
        
        i += 1
        j -= 1
    if and1(gt1(len(hist1), 1), gt1(i, 50)):
        #print(strategy.trades)
        print(['SPY:', W_C[0]])
        print(['D', D[0]])#matches current
        print(['D[1]', D[1]])
        print(['D[2]', D[2]])
        print(['D1', D1[0]])#matches current
        print(['D3', D3[0]])
        print(['D3[1]', D3[1]])
        print(['D3[2]', D3[2]])
        print(['D3[3]', D3[3]])
        print(['D4', D4[0]])
        print(['D01', D01[0]])
        print(['D02', D02[0]])
        
        print(['D00', D00[0]])
        print(['D00[1]', D00[1]])
        print(['D00[2]', D00[2]])
        print(['DMF', DMF[0]])
        print(['DMF[1]', DMF[1]])
        print(['DMF[2]', DMF[2]])
        print(['DMF0', DMF0[0]])
        print(['DMF00', DMF00[0]])
        print(['hist1', hist1[0]])
        print(['hist1[1]', hist1[1]])
        print(['CALL', CALL[0]])
        print(['CALL[1]', CALL[1]])
        print(['CALL[2]', CALL[2]])
        print(['CloseShortTermCall', CloseShortTermCall[0]])
        print(['CloseShortTermCall[1]', CloseShortTermCall[1]])
        print(['CloseShortTermCall[2]', CloseShortTermCall[2]])
        
        print(['v2', v2[0]])
        print(['v2[1]', v2[1]])
        print(['v2[2]', v2[2]])
        print(['rT', rT[0]])
        print(['rT[1]', rT[1]])
        print(['T', T[0]])
        print(['T[1]', T[1]])
        print(['T[2]', T[2]])
        print(['rT2', rT2[0]])
        print(['rT2[1]', rT2[1]])
        print(['nT', nT[0]])
        print(['nT[1]', nT[1]])
        print(['nT[2]', nT[2]])
        print(['T0n', T0n[0]])
        print(['T0n[1]', T0n[1]])
        print(['T0n[2]', T0n[2]])
        print(['closeT0',closeT0[0]])
        print(['closeT0[1]',closeT0[1]])
        print(['closeT0[2]',closeT0[2]])
        print(['Ton', Ton[0]])
        print(['Ton[1]', Ton[1]])
        print(['Ton[2]', Ton[2]])
        print(['PUT', PUT[0]])
        print(['PUT[1]', PUT[1]])
        print(['ClosePUT', ClosePUT[0]])
        print(['ClosePUT[1]', ClosePUT[1]])
        print(['longOpened', longOpened[0]])
        print(['longOpened[1]', longOpened[1]])
        print(['shortClosed', shortClosed[0]])
        print(['shortClosed[1]', shortClosed[1]])
        print(['short_pl', short_pl])
        print(['long_pl', long_pl])


########################################
backtester()
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