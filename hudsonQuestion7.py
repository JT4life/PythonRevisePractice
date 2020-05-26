def count_letter(letter, wordList):
    count = 0
    for word in wordList:
        if letter in word:
            count += 1
    print("number of times letter appeared ",count, "letter ", letter)

wordList = ["hi", "hi", "you"]

count_letter("o", wordList)