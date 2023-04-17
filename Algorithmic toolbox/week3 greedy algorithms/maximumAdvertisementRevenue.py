

if __name__ == "__main__":
    number_of_ads = int(input())
    price_per_click = list(map(int, input().split()) )
    no_of_clicks = list(map(int, input().split()))
    
    price_per_click.sort()
    no_of_clicks.sort()
    #print(f"price_per_clicks: {price_per_click}")
    #print(f"no_of_clicks: {no_of_clicks}")

    total_revenue = 0
    for i in range(0,number_of_ads):
        #print(f"{price_per_click[i]} * {no_of_clicks[i]}")
        total_revenue += price_per_click[i] * no_of_clicks[i]
    print(total_revenue)