def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    SymbolToNumber = {'A':0,'C':1,'G':2,'T':3}
    n = len(Pattern)
    prefix = Pattern[:n-1]
    symbol = Pattern[n-1]
    print(prefix, symbol)
    return 4 * PatternToNumber(prefix) + SymbolToNumber[symbol]

print(PatternToNumber('CAATCTGCAAAAAGAGCGAG'))