#Enter A and B eg: A B: 
numbers = input("")
try: 
    numbers = numbers.split(' ')
    A = int(numbers[0]) 
    B = int(numbers[1])
    sum = A+B
except ValueError:
    print("This is not valid input for A and B")

#print( "Value of A and B are: ", numbers )
#print("sum of A and B is : ", sum)
print(sum)
