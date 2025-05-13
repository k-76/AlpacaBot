import safemath
import indicators as ind
import strategy_interface
import ind2
import api_data as api

################ math library #########################


def backtester():

    def OCA_ENTRY_PUT():
        def close_longs(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('CALLb', ind.price[0])
                strategy_interface.strategy.close('CALL', ind.price[0])
                strategy_interface.strategy.close('CALLa', ind.price[0])
                return True
            else:
                return False
        def open_shorts(calc_spec):
            if calc_spec:
                qty = (safemath.mul1(safemath.div2([strategy_interface.strategy.initial_capital, ind.price[0], 3]), -1) // 1)
                stop = safemath.sub1(api.open[j], safemath.mul1(6, mintick))
                strategy_interface.strategy.entry(i, 'PUT', qty, 0, stop, ind.price[0])
        def trade_logic(len_spec, direction_spec):
            a = False
            #if safemath.and1(len_spec, direction_spec):
            if len_spec:
                calc_spec = safemath.eq1(ind.PUT[0], True)
                a = close_longs(calc_spec, direction_spec)
                return [a, open_shorts(calc_spec)]
            else:
                return [False, 0]
        len_spec = safemath.gt1(len(ind.PUT), 0)
        direction_spec = safemath.gt1(strategy_interface.strategy.position_size[0], 0)
        [closed, opened] = trade_logic(len_spec, direction_spec)
        return closed
    def OCA_ENTRY_CALL():
        def close_shorts(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('PUT', ind.price[0])
                return True
            else:
                return False 
        def open_longs(calc_spec):
            if calc_spec:
                #print(ind2.cc[0])
                qty = safemath.div2([strategy_interface.strategy.initial_capital, ind.price[0], 3])
                stop = safemath.sub1(api.low[j], safemath.sub1(6, mintick))
                strategy_interface.strategy.entry(i, 'CALL', qty, 0, stop, ind.price[0])
        def trade_logic(len_spec, direction_spec):
            if len_spec:
                calc_spec = safemath.eq1(ind.CALL[0], True)
                [a,b] =[close_shorts(calc_spec, direction_spec), open_longs(calc_spec)]
                #if a == True:
                #    print(a)
                return [a,b]
            else:
                return [False, 0]
        len_spec = safemath.gt1(len(ind.CALL), 0)
        direction_spec = safemath.lt1(strategy_interface.strategy.position_size[0], 0)
        [closed, opened] = trade_logic(len_spec, direction_spec)
        return closed
    def OCA_EXIT_CALL():
        def close_longs(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('CALL', ind.price[0])
                #strategy_interface.strategy.close('CALLa', ind.price[0])
                return True
            else:
                return False
        len_spec = safemath.gt1(len(ind.CloseShortTermCall), 0)
        direction_spec = safemath.gt1(strategy_interface.strategy.position_size[0], 0)
        if len_spec:
            calc_spec = safemath.eq1(ind.CloseShortTermCall[0], True)
            return close_longs(calc_spec, direction_spec)
        else:
            return False
    def OCA_EXIT_PUT():
        def close_shorts(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('PUT', ind.price[0])
                return True
            else:
                return False 
        len_spec = safemath.gt1(len(ind.ClosePUT), 0)
        direction_spec = safemath.lt1(strategy_interface.strategy.position_size[0], 0)
        if len_spec:
            calc_spec = safemath.eq1(ind.ClosePUT[0], True)
            return close_shorts(calc_spec, direction_spec)
        else:
            return False
    def OCA_ENTRY_CALLa():
        
        def close_shorts(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('PUT', ind.price[0])
                return True
            else:
                return False 
        def open_longs(calc_spec):
            if calc_spec:
                qty = safemath.div2([strategy_interface.strategy.initial_capital, ind.price[0], 3])
                stop = safemath.sub1(api.low[j], safemath.mul1(6, mintick))
                strategy_interface.strategy.entry(i, 'CALLa', qty, 0, stop, ind.price[0])
        def trade_logic(len_spec, direction_spec):
            if len_spec:
                calc_spec = safemath.and1(safemath.gt1(ind2.offDays[0], ind2.CumAlpha[0]), safemath.gt1(ind2.CumAlpha[0], ind2.CumAlpha[2]))
                [a,b] =[close_shorts(calc_spec, direction_spec), open_longs(calc_spec)]
                #if a == True:
                #    print(a)
                return [a,b]
            else: 
                return [False, 0]
        len_spec = safemath.and1(safemath.gt1(len(ind2.CumAlpha), 2), safemath.gt1(len(ind2.cc), 1))
        direction_spec = safemath.lt1(strategy_interface.strategy.position_size[0], 0)
        [closed, opened] = trade_logic(len_spec, direction_spec)
        return closed
    def OCA_EXIT_CALLa():
        def close_longs(len_spec, direction_spec):
            if safemath.and1(len_spec, direction_spec):
                calc_spec = safemath.or1(safemath.gt1(ind.price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_size[0],100),120)), safemath.and1(safemath.eq1(ind2.cc[0], 0), safemath.gt1(ind2.cc[1], 0)))
                if calc_spec:
                    strategy_interface.strategy.close('CALLa', ind.price[0])
                    return True
                else:
                    return False
        direction_spec = safemath.gt1(strategy_interface.strategy.position_size[0], 0)
        len_spec = safemath.and1(safemath.gt1(len(ind2.CumAlpha), 3), safemath.gt1(len(ind2.cc), 2))
        return close_longs(len_spec, direction_spec)
    def OCA_ENTRY_CALLb():
        def close_shorts(calc_spec, direction_spec):
            if safemath.and1(calc_spec, direction_spec):
                strategy_interface.strategy.close('PUT', ind.price[0])
                return True
            else:
                return False 
        def open_longs(calc_spec):
            if calc_spec:
                qty = safemath.div2([strategy_interface.strategy.initial_capital, ind.price[0], 3])
                stop = safemath.sub1(api.low[j], safemath.mul1(6, mintick))
                strategy_interface.strategy.entry(i, 'CALLb', qty, 0, stop, ind.price[0])
        def trade_logic(len_spec, direction_spec):
            if len_spec:
                calc_spec = safemath.lt1(safemath.div1(ind.V[0], 10), -8)
                [a,b] =[close_shorts(calc_spec, direction_spec), open_longs(calc_spec)]
                #if a == True:
                #    print(a)
                return [a,b]
            else: 
                return [False, 0]
        len_spec = safemath.and1(safemath.gt1(len(ind2.CumAlpha), 2), safemath.gt1(len(ind2.cc), 1))
        direction_spec = safemath.lt1(strategy_interface.strategy.position_size[0], 0)
        [closed, opened] = trade_logic(len_spec, direction_spec)
        return closed
    def OCA_EXIT_CALLb():
        def close_longs(len_spec, direction_spec):
            if safemath.and1(len_spec, direction_spec):
                calc_spec = safemath.gt1(ind.price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_size[0],100),120))
                if calc_spec:
                    strategy_interface.strategy.close('CALLb', ind.price[0])
                    return True
                else:
                    return False
        direction_spec = safemath.gt1(strategy_interface.strategy.position_size[0], 0)
        len_spec = safemath.and1(safemath.gt1(len(ind2.CumAlpha), 3), safemath.gt1(len(ind2.cc), 2))
        return close_longs(len_spec, direction_spec)
        
    mintick = safemath.Decimal(0.01)
    i = (len(api.SPYclose) - len(api.close))
    j = len(api.close)-1
    while safemath.lt1(i, len(api.SPYclose)):
        ind.W_C.prepend(api.SPYclose[i])
        ind.W_O.prepend(api.SPYopen[i])
        ind.price.prepend(api.close[j])
        #print(['calc', i, ind.price[0]])
        ind.callChain()
        closed = safemath.or2([OCA_ENTRY_CALL(), OCA_ENTRY_PUT(), OCA_EXIT_PUT(),  OCA_EXIT_CALL(), OCA_ENTRY_CALLb(), OCA_ENTRY_CALLa()])
        ind2.callChain()
        #closed = safemath.or2([closed, OCA_ENTRY_CALLa(), OCA_ENTRY_CALLb()])
        strategy_interface.strategy.calc2(closed)
        
        #print(strategy_interface.strategy.gross_short_profits[0])
        i += 1
        j -= 1
    if safemath.and1(safemath.gt1(len(ind.hist1), 1), safemath.gt1(i, 50)):
        '''
        print(['odot', ind.odot[0]])
        print(['odot[1]', ind.odot[1]])
        print(['longOpened', ind2.longOpened[0]])
        print(['longOpened[1]', ind2.longOpened[1]])
        print(['shortClosed', ind2.shortClosed[0]])
        print(['shortClosed[1]', ind2.shortClosed[1]])
        print(['offDays', ind2.offDays[0]])
        print(['offDays[1]', ind2.offDays[1]])
        print(['onDays', ind2.onDays[0]])
        print(['onDays[1]', ind2.onDays[1]])
        print(['CumAlpha', ind2.CumAlpha[0]])
        print(['CumAlpha[1]', ind2.CumAlpha[1]])
        print(['market', ind2.market[0]])
        print(['market[1]', ind2.market[1]])
        print(['CumVega', ind2.CumVega[0]])
        print(['CumVega[1]', ind2.CumVega[1]])
        print(['market1', ind2.market1[0]])
        print(['market1[1]', ind2.market1[1]])
        print(['cc', ind2.cc[0]])
        print(['cc[1]', ind2.cc[1]])
        '''
        print(['pyramiding', strategy_interface.strategy.pyramiding])
        print(['opentrades', strategy_interface.strategy.opentrades[0]])
        print(['closedtrades', strategy_interface.strategy.closedtrades[0]] )
        print(['wintrades', strategy_interface.strategy.wintrades[0]])
        print(['losstrades', strategy_interface.strategy.losstrades[0]] )
        print(['net long pl', strategy_interface.strategy.net_long_pl[0]])
        print(['gross_long_losses', strategy_interface.strategy.gross_long_losses[0]])
        print(['gross_long_profits', strategy_interface.strategy.gross_long_profits[0]])
        print(['net short pl', strategy_interface.strategy.net_short_pl[0]])
        print(['gross_short_losses', strategy_interface.strategy.gross_short_losses[0]])
        print(['gross_short_profits', strategy_interface.strategy.gross_short_profits[0]])
        '''
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


import os
import shutil
    
def remove_pycache(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
    
remove_pycache(".") # Removes from current directory