inputFile = input("Enter the input file name: ");



def count(elements):
    if elements[-1] == '.':
        elements = elements[0:len(elements) - 1]
    elif elements in dictionary:
        dictionary[elements] += 1
    else:
        dictionary.update({elements: 1})
   

def main():
    f = open(inputFile, 'r')
    lines = f.readlines()
    allWords = {}
    wordList = []
    for eachLine in lines:
        words = eachLine.split()
        wordList += words
    for eachWord in wordList:
        freq = allWords.get(eachWord, None)
        if freq == None:
            allWords[eachWord] = 1
        else:
            allWords[eachWord] = freq + 1
    wordList = list(allWords.keys())
    wordList.sort()
    for word in wordList:
        print(word,allWords[eachWord])
    dictionary = {}
    for elements in wordList:
        count(elements)
    for allKeys in dictionary:
        print (allKeys, dictionary[allKeys]

if __name__ == "__main__": 
    main()
