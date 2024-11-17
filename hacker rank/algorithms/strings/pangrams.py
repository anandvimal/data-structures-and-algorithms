data = raw_input().lower()

alpha = "qwertyuioplkjhgfdsazxcvbnm"
p = True

for i in alpha:
    if data.find(i) == -1 :
        p = False

if p:
    print "pangram"
else:
    print "not pangram"

    
