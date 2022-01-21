from time import sleep

wordFile = open("words.txt", "r")
words = []
for word in wordFile:
    word = word[0:5]
    words.append(word)

notIn = []
inWord = []
rightPlace = []
toBeRemoved = []
guesses = 0
print("Enter " + words[0] + " as your first guess")
guess = words[0]
guesses += 1
while guesses < 6:
    toBeRemoved.clear()
    correct = input(
        "If the guess was correct type correct, type anything else if wrong: ")
    if correct == "correct":
        print("Congrats you got it on your " + str(guesses) + " guess")
        guesses = True
        break
    notIn = input(
        "Please enter all letters not in the word: ")
    inWord = input(
        "Please enter all letters that were in the word, but not in the right place: ")
    rightPlace = input(
        "Please enter the word but only including letters that were in the right place, ie a***n: ")
    done = False
    j = 0
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
        if not done:
            for i in range(5):
                if rightPlace[i] != "*" and word[i] != rightPlace[i]:
                    toBeRemoved.append(word)
                    break
    for word in toBeRemoved:
        words.remove(word)
    print("There are " + str(len(words)) + " words remaining")
    print("Please enter " + words[0] + " as your next guess")
    guess = words[0]

if not guesses:
    print("Unfortunately we were unable to guess the word:(")
