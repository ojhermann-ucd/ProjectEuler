import operator
import functools
import grid


def horizonal_array_calculation_single_instance(array, width, start):
	sub_array = array[start:start+width:1]
	return functools.reduce(operator.mul, sub_array, 1)

def horizonal_array_calculation_1d_array(array, width):
	# data
	array_length = len(array)
	horizontal_product = 0
	# iteration
	for i in range(0, array_length - width +1, 1):
		current_product = horizonal_array_calculation_single_instance(array, width, i)
		if current_product > horizontal_product:
			horizontal_product = current_product
	return horizontal_product

def horizontal_product(array, width):
	maximum = 0
	for sub_array in array:
		value = horizonal_array_calculation_1d_array(sub_array, width)
		maximum = max(value, maximum)
	return maximum



def vertical_product(array, width):
	maximum = 0
	for row in range(0, 20 - width, 1):
		for column in range(0, 20, 1):
			product = 1
			for i in range(0, width, 1):
				product *= array[row + i][column]
			maximum = max(product, maximum)
	return maximum



def left_titling_product(array, width):
	maximum = 0
	for row in range(0, 20 - width +1, 1):
		for column in range(row, 20 - width + 1, 1):
			product = 1
			for i in range(0, width, 1):
				product *= array[row + i][column + i]
			maximum = max(product, maximum)
	return maximum



def right_tilting_product(array, width):
	maximum = 0
	for column in range(width, 20, 1):
		for row in range(0, 20 - width + 1, 1):
			product = 1
			for i in range(0, width, 1):
				product *= array[row + i][column - i]
			maximum = max(product, maximum)
	return maximum



if __name__ == "__main__":
	# data
	this_grid = grid.get_the_grid(grid.the_grid)

	# horizontal_product
	print(horizontal_product(this_grid, 4))

	# vertical_product
	print(vertical_product(this_grid, 4))

	# left_titling_product
	print(left_titling_product(this_grid, 4))

	# # right_tilting_product
	print(right_tilting_product(this_grid, 4))