def the_numbers(w):
	the_sum = 1
	current = 1
	increment = 2
	width = increment + 1
	while width < w + 1:
		for j in range(1, 5, 1):
			current += increment
			the_sum += current
		increment += 2
		width = increment + 1
	return the_sum

print(the_numbers(1001))