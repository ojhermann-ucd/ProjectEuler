def prime_factors(dividend):
	divisor = 2
	while divisor <= dividend:
		while (dividend % divisor) == 0:
			dividend /= divisor
			if dividend == 1:
				return divisor
		divisor += 1


print(prime_factors(600851475143))