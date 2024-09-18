global excess
excess = 0
def fabricExcess(inches):
	Yards = inches // 36
	if (inches % 36 != 0):
		Yards = Yards + 1
		global excess
		excess = (Yards * 36) - inches
	return excess

print(fabricExcess(int(input())))