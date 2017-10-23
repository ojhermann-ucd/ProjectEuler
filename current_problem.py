# from decimal import *
# getcontext().prec = 64


# def possible_patterns(string):
# 	return [string[0:k+1:1] for k in range(len(string))]

# print(possible_patterns("otto"))




# def equilibrium_index(arrayA, intN):
# 	# initial values
# 	below_index_sum = 0
# 	above_index_sum = sum(arrayA[1::1])
# 	# index = 0
# 	if above_index_sum == below_index_sum:
# 		return 0
# 	# iteration
# 	index = 1
# 	while index < intN:
# 		below_index_sum += arrayA[index - 1]
# 		above_index_sum -= arrayA[index]
# 		if above_index_sum == below_index_sum:
# 			return index
# 		index += 1
# 	return -1

# A = [-1, 3, -4, 5, 1, -6, 2, 1]
# print(A[0])
# print(sum(A[2::1]))

# print(equilibrium_index(A, 8))




# n = 10**12 + 1
# while True:
# 	if n * (n - 1) % 2 == 0:
# 		a_value = int(n * (n - 1) / 2)
# 		# print(a_value)
# 		for k in range(1, a_value):
# 			if a_value % k == 0 and k * (k + 1) == a_value:
# 				print("answer", k + 1)
# 				break
# 	n += 1
# 	print(n)



# current = 1
# print(current)
# for i in range(1, 5, 1):
# 	current += 2
# 	print(current)
# for i in range(1, 5, 1):
# 	current += 4
# 	print(current)
# for i in range(1, 5, 1):
# 	current += 6
# 	print(current)