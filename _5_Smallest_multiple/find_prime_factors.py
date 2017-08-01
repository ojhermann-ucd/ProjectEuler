def prime_factors(n):
	pf_dict = dict()
	dividend = n
	divisor = 2
	status = True
	while status:
		status = ((dividend % divisor) == 0)
		if status:
			dividend /= divisor
			if divisor in pf_dict:
				pf_dict[divisor] += 1
			else:
				pf_dict[divisor] = 1
		else:
			divisor += 1
			if dividend == 1:
				pass
			else:
				status = True
	return pf_dict



def prime_factors_in_range(start, end):
	pf_dict = dict()
	for i in range(start, end + 1, 1):
		pf_temp = prime_factors(i)
		for number in pf_temp:
			if number in pf_dict:
				if pf_temp[number] > pf_dict[number]:
					pf_dict[number] = pf_temp[number]
			else:
				pf_dict[number] = pf_temp[number]
	return pf_dict


if __name__ == "__main__":
	test_dict = prime_factors_in_range(1, 20)
	output = 1
	for key in test_dict:
		value = test_dict[key]
		mult = key ** value
		output *= mult
	print(output)