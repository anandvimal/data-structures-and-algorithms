def find_most_expensive_item_per_unit(total_items: int, items: dict):
    max_cost_per_item = 0
    max_cost_per_item_index = -1
    for item in range(0, total_items):
        #print(f"item number:{item} : item_weight:{items[item][1]} item_cost_per_unit:{items[item][0]} ")
        if items[item][1] > 0: # weight check more than 0
            if items[item][0] > max_cost_per_item:
                max_cost_per_item = items[item][0]
                max_cost_per_item_index = item
    return max_cost_per_item_index

if __name__ == "__main__":
    
    # get all details here for items etc.
    total_items, backpack_capacity = map(int, input().split())
    items = {}
    stolen_worth = 0
    for item in range(0,total_items):
        item_cost, item_weight= map(int, input().split())
        if item_weight>0:
            cost_per_item=item_cost/item_weight
        else:
            cost_per_item = 0
        items[item] = [cost_per_item,  item_weight, item_cost]
    
    #print(items)

    most_expensive_item_per_unit = find_most_expensive_item_per_unit(total_items, items)
    #print(f"use this : {most_expensive_item_per_unit}")

    while most_expensive_item_per_unit >= 0 and backpack_capacity > 0:
        if backpack_capacity >= items[most_expensive_item_per_unit][1]:
            backpack_capacity -= items[most_expensive_item_per_unit][1]
            stolen_worth += items[most_expensive_item_per_unit][1] * items[most_expensive_item_per_unit][0] # weight picked in backpack * cost of per unit weight
            items[most_expensive_item_per_unit][1] = 0
        elif items[most_expensive_item_per_unit][1] > backpack_capacity:
            stolen_worth +=backpack_capacity * items[most_expensive_item_per_unit][0] # weight picked in backpack * cost of per unit weight
            backpack_capacity = 0
            items[most_expensive_item_per_unit][1] -=  backpack_capacity
        #print(f"backpack :{backpack_capacity} ")
        #print(f"items: {items}")
        most_expensive_item_per_unit = find_most_expensive_item_per_unit(total_items, items)
        #print(f"use this : {most_expensive_item_per_unit}")
    print(stolen_worth)
