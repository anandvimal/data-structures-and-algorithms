words = []
all_words = ["apple","banada","blue", "hearth", "AND","SATURN", "SPIN"]

# with open('words.webarchive') as f:
#     all_words = f.readlines()


for item in all_words:
    x = lambda x: x.upper().strip()
    words.append(x(item))

print(words)
#words.remove("HE")
#words.remove("AR")

def isWord(word: str, words=words):

    #words.remove("HE")
    #words.remove("AR")
    if word in words:
        return True
    return False

text = "BLUEHEARTHANDSATURNSPIN"

def splittable(text: str):
    n = len(text)
    if n == 0:
        return True
    for i in range(0,n+1):
        print(f"test: {text[0:i]} : {isWord(text[0:i])}")
        if isWord(text[0:i]):
            #print(text[0:i+1])
            temp = (text[0:i])
            #print(f"new string: {text[i+1:n]}")
            if splittable(text[i:n]):
                print(temp)
                print(True, end= ' ')
                return True
    print(False)
    return False
            
splittable(text=text)
