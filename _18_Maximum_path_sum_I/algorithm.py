# imports
from data import pyramid

def reverse_array_of_arrays(array_of_arrays):
	new_array = list()
	length = len(pyramid)
	for k in range(1, length+1):
		new_array.append(array_of_arrays[-k])
	return new_array

reversed_pyramid = reverse_array_of_arrays(pyramid)
for r in reversed_pyramid:
	print(r)

def combine_rows(big, small):
	output = [0 for s in small]
	index = 0
	for s in small:
		b = max(big[index], big[index + 1]) # determine the larger neighbour
		output[index] = s + b
		index += 1
	return output

my_test = combine_rows(reversed_pyramid[0], reversed_pyramid[1])
print("")
print("combine_rows test")
print(my_test)
print("")

big = combine_rows(reversed_pyramid[0], reversed_pyramid[1])
for small in reversed_pyramid[2::1]:
	big = combine_rows(big, small)
	print(big)
	print(small)
	print("")
print("Answer: {}".format(big[0]))