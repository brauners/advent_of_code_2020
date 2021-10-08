if __name__ == "__main__":
    with open("13.in") as f:
        input = [x.strip() for x in f.readlines()]

    current_time = int(input[0])
    buses = {}
    for bus in input[1].split(','):
        if not bus == 'x':
            bus = int(bus)
            minutes_to_departure = bus - (current_time % bus)
            buses[bus] = minutes_to_departure
    
    next_bus = min(buses, key=buses.get)
    print(buses[next_bus]* next_bus)
