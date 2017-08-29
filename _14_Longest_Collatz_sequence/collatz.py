def collatz_rule(n):
	if n % 2 == 0:
		return int(n / 2)
	else:
		return int(3*n + 1)

def collatz_chain_length(n):
	length = 1
	while n != 1:
		length += 1
		n = collatz_rule(n)
	return length

def longest_chain():
	the_number = 0
	the_length = 0
	for i in range(1, 1000000, 1):
		temp_length = collatz_chain_length(i)
		if temp_length > the_length:
			the_length = temp_length
			the_number = i
	return [the_number, the_length]

print(longest_chain())