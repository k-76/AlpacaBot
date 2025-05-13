import safemath
import strategy_interface
from backtesting.lib import crossover
import api_data as api
import indicators as ind1
#print(close[0], close[1]) the price data is now relative to the present

longOpened = api.indicator()
shortClosed = api.indicator()
offDays = api.indicator()
onDays = api.indicator()
CumAlpha = api.indicator()
market = api.indicator()
CumVega = api.indicator()    
market1 = api.indicator()
cc = api.indicator()


def structure(func1, array1, func2, array2):
    if safemath.eq1(array2, []):
        return [[func1, array1], func2[0]]
    else:
        return [[func1, array1], [func2, array2]]
def if_else1(_spec, _result):
    spec = structure(_spec, safemath.eq2, [0,0])#(a,b = requires (func(array) == True) and (a == False) for else) 
    #result = structure(_result1, _result2)
    if_else =  safemath.branchless(spec, _result)
    return if_else.build()

def Leaf(_branched_build):
    arr = [_branched_build, True, False]
    if safemath.or2(arr):
        arr2 = [arr[0], []]
    else:
        arr2 = [[], arr[0]]
    return arr2#[Decimal('6')]
class calculate():
    def longOpened(globals):
        def A_limits(limit_spec):
            if limit_spec:
                return safemath.Decimal(0)
            else:
                return safemath.add1(longOpened[0], 1) 
        def A_CALC(calc_spec):
            if calc_spec:
                limit_spec = safemath.gt1(longOpened[0], 100)
                return A_limits(limit_spec)
            else:
                return safemath.Decimal(0)
        def B_limits(limit_spec):
            if limit_spec:
                return safemath.Decimal(1)
            else:
                return safemath.Decimal(0)
        def B_CALC(len_spec):
            if len_spec:
                limit_spec = safemath.and1(safemath.gt1(offDays[0], CumAlpha[0]), safemath.gt1(CumAlpha[0], CumAlpha[2]))
                return B_limits(limit_spec)
            else:
                return safemath.Decimal(0)
        def branched_logic():
            len_spec = safemath.gt1(len(longOpened), 1)
            if len_spec:
                calc_spec = safemath.gt1(longOpened[0], 1)
                return A_CALC(calc_spec)
            else:
                len_spec = safemath.gt1(len(CumAlpha), 3)
                return B_CALC(len_spec)
        longOpened.prepend(branched_logic())
        #[calc_spec, len_spec] = if_else1(safemath.gt1(len(longOpened), 1), structure([safemath.gt2, [longOpened[0], 1]], [safemath.gt2, [len(CumAlpha), 1]]))
        #[_spec_1, r1] = Leaf(if_else1(calc_spec, structure([safemath.gt2, [longOpened[0], 100]], [safemath.Decimal(0)])))
        #[_spec_1_1, r2] = Leaf(if_else1(_spec_1, structure([[safemath.Decimal(0)], [safemath.add2, [longOpened, 1]]])))
        #[_spec_2, r3] = Leaf(if_else1(len_spec, structure([safemath.gt2, [offDays[0], CumAlpha[0], CumAlpha[2]]], [safemath.Decimal(0)])))
        #[_spec_2_1, r4] = Leaf(if_else1(_spec_2, structure([[safemath.Decimal(1)], [safemath.Decimal(0)]])))
        
    def shortClosed(globals):
        '''len_spec = safemath.gt1(len(shortClosed), 2)
        if len_spec:
            calc_spec = safemath.or1(safemath.gt1(shortClosed[1], 1), safemath.eq1(shortClosed[1], 1))
            calc_spec2 = safemath.nor1(safemath.gt1(shortClosed[1], 1), safemath.eq1(shortClosed[1], 1))
            if calc_spec:
                calc_spec = safemath.not1(safemath.gt1(shortClosed, 100))
                if calc_spec:  #//and longOpened > 0
                    shortClosed.prepend(safemath.add1(shortClosed[1], 1))   
                else:
                    shortClosed.prepend(safemath.Decimal(0))             
            elif calc_spec2:
                shortClosed.prepend(safemath.Decimal(0))
        else:
            shortClosed.prepend(safemath.Decimal(0))'''
        def A_CALC():
            calc_spec1 = safemath.or1(safemath.gt1(shortClosed[1], 1), safemath.eq1(shortClosed[1], 1))
            calc_spec2 = safemath.nor1(safemath.gt1(shortClosed[1], 1), safemath.eq1(shortClosed[1], 1))
            if calc_spec1:
                return A_LIMITS()
            elif calc_spec2:
                return safemath.Decimal(0)
        def A_LIMITS():
            calc_spec = safemath.not1(safemath.gt1(shortClosed, 100))
            if calc_spec:
                return safemath.add1(shortClosed[1], 1)
            else:
                return safemath.Decimal(0)
        def branched_logic():
            len_spec = safemath.gt1(len(shortClosed), 2)
            if len_spec:
                return A_CALC()
            else:
                return safemath.Decimal(0)
        shortClosed.prepend(branched_logic())
        
    def offDays(globals):
        '''len_spec = safemath.and1(safemath.gt1(len(strategy_interface.strategy.position_size), 1), safemath.gt1(len(offDays), 2))
        if len_spec:
            calc_spec = safemath.eq1(strategy_interface.strategy.position_size[0], 0)
            if calc_spec:
                offDays.prepend(safemath.add1(offDays[1], 1))
            else:
                offDays.prepend(safemath.Decimal(0))
        else:
            offDays.prepend(safemath.Decimal(0))'''
        def A_CALC():
            calc_spec = safemath.eq1(strategy_interface.strategy.position_size[0], 0)
            if calc_spec:
                return safemath.add1(offDays[1], 1)
            else:
                return safemath.Decimal(0)
        def branched_logic():
            len_spec = safemath.and1(safemath.gt1(len(strategy_interface.strategy.position_size), 1), safemath.gt1(len(offDays), 2))
            if len_spec:
                return A_CALC()
            else:
                return safemath.Decimal(0)
        offDays.prepend(branched_logic())
    def onDays(globals):
        '''len_spec = safemath.and1(safemath.gt1(len(strategy_interface.strategy.position_size), 1), safemath.gt1(len(onDays), 2))
        if len_spec:
            calc_spec = safemath.not1(safemath.eq1(strategy_interface.strategy.position_size[0], 0))
            if calc_spec:
                onDays.prepend(safemath.add1(onDays[1], 1))
            else:
                onDays.prepend(safemath.Decimal(0))
        else:
            onDays.prepend(safemath.Decimal(0))'''
        def A_CALC():
            calc_spec = safemath.not1(safemath.eq1(strategy_interface.strategy.position_size[0], 0))
            if calc_spec:
                return safemath.add1(onDays[1], 1)
            else:
                return safemath.Decimal(0)
        def branched_logic():
            len_spec = safemath.and1(safemath.gt1(len(strategy_interface.strategy.position_size), 1), safemath.gt1(len(onDays), 2))
            if len_spec:
                return A_CALC()
            else:
                return safemath.Decimal(0)
        onDays.prepend(branched_logic())
    def CumAlpha(globals):
        mod = safemath.Decimal(0)
        len_spec = safemath.and2([safemath.gt1(len(strategy_interface.strategy.position_size), 1), safemath.gt1(len(offDays), 1), safemath.gt1(len(CumAlpha), 2), safemath.gt1(len(ind1.W_C), 2)])
        if len_spec:
            calc_spec1 = safemath.not1(safemath.eq1(strategy_interface.strategy.position_size[0], 0))
            calc_spec2 = safemath.or1(safemath.eq1(offDays[0], 1), safemath.gt1(offDays[0], 1))
            if calc_spec1:
                mod = safemath.Decimal(CumAlpha[1])
            if calc_spec2:
                mod = safemath.add1(CumAlpha[1], safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(offDays[0])]), 100))
        CumAlpha.prepend(mod)
    def market(globals):
        len_spec = safemath.gt1(len(offDays), 0)
        if len_spec:
            if safemath.eq1(offDays[0], 1):
                market.prepend(safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(offDays[0])]), 100))
            elif safemath.gt1(offDays[0], 1):
                market.prepend(safemath.add1(market[1], (safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(offDays[0])]), 100))))
            else:
                market.prepend(safemath.Decimal(0))
        else:
                market.prepend(safemath.Decimal(0))
    def CumVega(globals):
        len_spec = safemath.gt1(len(CumVega), 1)
        if len_spec:
            calc_spec1 = safemath.eq1(onDays[0], 1)
            calc_spec2 = safemath.gt1(onDays[0], 1)
            if calc_spec1:
                CumVega.prepend(safemath.add1(CumVega[1], (safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(onDays[0])]), 100))))
            elif calc_spec2:
                CumVega.prepend(safemath.add1(CumVega[1], (safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(onDays[0])]), 100))))
        else:
            CumVega.prepend(safemath.Decimal(0))
    def market1(globals):
        if safemath.eq1(onDays[0], 1):
            market1.prepend((safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(onDays[0])]), 100)))
        elif safemath.gt1(onDays[0], 1):
            market1.prepend(safemath.add1(market1[1], (safemath.mul1(safemath.div1(safemath.sub1(ind1.W_C[0], ind1.W_C[1]), ind1.W_C[int(onDays[0])]), 100))))
    def cc(globals):
        def ind_logic(len_spec):
            if len_spec:
                calc_spec = safemath.eq1(ind1.CALL, 1)
                if calc_spec:
                    mod = (safemath.add1(cc[0], 1))
                else:
                    mod = (cc[0])
                calc_spec = safemath.eq1(ind1.CloseShortTermCall[0], True)
                if calc_spec:
                    mod =  safemath.Decimal(0)
                return mod
            else:
                return safemath.Decimal(0)
        mod = safemath.Decimal(0)
        len_spec = safemath.and1(safemath.gt1(len(cc), 2), safemath.gt1(len(ind1.CloseShortTermCall), 1))
        mod = ind_logic(len_spec)
        cc.prepend(mod)

def callChain():
    calc.longOpened()
    calc.shortClosed()
    calc.offDays()
    calc.onDays()
    calc.CumAlpha()
    calc.market()
    calc.CumVega()
    calc.market1()
    calc.cc()

calc = calculate()