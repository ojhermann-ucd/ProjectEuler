# imports
import time


def prime_sum(n):
	if n < 2:
		return 0
	elif n == 2:
		return 2
	else:
		primes = {k:True for k in range(n)}
		primes[0], primes[1] = False, False
		p_sum = 0
		for number in primes:
			if primes[number]:
				p_sum += number
				for i in range(2*number, n, number):
					primes[i] = False
		return p_sum


def prime_sum_time(n):
	start = time.time()
	the_sum = prime_sum(n)
	the_time = time.time() - start
	return "It took {} to find the sum of the primes less than {}, which is {}".format(the_time, n, the_sum)


if __name__ == "__main__":
	print(prime_sum_time(10))
	print(prime_sum_time(100))
	print(prime_sum_time(1000))
	print(prime_sum_time(10000))
	print(prime_sum_time(100000))
	print(prime_sum_time(1000000))
	print(prime_sum_time(2000000))