def factorial(n):
	factorial = 1
	multiplier = n
	while multiplier > 1:
		factorial *= multiplier
		multiplier -= 1
	return factorial

print(sum([int(x) for x in list(str(factorial(100)))]))