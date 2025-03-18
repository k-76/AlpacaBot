
from decimal import Decimal
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
def ABS(a):
    if lt1(a, 0):
        a = mul1(a, -1)
    return a

def DEV(data, period):
    i = 0
    _data = []
    if gt1(len(data), period):
        while lt1(i,period):
            _data.append(ABS(sub1(data[i], SMA(data, period))))
            i += 1
        return (div1(add2(_data),period))
    else:
        return Decimal(0)