from patternCount import patternCount

trial = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
kmer = 5

def frequentWordsDictionary(text, k, t):
    frequentPatterns = []
    count = []
    dict_kmer = {}
    dict_kmer_bigger_than_t = {}
    for x in range(0, len(text) - k + 1):
        pattern = text[x: k + x]
        if pattern not in dict_kmer.keys():
            dict_kmer[pattern] = patternCount(text, pattern)
    dict_kmer_bigger_than_t = dict((k, v) for k, v in dict_kmer.items() if v >= t)
    return list(dict_kmer_bigger_than_t)
        
    # maxCount = max(count)
    # for x in range(0, len(text) - k + 1):
    #     if count[x] == maxCount:
    #         frequentPatterns.append(text[x : k + x])
    # frequentPatterns = dict.fromkeys(frequentPatterns)
    # return frequentPatterns