#find a two digit number that becomes 57 times smaller when first digit is removed.

test = 10
found = False

while test<10000000 and found == False:
    test_string=str(test)
    test_string=test_string[1:]
    print(f"test_string:{test_string} test:{test}")
    result = int(test_string)
    if test/57 == result:
        print("number is: "+str(test)+"after removing first digit it becomes 1/57 : "+ str(result))
        found = True #this will just break the loop
    #print(test)
    #print(test_string)

    #print("\n\n")
    test+=1




