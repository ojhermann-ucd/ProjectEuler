# imports



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
	else:
		largest_prime = prime_list[-1]
		if n < largest_prime:
			return False
		else:
			dividend = n
			for p in prime_list:
				if is_divisible(dividend, p):
					return False
		prime_list.append(n)
		return True


def sieve(n_list):
	the_sum = 0
	for n in n_list:
		if n is None:
			pass
		else:
			print(n)
			the_sum += n
			index = n_list.index(n)
			go_for_it = True
			while go_for_it:
				try:
					index += n
					n_list[index] = None
				except:
					go_for_it = False
	return the_sum








if __name__ == "__main__":
	numbers = [i for i in range(3, 2000000, 2)]
	numbers = sieve(numbers)
	print(numbers + 2)

	# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# print(numbers)
	# for i in numbers[::2]:
	# 	numbers[numbers.index(i)] = None
	# print(numbers)

	# print(sieve(2000000))
	
	# prime_list = [2]
	# number = 2
	# the_sum = 0
	# while number < 2000000:
	# 	if is_prime_with_list(number, prime_list):
	# 		the_sum += number
	# 		print(prime_list[-1])
	# 	number += 1
	# print(the_sum - prime_list[-1])