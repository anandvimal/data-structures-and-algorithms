line = raw_input()


result = False
for i in line:
    if i.isalnum():
        result =  True
print result


result = False
for i in line:
    if i.isalpha():
        result =  True
print result

result = False
for i in line:
    if i.isdigit():
        result =  True
print result

result = False
for i in line:
    if i.islower():
        result =  True
print result

result = False
for i in line:
    if i.isupper():
        result =  True
print result
