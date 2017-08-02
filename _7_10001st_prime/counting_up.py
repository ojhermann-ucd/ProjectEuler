def is_divisible(dividend, divisor):
	return ((dividend % divisor) == 0)

def is_prime(n):
	if n < 2:
		return False
	else:
		dividend = n
		divisor = 2
		while divisor < dividend:
			if is_divisible(dividend, divisor):
				return False
			else:
				divisor += 1
	return True

def is_prime_with_list(n, prime_list):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		largest_prime = prime_list[-1]
		if n < largest_prime:
			return False
		else:
			dividend = n
			for p in prime_list:
				if is_divisible(dividend, p):
					return False
		return True

if __name__ == "__main__":
	prime_list = []
	count = 0
	value = 0
	while count < 10001:
		if is_prime_with_list(value, prime_list):
			prime_list.append(value)
			count += 1
		value += 1
	print(value - 1)