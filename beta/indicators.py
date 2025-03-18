import safemath
#import strategy_interface
from backtesting.lib import crossover
import api_data as api

W_O = api.indicator()
W_H = api.indicator()
W_L = api.indicator()
W_C = api.indicator()
HLC3 = api.indicator()
sma20_HLC3 = api.indicator()
sma100 = api.indicator()
CCI = api.indicator()

price = api.indicator()


class calculate():
    def sma100(globals):
        if safemath.gt1(len(W_C), 100):
            sma100.prepend(safemath.SMA(W_C, 100))
        else:
            sma100.prepend(safemath.Decimal(0))
    def HLC3(globals):
        if safemath.and2([safemath.gt1(len(W_H), 0), safemath.gt1(len(W_L), 0), safemath.gt1(len(W_C), 0)]):
            HLC3.prepend(safemath.div1(safemath.add2([W_H[0], W_L[0], W_C[0]]), 3))
        else:
            HLC3.prepend(safemath.Decimal(0))
    def sma20_HLC3(globals):
        if safemath.gt1(len(HLC3), 20):
            sma20_HLC3.prepend(safemath.SMA(HLC3, 20))
        else:
            sma100.prepend(safemath.Decimal(0))

    def CCI(globals):
        src = HLC3
        length = 100
        MA = safemath.SMA(HLC3, length)
        MD = safemath.DEV(HLC3, length)
        if safemath.and1(safemath.gt1(len(W_C), length), safemath.gt1(safemath.mul1(0.015, safemath.DEV(HLC3, length)), 0)):
            CCI.prepend(safemath.sub1(safemath.div1(safemath.sub1(src[0], MA), safemath.mul1(0.015, MD)), 6.45))
        else:
            CCI.prepend(safemath.Decimal(0))

def callChain():
    W_H = api.SPYhigh
    W_L = api.SPYlow
    W_C = api.SPYclose
    calc.HLC3()
    calc.sma20_HLC3()
    calc.CCI()

calc = calculate()