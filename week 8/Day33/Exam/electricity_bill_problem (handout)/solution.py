def calculate_electricity_bill(units):
    total_cost = 0.0
    
    if units > 800:
        excess_units = units - 800
        total_cost += excess_units * 2.00
        total_cost += total_cost * 0.30
        units = 800
    
    if units > 600:
        excess_units = units - 600
        total_cost += excess_units * 1.75
        total_cost += total_cost * 0.25
        units = 600
    
    if units > 400:
        excess_units = units - 400
        total_cost += excess_units * 1.50
        total_cost += total_cost * 0.20
        units = 400
    
    if units > 250:
        excess_units = units - 250
        total_cost += excess_units * 1.20
        total_cost += total_cost * 0.15
        units = 250
    
    if units > 150:
        excess_units = units - 150
        total_cost += excess_units * 0.75
        total_cost += total_cost * 0.10
        units = 150
    
    if units > 50:
        excess_units = units - 50
        total_cost += excess_units * 0.50
        total_cost += total_cost * 0.05
        units = 50
    
    if units > 0:
        total_cost += units * 0.30
    
    if total_cost > 1000:
        total_cost += 100
    
    return round(total_cost, 2)


print(calculate_electricity_bill(units=int(input())))