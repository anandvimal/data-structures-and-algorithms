
def where_to_fuel_next(starting_range: int, end_range:int, stops: list):
    stops_in_range = []
    for stop in stops:
        if stop > starting_range and stop <= end_range:
            stops_in_range.append(stop)
    #print(f"stops in range = {stops_in_range}")
    if (stops_in_range):
        last_stop_to_refuel = max(stops_in_range)
        return last_stop_to_refuel
    else:
        return -1

if __name__ == "__main__":
 
    distance_to_travel = int(input())
    mileage_of_car = int(input())
    number_of_stops = int(input())
    stops = list(map(int, input().split()))

    position_of_car =0 
    minimum_number_of_stops = 0

    while (position_of_car+mileage_of_car < distance_to_travel):
        starting_range = position_of_car
        end_range = position_of_car + mileage_of_car
        position_of_car = where_to_fuel_next(starting_range, end_range, stops)
        if position_of_car == -1:
            minimum_number_of_stops = -1
            break
        minimum_number_of_stops += 1

    print(minimum_number_of_stops)

    
