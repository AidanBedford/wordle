
# A way to rank the words, each word is given a score based on how many other remaining words it can give info about
def rankWords(words):
    scores = {word: 0 for word in words}
    returnList = []
    for word in words:
        for compare in words:
            for letter in word:
                if letter in compare:
                    scores[word]+=1
                    break
    scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))         
    for word in scores:
        returnList.append(word)
    return returnList


#Gets the total list of words from words.txt
def getWords():
    file = open("words.txt", "r")
    words = []
    for word in file:
        word = word[0:5]
        words.append(word)
    file.close()
    return words


# Given the return from wordle, filter out words that are impossible, then re-score the words
# Return this list of rescored words.
def filterWords(words, notIn, inWord, rightPlace, guess):
    toBeRemoved = []
    done = False
    for word in words:
        done = False
        for letter in notIn:
            if letter in word:
                toBeRemoved.append(word)
                done = True
                break
        if not done:
            for letter in inWord:
                if letter not in word:
                    toBeRemoved.append(word)
                    done = True
                    break
        if not done:
            for letter in inWord:
                for i in range(5):
                    if letter == guess[i]:
                        if letter == word[i]:
                            toBeRemoved.append(word)
                            done = True
                            break
                if done:
                    break
        if not done and len(rightPlace)>0:
            for i in range(5):
                if rightPlace[i] != "*" and word[i] != rightPlace[i]:
                    toBeRemoved.append(word)
                    break
    for word in toBeRemoved:
        words.remove(word)
    words = rankWords(words)
    return words





words = getWords()
words = rankWords(words)
for i in range(10):
    print(words[i])
while True:
    guess = words[0]
    print("Please use " + words[0] + " as your guess")
    correct = input("If it was correct please type yes ")
    if correct == "yes":
        break

    notIn = input("Please enter all letters not in word: ")
    inWord = input("Please enter all letters in the word, but not in the right place: ")
    rightPlace = input("Please enter a 5 character string to represent the word, only including the letters that are in the right place and '*' for any other character: ")
    words = filterWords(words, notIn, inWord, rightPlace, guess)





