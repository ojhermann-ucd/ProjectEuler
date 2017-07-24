"""
https://projecteuler.net/problem=2
"""

# imports



if __name__ == "__main__":
	output = 2
	a = 1
	b = 2
	fib = 2
	while fib <= 4000000:
		fib = a + b
		if (fib % 2) == 0:
			output += fib
		a = b
		b = fib
	print(output)