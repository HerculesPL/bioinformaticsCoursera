from frequent_pattern2 import frequentWordsDictionary

file = open("Vibrio_cholerae.txt", "r")

fileContent = file.readlines()
genoma = fileContent[0]


def clump_finding(k,l,t,genome):
    list_of_most_clump = []
    for i in range(0, len(genome) - l + 1):
        piece_text = genome[i:l+i]
        list_of_most_clump = list_of_most_clump + frequentWordsDictionary(piece_text,k,t)
    return list_of_most_clump

test = clump_finding(9,500,3,genoma)
answer = f= open("cluster_match_answer.txt","w+") 
for i in range (0, len(test)):
    answer.write((str(test[i]) + " "))
answer.close()

test = clump_finding(9,500,3,genoma)