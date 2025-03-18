import safemath
#import strategy_interface
import indicators as ind
import api_data as api

################ math library #########################


def backtester():

    mintick = safemath.Decimal(0.01)
    i = len(api.SPYclose) - 200 
    while safemath.lt1(i, len(api.SPYclose)):
        ind.W_C.prepend(api.SPYclose[i])
        ind.W_O.prepend(api.SPYopen[i])
        ind.W_L.prepend(api.SPYlow[i])
        ind.W_H.prepend(api.SPYhigh[i])
        
        print(['calc', i, ind.W_C[0]])
        ind.callChain()
        print(['CCI', ind.CCI[0]])

        closed = False
        i += 1
        

########################################
backtester()
