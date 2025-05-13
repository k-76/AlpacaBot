
def repaymentInYears(amount, rate, years):
    i = 0
    while years[i] < amount:
        a = ((amount * (rate))-amount)*i
        years.append(a)
        i += 1
    return (i-1)
equity = 500000
margin = 0
firstLoan = repaymentInYears(equity, 1.05, [0])
margin += equity
ourDebt = repaymentInYears(500000, 1.04, [0])
equity += margin#cash
secondLoan = repaymentInYears(margin, 1.05, [0])
print(equity/margin)