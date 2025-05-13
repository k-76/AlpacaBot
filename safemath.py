
from decimal import Decimal
from indicators import v2
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


class branchless():
    def __init__(self, specs, returns):
        self.if_branch_specs = []
        self.else_branch_specs = []
        self.if_branch_returns = []
        self.else_branch_returns = []
        i=0
        while  gt1(len(specs),i):
            self.if_branch_specs.append(specs[i])
            self.if_branch_returns.append(returns[i])
            i+=2
            self.else_branch_specs.append(specs[i-1])
            self.else_branch_returns.append(returns[i-1])
    def build(self):
        def _else(if_result, spec, returns):
            if  eq1(if_result[0], 'exception'):
                try:
                    return _if(spec, returns)
                except:
                    try:
                        func2 = returns[0][0]
                        array2 = returns[0][1]
                        return [func2(array2)]
                    except:
                        return [returns[0]]
            else:
                return [if_result[0]]
        def _if(spec, returns):
            
            func = spec[0][0]
            array = spec[0][1]
            if func(array):
                try:
                    func2 = returns[0][0]
                    array2 = returns[0][1]
                    #print(['case', 1, 1])
                    return [func2(array2)]
                except:
                    #print(['case', 1, 2])
                    return [returns[0]]
            else:
                #print(['case', 2, 1])
                return ['exception']
        return _else(_if(self.if_branch_specs, self.if_branch_returns), self.else_branch_specs, self.else_branch_returns)



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
