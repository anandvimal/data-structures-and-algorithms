# python3

#read this to improve ?
#https://www.coursera.org/learn/algorithms-on-strings/discussions/forums/caakMsMCEeyb8QqTmnjx6w/threads/q9Qi-8_EEe6sSwrM6xmJAQ

import sys

def InverseBWT(bwt):
    # write your code here
    return ""

def process_to_dict(bwt):
    smart_record = {}
    record = {}
    for position in range(len(bwt)):
        symbol = bwt[position]
        if symbol not in record:
            record[symbol] = 1
        else:
            record[symbol] += 1
        smart_record[ str(symbol) + str(record[symbol])] = position
    #print(f"record: {record}")
    #print(f"smart_record: {smart_record}")
    return smart_record

def proces_lists(bwt):
    smart_list = []
    record = {}
    for position in range(len(bwt)):
        symbol = bwt[position]
        if symbol not in record:
            record[symbol] = 1
        else:
            record[symbol] += 1
        smart_list.append( str(symbol) + str(record[symbol]))
    #print(f"smart_list: {smart_list}")
    return smart_list


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #bwt = "smnpbnnaaaaa$a"
    bwt = list(bwt)
    first_column = sorted(bwt)

    first_column_dict = process_to_dict(first_column)
    bwt_list = proces_lists(bwt)    
    #first_column_list = proces_lists(first_column)
    position = 0
    answer = ""
    #answer = []
    while len(answer) < len(bwt):
        answer = first_column[position] + answer
        symbol_in_bwt= bwt_list[position]
        position = first_column_dict[symbol_in_bwt]
    print(answer)


