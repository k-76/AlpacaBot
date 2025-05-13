import safemath
import strategy_interface
from backtesting.lib import crossover
import api_data as api
#print(close[0], close[1]) the price data is now relative to the present

W_C = api.indicator()
W_O = api.indicator()
sma100 = api.indicator()
V = api.indicator()
v2 = api.indicator()
D = api.indicator()
D1 = api.indicator()
D2 = api.indicator()
D0 = api.indicator()
D01 = api.indicator()
D02 = api.indicator()
D4 = api.indicator()
D3 = api.indicator()
D00 = api.indicator()
DMF = api.indicator()
DMF0 = api.indicator()
DMF00 = api.indicator()
hist1 = api.indicator()
CALL = api.indicator()
CloseShortTermCall = api.indicator()
CloseLongTermCall = api.indicator()
vCount = api.indicator()
vCount2 = api.indicator()


rT = api.indicator()
rT2 = api.indicator()
T = api.indicator()
nT = api.indicator()
T0n = api.indicator()
VcountFlow = api.indicator()
closeT0 = api.indicator()
Ton = api.indicator()
TMF = api.indicator()
TMF0 = api.indicator()
odot = api.indicator()
PUT = api.indicator()
ClosePUT = api.indicator()
longOpened = api.indicator()
shortClosed = api.indicator()
offDays = api.indicator()
onDays = api.indicator()
CumAlpha = api.indicator()
market = api.indicator()
CumVega = api.indicator()    
market1 = api.indicator()
cc = api.indicator()

price = api.indicator()


