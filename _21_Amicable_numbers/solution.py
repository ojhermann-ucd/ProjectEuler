# amicable_pair
def proper_divisors(n):
	return [d for d in range(1, n) if n % d == 0]

def sum_of_proper_divisors(n):
	return sum(proper_divisors(n))

def amicable_pair(a, b):
	return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a


amicable_numbers_list = list()
for a in range(1, 10000 + 1, 1):
	if a not in amicable_numbers_list:
		b = sum_of_proper_divisors(a)
		if 	a != b and amicable_pair(a, b):
			amicable_numbers_list.append(a)
			amicable_numbers_list.append(b)
print(amicable_numbers_list)
print(sum(amicable_numbers_list))