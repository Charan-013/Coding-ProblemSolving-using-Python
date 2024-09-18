def water(soil_dry,raining,day_time,temperature):
    a = (soil_dry == True)
    b = (raining == False)
    c = (day_time == True)
    d = ((temperature > 10) == True)
    return a and b and c and d

soil_dry = input() == "True"
raining = input() == "True"
day_time = input() == "True"
temperature = int(input())

print(water(soil_dry,raining,day_time,temperature))