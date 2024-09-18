
def eggCartons(eggs):
	carton = eggs // 12
	if (eggs % 12 != 0):
		carton = carton + 1
	return carton

print(eggCartons(int(input())))