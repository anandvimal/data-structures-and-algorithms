# python3
import sys

def InverseBWT(bwt):
    # write your code here
    return ""

    # no of occurences of symbol in bwt upto position inclusive of position 
def find_no_of_occurences(search_list, symbol, position):
    count = 1
    item = search_list[position]
    for i in range(position):
        if search_list[i] == item:
            count += 1
    return count
    
def find_position_in_first_column(first_column, symbol, no_of_occurences):
    count = 0
    for i in range(len(first_column)):
        if first_column[i] == symbol:
            count += 1
        if count == no_of_occurences:
            return i

def bwt_to_first_column(bwt, position):
    bwt_symbol = bwt[position]
    no_of_occurencesin_bwt =find_no_of_occurences(search_list=bwt, symbol=bwt[position], position=position)
    result = find_position_in_first_column(first_column, symbol=bwt_symbol, no_of_occurences=no_of_occurencesin_bwt)
    #print(f"result: {result}")
    return result


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #bwt = "smnpbnnaaaaa$a"
    bwt = list(bwt)
    first_column = sorted(bwt)

    position = 0
    answer = ""
    while len(answer) < len(bwt):
        #answer += first_column[position]
        #answer = answer + first_column[position]
        answer = first_column[position] + answer
        position = bwt_to_first_column(bwt, position)

    print(answer)
    #print(inverse(answer))

