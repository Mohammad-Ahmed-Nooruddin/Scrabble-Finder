file = open('allwords.txt', 'r')
allWords = file.read()
allWordsList = allWords.split('\n')

def convertToList(x):
    returnList = []
    for y in "abcdefghijklmnopqrstuvwxyz":
        returnList.append(len(x.split(y)) - 1)
    return returnList

def compareList(x,y):
    iteration = 0
    for num in x:
        if(x[iteration] > y[iteration]):
            return False
        iteration = iteration + 1
    return True

def possibleWords(x):
    returnList = []
    convertedX = convertToList(x)
    for word in allWordsList:
        if(len(word) > 2):
            convertedWord = convertToList(word)
            if(compareList(convertedWord, convertedX) == True):
                returnList.append(word)
    return returnList

combination = input("Allowed letters: ")
print(possibleWords(combination))
input()
