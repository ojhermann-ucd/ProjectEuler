def sum_of_numbers_to_power(start, end, power):
	n = start
	output = 0
	while n < (end + 1):
		output += n**power
		n += 1
	return output


if __name__ == "__main__":
	smaller = sum_of_numbers_to_power(1, 100, 2)
	larger = sum_of_numbers_to_power(1, 100, 1)**2
	print(larger - smaller)