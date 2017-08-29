def get_the_numbers():
	the_numbers = list()
	with open("the_numbers.txt", "r") as source:
		for line in source:
			the_numbers.append(int(line))
	return the_numbers

print(sum(get_the_numbers()))