def binaryToDecimal(binary:str) -> int:
    counter = 0
    sum = 0 
    for i in range(len(binary)-1, -1, -1):
        #print(f" binary digit = {binary[i]} counter:{counter}")
        sum = sum + int(binary[i]) * 2**counter
        counter+=1
    print(f"binary = {binary} decimal = {sum}")
    decimal = sum
    return decimal

def decimalToBinary(decimal:str) -> str:
    quotient = int(decimal)
    binary = ""

    if quotient ==0:
        binary = "0"

    while quotient !=0:
        quotient, remainder = divmod(quotient, 2)
        binary = str(remainder) + binary 
    #print(f"decimal = {decimal} and  binary={binary}")
    return binary
    

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = binaryToDecimal(a)
        decimal_b = binaryToDecimal(b)
        decimal_sum = decimal_a + decimal_b
        binary_sum = decimalToBinary(decimal_sum)
        print(f"binary sum = {binary_sum}")
        return binary_sum
        


# binaryToDecimal("1")
# binaryToDecimal("10")
# binaryToDecimal("10100")

# decimalToBinary("20")

#pumpkin really not looking!

test = Solution()
test.addBinary("1010", "1011")
test.addBinary("0", "0")