m = {}
M = {}
operators = []
digits = []
n=0


def min_and_max(i,j):
    min_x = 100
    max_x = -100
    #print(f"min and max --> M:{M} m:{m}")
    #print(f"i:{i} j:{j}")
    for k in range(i,j):
        #print(f"i:{i} j:{j} k:{k} M[i,k]:{M[i,k]} operators[k]:{operators[k]}  m[i,k]:{m[i,k]}")
        a = eval(str(M[i,k]) + str(operators[k]) + str(M[k+1,j]))
        b = eval(str(M[i,k]) + str(operators[k]) + str(m[k+1,j]))
        c = eval(str(m[i,k]) + str(operators[k]) + str(M[k+1,j]))
        d = eval(str(m[i,k]) + str(operators[k]) + str(M[k+1,j]))
        min_x = min(a,b,c,d, min_x)
        max_x = max(a,b,c,d, max_x,)
        #print(f"k:{k} a:{a} b:{b} c:{c} d:{d}")
    minimum = min_x
    maximum = max_x
    return (minimum, maximum)
    #pass

def parantheses():
    for i in range(0,n):
        m[i,i] = digits[i]
        M[i,i] = digits[i]
    #print(f"parantheses --> m:{m} M:{M}")
    for s in range(0,n):
        for i in range (0,n-s):
            j = i+s
            if(i != j):
                m[i,j], M[i,j] = min_and_max(i,j)
            elif(i ==j):
                m[i,j], M[i,j] = m[i,i], M[j,j]
    #print(f"final M:{M}")
    #print(f"n-1 = {n-1} n:{n} ")
    return M[0,n-1]


def my_split(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    return res


if __name__ == "__main__":
    exp = str(input())
    delimiters_operators = ['+','-','*','/']
    delimiter_numbers = ['1','2','3','4','5','6','7','8','9','0']
    digits =list( map(int, my_split(exp, delimiters_operators)))
    operators = list( map(str, my_split(exp, delimiter_numbers)))    
    operators = [x for x in operators if x != ''] 
    #print(f"digits: {digits}")
    #print(f"operators: {operators}")
    n = len(digits)    
    result = parantheses()
    print(result)


