
file = open("Vibrio_cholerae.txt", "r")

fileContent = file.readlines()
genome = fileContent[0]

def pattern_match(pattern, genome):
    matches = []
    for i in range (0, len(genome) - len(pattern) + 1): 
        if genome[i:i+len(pattern)] == pattern:
            print(i)
            matches.append(i)
    return matches


test = pattern_match('CTTGATCAT', genome)
answer = f= open("pattern_match.txt","w+") 
for i in range (0, len(test)):
    answer.write((str(test[i]) + " "))
answer.close()
