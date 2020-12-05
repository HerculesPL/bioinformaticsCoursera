def numberToPattern(number,k):
    SymbolToNumber = {'A':0,'C':1,'G':2,'T':3}
    test = ''
    if k == 1:
        return  SymbolToNumber[number]
    prefixNumber = number//4
    remainder = number%4
    prefixPattern = numberToPattern(prefixNumber, k - 1)
    test = test + SymbolToNumber[remainder]
    return test

# print(numberToPattern(45,4))
SymbolToNumber = {'A':0,'C':1,'G':2,'T':3}
print(SymbolToNumber['A'])