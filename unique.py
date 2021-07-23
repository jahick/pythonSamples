inputFile = input("Enter the input file name: ");

def main():
    f = open(inputFile, 'r')
    uniqueWords = []
    lines = f.readlines()
    print(lines)
    allWords = []
    for eachLine in lines:
        words = eachLine.split()
        allWords += words
    print(allWords)
    allWords.sort()
    for eachWord in allWords:
        print(eachWord)  

if __name__ == "__main__": 
    main()
