def parrot(talking,hour):
    return talking and (hour < 7 or hour > 20)

talking = input() == "True"
hour = int(input())

print(parrot(talking,hour))