def interleave(s1, s2):
	i = 0
	result = ""
	length = min(len(s1),len(s2))
	for i in range(length):
		result += s1[i] + s2[i]
	

	if len(s1) > len(s2):
		result += s1[length:]
	else:
		result += s2[length:]
	return result

print(interleave(input(), input()))