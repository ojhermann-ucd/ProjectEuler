def factorial(n, holder):
	if n == 2:
		return 2 * holder
	else:
		return factorial(n-1, holder * n)

numerator = factorial(40, 1)
denominator = factorial(20, 1) * factorial(20, 1)
print(int(numerator / denominator))