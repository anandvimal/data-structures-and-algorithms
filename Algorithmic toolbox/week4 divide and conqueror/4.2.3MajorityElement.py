from math import floor

if __name__ == "__main__":
    number_of_enteries = int(input()) #ignore
    original_list = list(map(int, input().split()))
    count_reg = {}
    is_majority = False
    majority_qualify = floor(len(original_list)/2)+1 
    
    for item in original_list:
        if count_reg.get(item):
            count_reg[item] = count_reg[item]+1
        else:
            count_reg[item]= 1

    for key in count_reg:
        if count_reg[key] >= majority_qualify:
            is_majority = True
            
    if is_majority:
        print("1")
    else:
        print("0")


    #print(count_reg)
