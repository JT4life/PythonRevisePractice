def count_letter(letter, wordlist):
    count = 0
    for word in wordlist:
        if word in letter:
            count+=1
        return count

wordlist = ['a','b','c','a']

a = count_letter('a',wordlist)

print(a)