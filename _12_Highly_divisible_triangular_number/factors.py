def factors(n):
	# starting data
	divisor = 2
	dividend = n
	# return data
	divisor_list = [1]
	dividend_list = [n]
	# populate lists
	while divisor < dividend_list[-1]:
		if dividend % divisor == 0:
			divisor_list.append(divisor)
			dividend_list.append(int(dividend / divisor))
		divisor += 1
	# return
	dividend_list.reverse()
	return divisor_list + dividend_list

def triangle_number(n):
	"""
	x + (x+1) + (x+2) + . . . = nx + (n-1)(n/2) = nx + (n^2 - n)(1/2)
	"""
	return int(n + (n**2 - n)*(1/2))

def first_to_500():
	n = 1
	found = False
	while not found:
		tn = triangle_number(n)
		length = len(factors(tn))
		if length > 499:
			return tn
		n +=1



if __name__ == "__main__":
	print(first_to_500())