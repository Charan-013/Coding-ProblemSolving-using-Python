def replace(s1, s2, s3):
	result = ""
	i = 0
	while i < len(s1):
		if s1[i:i+len(s2)] == s2:
			result = result + s3
			i = i + len(s2)
		else:
			result = result + s1[i]
			i = i + 1
	return result 

print(replace(input(), input(), input()))
