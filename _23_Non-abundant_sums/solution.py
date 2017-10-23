# preliminaries
def proper_divisors(n):
	return [d for d in range(1, n) if n % d == 0]

def sum_of_proper_divisors(n):
	return sum(proper_divisors(n))


# limit = 28123
# abundant_numbers_list = list()
# n = 1
# while n < limit + 1:
# 	if sum_of_proper_divisors(n) > n:
# 		abundant_numbers_list.append(n)
# 	n += 1




