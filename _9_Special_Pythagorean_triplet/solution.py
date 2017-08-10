# imports



def check_if_pythagorean_triplet(a, b, c):
	if (a < b) and (b < c) and (a**2 + b**2 == c**2):
		return True



def brute_way_to_find_pythagorean_triplet(value):
	for c in range(2, 999, 1):
		for b in range(1, 998, 1):
			for a in range(0, 997, 1):
				if check_if_pythagorean_triplet(a, b, c) and (a + b + c) == value:
					return a*b*c



print(brute_way_to_find_pythagorean_triplet(1000))