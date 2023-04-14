def calculate_min_coins(amount: int, coins ):
    coins.sort(reverse=True)
    #print(coins)
    coins_to_break_even = []
    coin_count = 0
    for biggest_coin in coins:
        while amount >= biggest_coin:
            amount = amount - biggest_coin
            coins_to_break_even.append(biggest_coin)
            coin_count += 1
    #print("this that")
    #print(f" coints used: {coins_to_break_even}")
    #print(f"total coints used: {coin_count}")
    return coin_count

if __name__ == "__main__":
    amount = int(input())
    coins = [5, 1, 10]
    coin_count = calculate_min_coins(amount, coins)
    print(coin_count)


    # alpaca
