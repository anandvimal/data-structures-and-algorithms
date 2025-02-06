# python3
import sys

def cyclic_rotations(text):
    return [ text[len(text)-i:] + text[:len(text)-i]   for i in range(len(text))]

def sort_cyclic_rotations(text):
    return sorted(cyclic_rotations(text))   

def BWT(text):
    bwt = ""
    list = sort_cyclic_rotations(text)
    for item in list:
        last_char = item[len(item)-1]
        bwt += last_char
    return bwt

# if __name__ == '__main__':
#     text = sys.stdin.readline().strip()
#     print(BWT(text))

text = sys.stdin.readline().strip()
print(BWT(text))
