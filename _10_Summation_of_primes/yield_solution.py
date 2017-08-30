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



def get_prime(number, limit):
	while number < limit:
		if is_prime(number):
			yield number
		number += 1



def prime_sum(number, limit):
	p_sum = 0
	for n in get_prime(number, limit):
		p_sum += n
	return p_sum



if __name__ == "__main__":
	print(prime_sum(2, 2000000))