import safemath
import strategy_interface
import indicators as ind
import api_data as api

################ math library #########################


def backtester():

    mintick = safemath.Decimal(0.01)
    #ind.close = safemath.reverse(ind.close)
    #trade_id = 1
    i = (len(api.SPYclose) - len(api.close))
    j = len(api.close)-1
    #print(j)
    while safemath.lt1(i, len(api.SPYclose)):
        ind.W_C.prepend(api.SPYclose[i])
        ind.W_O.prepend(api.SPYopen[i])
        ind.price.prepend(api.close[j])
        #print(['calc', i, ind.price[0]])
        ind.callChain()
        closed = False
        #if safemath.eq1(ind.PUT[0], True):
        #    if strategy_interface.strategy.position_size[0] > 0:
        #        strategy_interface.strategy.close('CALL', ind.price[0])
        #        closed = True
        #    qty = (safemath.mul1(safemath.div2([strategy_interface.strategy.initial_capital, api.close[j], 3]), -1) // 1)
        #    staop = safemath.sub1(api.open[j], safemath.sub1(6, mintick))
        #    strategy_interface.strategy.entry(i, 'PUT', qty, 0, stop, ind.price[0])
        #if safemath.eq1(ind.ClosePUT[0], True):
        #    strategy_interface.strategy.close('PUT', ind.price[0])
        #    closed = True
        if safemath.eq1(ind.CALL[0], True):
        #    if strategy_interface.strategy.position_size[0] < 0:
        #        strategy_interface.strategy.close('PUT', ind.price[0])
        #        closed = True
            qty = safemath.div2([strategy_interface.strategy.initial_capital, api.close[j], 3])
            stop = safemath.sub1(api.low[j], safemath.sub1(6, mintick))
            strategy_interface.strategy.entry(i, 'CALL', qty, 0, stop, ind.price[0])
        if safemath.eq1(ind.CloseShortTermCall[0], True):
            if strategy_interface.strategy.position_size[0] > 0:
                strategy_interface.strategy.close('CALL', ind.price[0])
                closed = True
        
        strategy_interface.strategy.calc2(closed)
        #strategy_interface.strategy.calc(ind.price[0])b
        if safemath.gt1(strategy_interface.strategy.position_avg_price[0], 0):
            print([strategy_interface.strategy.trades[len(strategy_interface.strategy.trades)-1].direction, strategy_interface.strategy.position_avg_price[0], ind.price[0] ,safemath.div1(ind.price[0], strategy_interface.strategy.position_avg_price[0])])
            print(['call', ind.CALL[0]])
            print(['close call', ind.CloseShortTermCall[0], safemath.gt1(ind.D00[0], 0), safemath.gt1(ind.price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_avg_price[0], 100), 101))])
            if safemath.gt1(ind.D00[0], 0) and safemath.gt1(ind.price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_avg_price[0], 100), 101)):
                break
            #print(['put', ind.PUT[0]])
            #print(['close put', ind.ClosePUT[0]])
        #if strategy_interface.strategy.position_size[0] > 0:
        #    print(['avg_price', strategy_interface.strategy.position_avg_price[0] ])
        
        
        i += 1
        j -= 1
    if safemath.and1(safemath.gt1(len(ind.hist1), 1), safemath.gt1(i, 50)):
        '''
        print(['longOpened', ind.longOpened[0]])
        print(['longOpened[1]', ind.longOpened[1]])
        print(['shortClosed', ind.shortClosed[0]])
        print(['shortClosed[1]', ind.shortClosed[1]])
        print(['offDays', ind.offDays[0]])
        print(['offDays[1]', ind.offDays[1]])
        print(['onDays', ind.onDays[0]])
        print(['onDays[1]', ind.onDays[1]])
        print(['CumAlpha', ind.CumAlpha[0]])
        print(['CumAlpha[1]', ind.CumAlpha[1]])
        print(['market', ind.market[0]])
        print(['market[1]', ind.market[1]])
        print(['CumVega', ind.CumVega[0]])
        print(['CumVega[1]', ind.CumVega[1]])
        print(['market1', ind.market1[0]])
        print(['market1[1]', ind.market1[1]])
        print(['cc', ind.cc[0]])
        print(['cc[1]', ind.cc[1]])
        '''
        print(['opentrades', strategy_interface.strategy.opentrades[0]])
        print(['closedtrades', strategy_interface.strategy.closedtrades[0]] )
        print(['wintrades', strategy_interface.strategy.wintrades[0]])
        print(['losstrades', strategy_interface.strategy.losstrades[0]] )
        print(['net long pl', strategy_interface.strategy.net_long_pl[0]])
        print(['net short pl', strategy_interface.strategy.net_short_pl[0]])
        
    '''#test data
        #print(strategy_interface.strategy.trades)
        print(['SPY:', ind.W_C[0]])
        print(['D', ind.D[0]])#matches current
        print(['D[1]', ind.D[1]])
        print(['D[2]', ind.D[2]])
        print(['D1', ind.D1[0]])#matches current
        print(['D3', ind.D3[0]])
        print(['D3[1]', ind.D3[1]])
        print(['D3[2]', ind.D3[2]])
        print(['D3[3]', ind.D3[3]])
        print(['D4', ind.D4[0]])
        print(['D01', ind.D01[0]])
        print(['D02', ind.D02[0]])
        
        print(['D00', ind.D00[0]])
        print(['D00[1]', ind.D00[1]])
        print(['D00[2]', ind.D00[2]])
        print(['DMF', ind.DMF[0]])
        print(['DMF[1]', ind.DMF[1]])
        print(['DMF[2]', ind.DMF[2]])
        print(['DMF0', ind.DMF0[0]])
        print(['DMF00', ind.DMF00[0]])
        print(['hist1', ind.hist1[0]])
        print(['hist1[1]', ind.hist1[1]])
        print(['CALL', ind.CALL[0]])
        print(['ind.CALL[1]', ind.CALL[1]])
        print(['ind.CALL[2]', ind.CALL[2]])
        print(['CloseShortTermCall', ind.CloseShortTermCall[0]])
        print(['CloseShortTermCall[1]', ind.CloseShortTermCall[1]])
        print(['CloseShortTermCall[2]', ind.CloseShortTermCall[2]])
        
        print(['v2', ind.v2[0]])
        print(['v2[1]', ind.v2[1]])
        print(['v2[2]', ind.v2[2]])
        print(['rT', ind.rT[0]])
        print(['rT[1]', ind.rT[1]])
        print(['T', ind.T[0]])
        print(['T[1]', ind.T[1]])
        print(['T[2]', ind.T[2]])
        print(['rT2', ind.rT2[0]])
        print(['rT2[1]', ind.rT2[1]])
        print(['nT', ind.nT[0]])
        print(['nT[1]', ind.nT[1]])
        print(['nT[2]', ind.nT[2]])
        print(['T0n', ind.T0n[0]])
        print(['T0n[1]', ind.T0n[1]])
        print(['T0n[2]', ind.T0n[2]])
        print(['ind.closeT0',ind.closeT0[0]])
        print(['ind.closeT0[1]',ind.closeT0[1]])
        print(['ind.closeT0[2]',ind.closeT0[2]])
        print(['Ton', ind.Ton[0]])
        print(['Ton[1]', ind.Ton[1]])
        print(['Ton[2]', ind.Ton[2]])
        print(['PUT', ind.PUT[0]])
        print(['PUT[1]', ind.PUT[1]])
        print(['ClosePUT', ind.ClosePUT[0]])
        print(['ClosePUT[1]', ind.ClosePUT[1]])
    '''

########################################
backtester()
