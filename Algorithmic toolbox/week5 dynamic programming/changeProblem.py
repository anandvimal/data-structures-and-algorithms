

min_num_coins ={}
def DPChange(money):
    money = int(money)
    coins = [1,3,4]
    min_num_coins['0']=0
    for m in range(1,money+1):
        min_num_coins[str(m)]=1000000 #infinite value of coins
        #print(f"money: {m}")
        for coin in coins:
            if m>= coin:
                num_coins = min_num_coins[str(m-coin)]+1
                if num_coins < min_num_coins[str(m)]:
                    min_num_coins[str(m)] = num_coins
    return min_num_coins[str(money)]
    


#print(DPChange(money=6, coins=[1,2,3,5]))

if __name__ == "__main__":
    money = int(input()) #ignore
    #money = 10
    num_of_coins_used =DPChange(money=money)
    print(num_of_coins_used)


