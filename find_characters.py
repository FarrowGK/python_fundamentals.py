

def findcharacters(letter, wordlist):
    container = []
    for word in wordlist:
        for l in word:
            if l == letter:
                container.append(word)
                break               
    print container
letter = "o"
wordlist = ['hello','world','my','name','is','Anna', 'cool']

findcharacters(letter, wordlist)




        
