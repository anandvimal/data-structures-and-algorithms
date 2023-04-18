def is_better(number, maxNumber):
    if int(str(number)+str(maxNumber)) >= int(str(maxNumber)+str(number)):
        #number is bigger:
        return number
    else:
        return maxNumber



def find_biggest_number_prefix(list_of_numbers : list):
    max_prefix = 0
    for i in list_of_numbers:
        #print(f"compare max_prefix:{max_prefix} index:{i}")
        max_prefix = is_better(i, max_prefix)    
    #print(f"max_prefix:{max_prefix}")
    index = list_of_numbers.index(max_prefix)
    return max_prefix, index


if __name__ == "__main__":
    number = int(input())
    salary = ""
    all_numbers = list(map(str, input().split()) )
    #print(all_numbers)
    while ( len(all_numbers) > 0 ):
        max_salary_prefix, max_salary_prefix_index = find_biggest_number_prefix(list_of_numbers=all_numbers) 
        salary = str(salary) + str(max_salary_prefix)
        all_numbers.pop(max_salary_prefix_index)
        #print(f"salary: {salary}")
    #print(f"final salary: {salary}")
    print(salary)

    
    
    

