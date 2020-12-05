# file = open("dataset_2_7.txt", "r")

# fileContent = file.readlines()

# Text = fileContent[0]
# Pattern = fileContent[1].replace("\n","")
# file.close()

def patternCount(text, pattern):

    textLength = len(text)
    patternLength = len(pattern)
    counter = 0

    for x in range(0, textLength - patternLength + 1):
        if text[x : x + patternLength ] == pattern:
            counter = counter + 1
    return counter
