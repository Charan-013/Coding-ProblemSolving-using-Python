
def isLegalTriangle(s1, s2, s3):
	if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
		return True
	return False

print(isLegalTriangle(float(input()), float(input()), float(input())))