#start with 0 cast and 0 stock 
# buy or hold unlimited times 1 each day

#daily_price = [19,2, 30, 15, 33]
daily_price = [5,1,7]

def max_profit(daily_price):
    #initial state:start from a reference cash amount
    # it can be any value
    # we use 0 and allow our cash to go below 0 if we need to buy a share.
    cash_not_owning_share = 0 # amount we start with 0 share 0 money in hand.
    # high penalty for owning a stock initially. 
    # ensure this option is never used. 
    cash_owning_share = -float('inf') # starting with a stock not allowed.
    for price in daily_price:
        
        # Transitions to the current day, owning the stock  
        # Buy or hold
        print(" Buy or hold")
        strategy_buy = cash_not_owning_share - price
        strategy_hold = cash_owning_share
        print(f"strategy_buy = {strategy_buy}")
        print(f"strategy_hold = {strategy_hold}")
        print(" ")

        #transition to the current day, not owning the stock 
        # sell or hold
        print("Sell or hold")
        strategy_sell = cash_owning_share + price
        strategy_avoid = cash_not_owning_share
        print(f"strategy_sell = {strategy_sell}")
        print(f"strategy_avoid = {strategy_avoid}")
        print(" ")
        
        #compute the new states
        print("Compute the new states : what we end up choosing!")
        cash_owning_share = max(strategy_buy, strategy_hold)
        cash_not_owning_share = max(strategy_sell, strategy_avoid)
        print(f"cash_owning_share = {cash_owning_share}")
        print(f"cash_not_owning_share = {cash_not_owning_share}")
        print("--------------------")

    return cash_not_owning_share

print("*************")
print(max_profit(daily_price))


daily_price = [5,1,7]

def max_profit2(daily_price):
    #initial state:start from a reference cash amount
    # it can be any value
    # we use 0 and allow our cash to go below 0 if we need to buy a share.
    cash_not_owning_share = 0 # amount we start with 0 share 0 money in hand.
    # high penalty for owning a stock initially. 
    # ensure this option is never used. 
    cash_owning_share = -float('inf') # starting with a stock not allowed.

    for price in daily_price:
        
        # buy or hold 
        buy = cash_not_owning_share - price
        hold = cash_owning_share
        
        buy_or_hold = max(buy, hold)
        
        #sell or avoid 
        sell = cash_owning_share + price
        avoid = cash_not_owning_share
        
        sell_or_avoid = max(sell, avoid)
        
        cash_not_owning_share = sell_or_avoid
        cash_owning_share = buy_or_hold
        
    return cash_not_owning_share

print(f"max profit 2 : {max_profit2(daily_price)}")
        


























