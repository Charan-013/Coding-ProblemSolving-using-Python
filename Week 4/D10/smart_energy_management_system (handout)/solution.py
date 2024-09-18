def isEnergySaving(house_occupied,high_energy,peak_hours,current_energy_usage):
    a = (house_occupied == False)
    b = (high_energy and peak_hours == True)
    c = ((current_energy_usage > 50)== True)
    return a or b and c

house_occupied = input() == "True"
high_energy = input() == "True"
peak_hours = input() == "True"
current_energy_usage = int(input())

print(isEnergySaving(house_occupied,high_energy,peak_hours,current_energy_usage))