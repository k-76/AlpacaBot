import safemath
import api_data as api
class trade():
    def __init__(self, date, id,  contracts, entry_price):
        if safemath.lt1(contracts, 0):
            self.direction = 'short'
        else:
            self.direction = 'long'
        self.id = id
        self.entry_date = date
        self.closed = False
        self.contracts = contracts
        self.entry_price = entry_price
        self.exit_price = safemath.Decimal(0)
class Strat():
    def __init__(self, title, pyramiding, initial_capital):
        self.alpaca = False
        self.title = title
        self.pyramiding = pyramiding
        self.initial_capital = initial_capital
        self.trades = []
        self.constructor()
    def constructor(self):

        self.entry_cost = api.indicator()
        self.entry_cost.prepend(0)
        self.position_size = api.indicator() #
        self.position_size.prepend(0)
        self.position_avg_price = api.indicator()
        
        self.avg_trade = api.indicator()  #safemath.div1(sum2(trades), len(trades))
        self.net_long_pl = api.indicator()
        self.net_short_pl = api.indicator()
        self.gross_long_profits = api.indicator()
        self.gross_long_losses = api.indicator()
        self.gross_short_profits = api.indicator()
        self.gross_short_losses = api.indicator()
        self.winning_short_trades = api.indicator()
        self.winning_long_trades = api.indicator()
        self.losing_long_trades = api.indicator()
        self.losing_short_trades = api.indicator()
        
        self.grossloss = api.indicator()
        self.netprofit = api.indicator()
        self.wintrades = api.indicator()
        self.losstrades = api.indicator() #
        self.grossprofit = api.indicator() #
        self.opentrades = api.indicator() #
        self.closedtrades = api.indicator() #
        #self.max_runup = api.indicator()
        self.openprofit = api.indicator() #
        self.max_drawdown = api.indicator() #
        self.avg_losing_trade = api.indicator() #
        self.avg_losing_trade_percent = api.indicator() #
        self.avg_trade_percent = api.indicator() #
        self.avg_winning_trade = api.indicator() #
        self.avg_winning_trade_percent = api.indicator() #
        self.grossloss_percent = api.indicator() #
        self.grossprofit_percent = api.indicator() #
        self.max_drawdown_percent = api.indicator() #
        self.max_runup_percent = api.indicator() #
        self.netprofit_percent = api.indicator() #
        self.openprofit_percent = api.indicator() #openPL / realizedEquity * 100
        #self.initial_capital = api.indicator() #
        self.margin_liquidation_price = api.indicator() #
        self.max_contracts_held_all = api.indicator() #
        self.max_contracts_held_all.prepend(0)
        self.max_contracts_held_long = api.indicator() #
        self.max_contracts_held_long.prepend(0)
        self.max_contracts_held_short = api.indicator() #
        self.max_contracts_held_short.prepend(0)
        self.opentrades.capital_held = api.indicator() #
        self.position_entry_name = api.indicator()
    def calc2(self, _from):
        net_long_pl = 0
        net_short_pl = 0
        gross_long_profits = 0
        gross_long_losses = 0
        gross_short_profits = 0
        gross_short_losses = 0
        winning_short_trades = 0
        winning_long_trades = 0
        losing_long_trades = 0
        losing_short_trades = 0
        win_trades = 0
        loss_trades = 0
        position_avg_price = 0
        if safemath.eq1(_from, True):
            k = 0
            while safemath.lt1(k, len(self.trades)):
                a = safemath.mul1(self.trades[k].contracts, self.trades[k].entry_price)
                b = safemath.mul1(self.trades[k].contracts, self.trades[k].exit_price)
                #print([self.trades[k].contracts , self.trades[k].entry_price, self.trades[k].exit_price])
                if safemath.eq1(self.trades[k].direction, 'short'):
                    short_pl = safemath.sub1(a, b)
                    long_pl = 0
                    if safemath.lt1(short_pl, 0):
                        gross_short_profits = safemath.sub1(gross_short_profits, short_pl)
                        winning_short_trades = safemath.add1(winning_short_trades, 1)
                    elif safemath.gt1(short_pl, 0):
                        gross_short_losses = safemath.sub1(gross_short_losses, short_pl)
                        losing_short_trades = safemath.add1(losing_short_trades, 1)
                elif safemath.eq1(self.trades[k].direction, 'long'):
                    long_pl = safemath.sub1(b, a)
                    short_pl = 0
                    if safemath.gt1(long_pl, 0):
                        gross_long_profits = safemath.add1(gross_long_profits, long_pl)
                        winning_long_trades = safemath.add1(winning_long_trades, 1)
                    elif safemath.lt1(long_pl, 0):
                        gross_long_losses = safemath.add1(gross_long_losses, long_pl)
                        losing_long_trades = safemath.add1(losing_long_trades, 1)
                net_long_pl = safemath.add1(net_long_pl, long_pl)
                net_short_pl  = safemath.sub1(net_short_pl, short_pl)
                win_trades = safemath.add1(winning_long_trades, winning_short_trades)
                loss_trades = safemath.add1(losing_long_trades, losing_short_trades)
                #print([self.trades[k].direction, ['gross_long_pl', gross_long_profits, gross_long_losses]])
                #print([self.trades[k].direction, ['gross_short_pl', gross_short_profits, gross_short_losses]])
                k += 1
        else:
            if safemath.eq1(len(self.net_long_pl), 0):
                net_long_pl = 0
                net_short_pl = 0
                gross_long_profits = 0
                gross_long_losses = 0
                gross_short_profits = 0
                gross_short_losses = 0
                winning_short_trades = 0
                winning_long_trades = 0
                losing_long_trades = 0
                losing_short_trades = 0
                win_trades = 0
                loss_trades = 0
                open_contracts = 0
                position_avg_price = 0
            else:        
                position_avg_price = 0
                open_contracts = 0
                entry_cost = 0
                k = 0
                while k < len(self.trades):
                    if  safemath.eq1(self.trades[k].closed, False):
                        a = safemath.mul1(self.trades[k].contracts , self.trades[k].entry_price)
                        entry_cost = safemath.add1(entry_cost, a)
                        open_contracts = safemath.add1(open_contracts, self.trades[k].contracts)
                        position_avg_price = safemath.div1(entry_cost, open_contracts)
                    k += 1
                net_long_pl = self.net_long_pl[0]
                net_short_pl = self.net_short_pl[0]
                gross_long_profits = self.gross_long_profits[0]
                gross_long_losses = self.gross_long_losses[0]
                gross_short_profits = self.gross_short_profits[0]
                gross_short_losses = self.gross_short_losses[0]
                winning_short_trades = self.winning_short_trades[0]
                winning_long_trades = self.winning_long_trades[0]
                losing_long_trades = self.losing_long_trades[0]
                losing_short_trades = self.losing_short_trades[0]
                win_trades = self.wintrades[0]
                loss_trades = self.losstrades[0]
        self.position_avg_price.prepend(position_avg_price)
        self.gross_long_profits.prepend(gross_long_profits)
        self.gross_long_losses.prepend(gross_long_losses)
        self.gross_short_profits.prepend(gross_short_profits)
        self.gross_short_losses.prepend(gross_short_losses)
        self.winning_short_trades.prepend(winning_short_trades)
        self.winning_long_trades.prepend(winning_long_trades)
        self.losing_long_trades.prepend(losing_long_trades)
        self.losing_short_trades.prepend(losing_short_trades)
        self.net_long_pl.prepend(net_long_pl)
        self.net_short_pl.prepend(net_short_pl)
        self.wintrades.prepend(win_trades)
        self.losstrades.prepend(loss_trades)
            
    def close(self, id, currentprice):
        def LOG_TRADE(calc_spec):
            if calc_spec:
                self.trades[i].exit_price = safemath.Decimal(currentprice)
                self.trades[i].closed = True
                a = self.position_size[0]
                b =self.trades[i].contracts
                #print([a, b])
                if safemath.eq1(len(self.closedtrades),0):
                    #self.position_size.prepend(safemath.sub1(a, b))
                    self.closedtrades.prepend(safemath.Decimal(1))
                    return b
                else:
                    #self.position_size.prepend(safemath.sub1(a, b))
                    self.closedtrades.prepend(safemath.add1(self.closedtrades[0], 1))
                    return b
            return 0
        i = 0
        k = 0
        x = safemath.Decimal(0)
        while len_spec := safemath.lt1(i, len(self.trades)):
            calc_spec = safemath.and1(safemath.eq1(self.trades[i].id, id), safemath.eq1(self.trades[i].closed, False))
            if calc_spec:
                k +=1
            x  = safemath.add1(x, LOG_TRADE(calc_spec))
            i += 1
        r = self.opentrades[0] - k
        self.position_size.prepend(safemath.sub1(self.position_size[0], x))
        if k > 0:
            print(['closed', id, currentprice, k, x, self.position_size[0]])
        self.opentrades.prepend(r) # account for new entry #this is apparently very important
    def entry(self, date, id, qty, limit, stop, currentprice):
        def LOG_TRADE(date, id, qty, currentprice):
            if safemath.eq1(len(self.opentrades),0):
                _trade = trade(date, id, qty, currentprice)
                self.trades.append(_trade)
                self.opentrades.prepend(safemath.Decimal(1))
                self.entry_cost.prepend(safemath.add1(self.entry_cost[0], safemath.mul1(qty, currentprice)))
                self.position_size.prepend(safemath.add1(self.position_size[0], qty))
                print(['opened', id, currentprice, self.opentrades[0], self.position_size[0]])
            else: 
                if safemath.or2([safemath.lt1(self.opentrades[0], self.pyramiding), safemath.and1(safemath.lt1(self.position_size[0], 0), safemath.eq1(id, 'CALL')), safemath.and1(safemath.gt1(self.position_size[0], 0), safemath.eq1(id, 'PUT'))]):
                    
                    _trade = trade(date, id, qty, currentprice)
                    self.trades.append(_trade)
                    self.opentrades.prepend(safemath.add1(self.opentrades[0], 1))
                    self.entry_cost.prepend(safemath.add1(self.entry_cost[0], safemath.mul1(qty, currentprice)))
                    self.position_size.prepend(safemath.add1(self.position_size[0], qty))
                    print(['opened', id, currentprice, self.opentrades[0], self.position_size[0]])
            #print(['opened', self.opentrades[0], id, ['qty:' , qty], currentprice, self.position_size[0]])
        LOG_TRADE(date, id, qty, currentprice)
        if safemath.eq1(self.alpaca, True): #it also needs to be the current date and price
            a = False#send the trade to alpaca API
    def cancel(self, id):
        if safemath.eq1(self.alpaca, True): #it also needs to be the current date and price
            cancel = True#
            _id = id
    def close_all(self):
        if safemath.eq1(self.alpaca, True): #it also needs to be the current date and price
            close_all = True
    def cancel_all(self):
        if safemath.eq1(self.alpaca, True): #it also needs to be the current date and price
            cancel_all = True

strategy = Strat('Quantum Simple', 10, 1000000)
