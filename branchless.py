import safemath


def structure(func1, array1, func2, array2):
    if safemath.eq1(array2, []):
        return [[func1, array1], func2[0]]
    else:
        return [[func1, array1], [func2, array2]]
def if_else1():
    spec = structure(safemath.gt2, [5,4], safemath.eq2, [0,0])#(a,b = requires (func(array) == True) and (a == False) for else) 
    result = structure(safemath.add2, [3,3], safemath.add2, [3,4])
    if_else =  safemath.branchless(spec, result)
    return if_else.build() #[Decimal('6')]
def if_elif_else1():
    spec = structure(safemath.gt2, [5,4], safemath.gt2, [3,2])
    result = structure(safemath.add2, [3,3], safemath.add2, [3,4])
    if_elif =  safemath.branchless(spec, result)
    else_spec = structure(safemath.eq2, [if_elif.build(), ['exception']], safemath.eq2, [0,0])
    else_result = structure(safemath.add2, [4,4], else_spec[0][1][0], [])#(a = execute else case, b = pass if/elif case) 
    if_elif_else =  safemath.branchless(else_spec, else_result)
    return if_elif_else.build() #[Decimal('6')]
def if_elif_elif1():
    spec = structure(safemath.gt2, [5,4], safemath.gt2, [3,2])
    result = structure(safemath.add2, [3,3], safemath.add2, [3,4])
    if_elif =  safemath.branchless(spec, result)
    r = if_elif.build()
    elif2_spec = structure(safemath.and2, [safemath.eq1(r, ['exception']), safemath.gt2, [1,0]], safemath.eq2, [0,0])
    else_result = structure(safemath.add2, [4,4], r, [])#(a = execute 2nd elif case, b = pass if/elif case) 
    if_elif_elif =  safemath.branchless(elif2_spec, else_result)
    return if_elif_elif.build() #[Decimal('6')] THIS CAN STILL RETURN AN EXCEPTION

print(if_elif_elif1())
macros = [[if_elif_else1, [safemath.Decimal(6)]]]
def jit(func):
    i = 0
    print(macros[i][0])
    print(func)
    while safemath.gt1(len(macros), i):
        if safemath.eq1(macros[i][0], func):
            return macros[i][1]
        i += 1
    return func()