"""
https://projecteuler.net/problem=1
"""

# imports



# functions
def multiple_of_n(number, n):
	return ((number % n) == 0)

if __name__ == "__main__":
	current = 6
	output = 3 + 5
	while current < 1000:
		if multiple_of_n(current, 3) or multiple_of_n(current, 5):
			output += current
		current += 1
	print(output)