class calculate():
    def sma100(globals):
        if safemath.gt1(len(W_C), 100):
            sma100.prepend(safemath.SMA(W_C, 100))
        else:
            sma100.prepend(safemath.Decimal(0))
    def V(globals):
        V.prepend(safemath.sub1(W_C[0], sma100[0]))
    def v2(globals):
        if safemath.gt1(len(V), 100):
            v2.prepend(safemath.SMA(V, 100))
        else:
            v2.prepend(safemath.Decimal(0))
    def D(globals):
        D.prepend(safemath.sub1(W_C[0], W_O[0]))
    def D1(globals):
        i = 0
        a = []
        while safemath.lt1(i, len(W_C)):
            a.append(safemath.sub1(W_C[i],W_O[i]))
            i += 1
        D1.prepend(safemath.SMA(a, 50))
    def D2(globals):
        i = 0
        a = []
        while i < len(W_C):
            a.append(safemath.sub1(W_C[i],W_O[i]))
            i += 1
        D2.prepend(safemath.SMA(a, 200))
    def D0(globals):
        i = 0
        a = []
        while i < len(W_C):
            a.append(safemath.sub1(W_C[i],W_O[i]))
            i += 1
        D0.prepend(safemath.div1(safemath.SMA(a, 2), 2))
    def D01(globals):
        D01.prepend(safemath.SMA(D0, 25))
    def D02(globals):
        D02.prepend(safemath.SMA(D0, 100))
    def D4(globals):
        if len(D4) > 200:
            if len(D2) > 1:
                a = safemath.EMA(D4, D2, 200)
                D4.prepend(a)
        else:
            D4.prepend(safemath.Decimal(0))
    def D3(globals):
        if len(D1) > 0 and len(D3) > 1:
            a = safemath.EMA(D3, D1, 50)
            if a < 0:
                _a =a *-1
                _b = D4[0] - _a
            D3.prepend(a)
        else:
            D3.prepend(D1[0])
        
    def D00(globals):
        D00.prepend(safemath.add2([D01[0], D02[0], D3[0]]))
    def DMF(globals):
        if safemath.gt1(len(DMF), 0) and safemath.gt1(len(D), 1):
            DMF.prepend(safemath.Decimal(0))
            a = safemath.Decimal(0)
            if D[0] > (D[1] + safemath.Decimal(0.001)):
                a = DMF[1] - (D[1] - D[0])
                DMF[0] = a
            elif (D[0] + safemath.Decimal(0.001)) < D[1]:
                a = DMF[1] + (D[0] - D[1])
                DMF[0] = a
                
        else:
            DMF.prepend(safemath.Decimal(0))
                          
        #print(['DMF', DMF[0]])
    def DMF0(globals):
        if safemath.gt1(len(DMF), 14):
            #print(['DMF0', safemath.SMA(DMF, 14)])
            DMF0.prepend(safemath.SMA(DMF, 14))
        else:
            DMF0.prepend(safemath.Decimal(0))
    def DMF00(globals):
        if safemath.gt1(len(DMF), 120):
            DMF00.prepend(safemath.SMA(DMF, 120))
        else:
            DMF00.prepend((safemath.Decimal(0)))
    def hist1(globals):
        if safemath.gt1(len(DMF0), 0):
            #print([DMF0[0], D00[0]], safemath.sub1(DMF0[0], D00[0]))
            a = safemath.sub1(DMF0[0], D00[0])
            hist1.prepend(a)
            #print(hist1[0])
        else:
            hist1.prepend(safemath.Decimal(0))
    def CALL(globals):
        if safemath.and1(safemath.gt1(len(D00), 0), safemath.gt1(len(hist1), 1)):
            CALL.prepend(safemath.and2([safemath.lt1(D00[0], hist1[0]), safemath.lt1(hist1[1], D00[0]), safemath.lt1(hist1[0], 0)]))
            #if safemath.and1(CALL[0], True):
                #print(['CALL:', price[0]])
        else:
            CALL.prepend(False)
        #print(['Call:', CALL[0], price[0]])
    
    def CloseShortTermCall(globals):
        if safemath.and2([safemath.gt1(len(strategy_interface.strategy.position_avg_price), 0), safemath.gt1(len(D00), 0), safemath.gt1(strategy_interface.strategy.position_size[0], 0)]):# and safemath.gt1(len(close), 1))
            cal_spec = safemath.and1(safemath.gt1(D00[0], 0), safemath.gt1(price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_avg_price[0], 100), 101)))
            CloseShortTermCall.prepend(cal_spec)
        else:
            CloseShortTermCall.prepend(False)
        #print(['CloseCall:',CloseShortTermCall[0], price[0]])
    def CloseLongTermCall(globals):
        if safemath.and2([safemath.gt1(len(V), 1), safemath.gt1(len(strategy_interface.strategy.position_avg_price), 1), safemath.gt1(len(D00), 1)]):
            CloseLongTermCall.prepend(safemath.and2([crossover(safemath.div1(V[0], 10), 0), safemath.gt1(D00[0], 0), safemath.gt1(api.close[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_avg_price[0], 100), 105))]))
        else:
            CloseLongTermCall.prepend(False)
    def vCount(globals):
        if safemath.gt1(v2[0], 0):
            vCount.prepend(safemath.add1(vCount[1], 1))
        else:
            vCount.prepend(safemath.Decimal(1))
    def vCount2(globals):
        if safemath.lt1(v2[0], 0):
            vCount2.prepend(safemath.add1(vCount2[1], 1))
        else:
            vCount2.prepend(safemath.Decimal(1))
    def rT(globals):
        result = safemath.Decimal(0)
        result2 = safemath.Decimal(0)
        i = 1
        if safemath.gt1(len(v2), 100):
            for i in range(100):#while safemath.lt1(i, 100):
                if safemath.gt1(v2[i], 0):
                    result += 1
                i += 1
            rT.prepend((safemath.add1(rT[0],result)))
            i = 1
            for i in range(100):#while safemath.lt1(i, 100):
                if safemath.and1(safemath.lt1(v2[i], 0), safemath.gt1(rT[i], 0)):
                    result2 += safemath.div1(rT[0], 100000)
                i += 1
            T.prepend((safemath.add1(T[0],result2)))
            result3 = safemath.Decimal(0)
            result4 = safemath.Decimal(0)
            i = 1
            for i in range(100):#while safemath.lt1(i, 100):
                if safemath.lt1(v2[i], 0):
                    result3 += 1
                i += 1
            rT2.prepend((safemath.add1(rT2[0],result3)))
            i = 1
            for i in range(100):#while safemath.lt1(i, 100):
                if safemath.and1(safemath.gt1(v2[i], 0), safemath.gt1(rT2[i], 0)):
                    result4 += safemath.div1(rT2[0], 100000)
                i += 1
            nT.prepend((safemath.add1(nT[0],result4)))

            #print(rT2[0])
            #print(nT[0])
        else:
            rT.prepend(safemath.Decimal(0)-9900)
            T.prepend(safemath.add1(safemath.Decimal(0), 66.9827))
            rT2.prepend(safemath.Decimal(0))
            nT.prepend(safemath.sub1(safemath.Decimal(0), 44.74115))
    def rT2(globals):
        a = safemath.Decimal(0)#rT2.prepend(qtyHigherCloses(100))
    def T(globals):
        a = safemath.Decimal(0)
    def nT(globals):
        a = safemath.Decimal(0)
        #nT.prepend(qtyLowerCloses(100))
    def T0n(globals):
        if safemath.and1(safemath.gt1(len(nT), 0), safemath.gt1(len(T), 0)):
            T0n.prepend(safemath.div1(nT[0], T[0]))
        else:
            T0n.prepend(safemath.Decimal(0))
    def VcountFlow(globals):
        VcountFlow.prepend(safemath.add1(safemath.div1(vCount[0], vCount2[0]), 1))
    def closeT0(globals):
        i = 0
        a = safemath.Decimal(0)
        if safemath.gt1(len(T0n), 100):
            while safemath.lt1(i, 100):
                a += safemath.div1(api.close[i], T0n[i])
                i += 1
            closeT0.prepend(safemath.div1(a, 100))#this is a problem for sma
        else:
            closeT0.prepend(safemath.Decimal(0))
    def Ton(globals):
        len_spec = safemath.and1(safemath.gt1(len(closeT0), 1), safemath.gt1(len(sma100), 1))
        if len_spec:
            if safemath.eq1(sma100[0], 0):
                Ton.prepend(safemath.Decimal(0))
            else:
                Ton.prepend(safemath.div1(closeT0[0], sma100[0]))
        else:
            Ton.prepend(safemath.Decimal(0))
    def TMF(globals):
        len_spec = safemath.and1(safemath.gt1(len(Ton), 1), safemath.gt1(len(TMF), 1))
        if len_spec:
            if safemath.gt1(Ton[0], Ton[1]):
                TMF.prepend(safemath.sub1(TMF[1], safemath.mul1(1, safemath.sub1(Ton[1], Ton[0]))))
            elif safemath.and1(safemath.lt1(Ton[0], Ton[1]), safemath.lt1(Ton[0], 1)):#safemath.and1(lt3(Ton[0], [Ton[1], 1]))
                TMF.prepend(safemath.add1(TMF[1], safemath.mul1(1, safemath.sub1(Ton[0], Ton[1]))))
            else:
                TMF.prepend(safemath.Decimal(0))
        else:
            TMF.prepend(safemath.Decimal(0))
    def TMF0(globals):
        TMF0.prepend(safemath.SMA(TMF, 14))
    def odot(globals):
        #odot = ((r > r[1] and T > T[1]))
        len_spec = safemath.gt1(len(rT), 1)
        if len_spec:
            odot.prepend(safemath.and1(safemath.gt1(rT[0], rT[1]), safemath.gt1(T[0], T[1])))
    def PUT(globals):
        len_spec = safemath.gt1(len(odot), 39)
        if len_spec:
            a = safemath.and2([safemath.gt1(DMF00[0], hist1[0]), safemath.gt1(hist1[0], 0), safemath.gt1(D00[0], 0)])
            if safemath.gt1(strategy_interface.strategy.position_size[0], 0):
                b = safemath.and1((odot[40]), safemath.or1(safemath.gt1(price[0], safemath.mul1(safemath.div1(strategy_interface.strategy.position_avg_price[0],100),105)), safemath.not1(odot[10])))
            else:
                b = safemath.not1(odot[0])
            #print([a, b])
            PUT.prepend(safemath.and1(a,b))
        else:
            PUT.prepend(False)
        #PUT = (DMF00 > hist1 and hist1 > 0 and D00 > 0) and ( (strategy.position_size > 0? ((odot[40]) and close > ((strategy.position_avg_price/100)*105)) or not(odot[10]):not(odot) ))// and (V/10) > 0 

        
    def ClosePUT(globals):
        len_spec = safemath.gt1(len(V), 1)
        if len_spec:
            a = safemath.and1(safemath.lt1(safemath.div1(V[0], 10), hist1[0]), safemath.lt1(hist1[0], 0))
            b = safemath.gt1(DMF0[0], safemath.div1(V[0], 10))
            c = safemath.or1(safemath.eq1(DMF0[1], safemath.div1(V[1], 10)), safemath.lt1(DMF0[1], safemath.div1(V[1], 10)))# crossover
            ClosePUT.prepend(safemath.and2([a, b, c]))
        #if safemath.and1(ClosePUT[0], True):
            #print(['ClosePUT:',  price[0]])
            #print(['ClosePUT:',safemath.lt1(safemath.div1(V[0], 10), hist1[0]), safemath.lt1(hist1[0], 0), safemath.gt1(DMF0[0], safemath.div1(V[0], 10)), safemath.or1(safemath.eq1(DMF0[1], safemath.div1(V[1], 10)), safemath.lt1(DMF0[1], safemath.div1(V[1], 10)))])

def callChain():
    W_C = api.SPYclose
    W_O = api.SPYopen
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
    calc.odot()
    calc.PUT()
    calc.ClosePUT()

calc = calculate()