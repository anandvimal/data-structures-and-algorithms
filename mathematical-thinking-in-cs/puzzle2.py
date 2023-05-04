#find a two digit number that becomes 7 times smaller when first digit is removed.

test = 10
found = False

while test<10000:
    test_string=str(test)
    test_string=test_string[1]
    result = int(test_string)
    if test/7 == result:
        print("number is: "+str(test)+"after removing first digit it becomes 1/7 : "+ str(result))
    #print(test)
    #print(test_string)

    #print("\n\n")
    test+=1




