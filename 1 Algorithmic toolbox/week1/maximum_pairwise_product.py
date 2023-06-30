number_of_inputs = input("")
number_of_inputs = int(number_of_inputs)

list_of_integers = input("")
list_of_integers = list_of_integers.split(' ')

for i in range(0, len(list_of_integers)): 
    list_of_integers[i] = int(list_of_integers[i]) 

list_of_integers.sort()
#print(list_of_integers)


#number_of_inputs given by judge should be same as number of elements in list.
assert(number_of_inputs == len(list_of_integers))

print(list_of_integers[number_of_inputs-1] * list_of_integers[number_of_inputs-2])

