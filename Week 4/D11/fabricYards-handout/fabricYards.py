
def fabricYards(inches):
	Yards = inches // 36
	if (inches % 36 !=0):
			Yards = Yards + 1				
	return Yards

print(fabricYards(int(input())))