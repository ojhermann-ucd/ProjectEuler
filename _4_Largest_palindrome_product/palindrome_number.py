def int_to_str(n):
	return str(n)

def check_palindrome(n):
	n_string = int_to_str(n)
	index_1 = 0
	index_2 = -1
	length = len(n_string)

	if length % 2 == 0:
		left_mid_point_index = (len(n_string) / 2) - 1
		right_mid_point_index = left_mid_point_index + 1
	else:
		left_mid_point_index = int(len(n_string) / 2)
		right_mid_point_index = left_mid_point_index
	is_palindrome = True

	while is_palindrome:
		is_palindrome = n_string[index_1] == n_string[index_2]
		if not is_palindrome:
			return False
		else:
			if index_1 == left_mid_point_index:
				return True
			else:
				index_1 += 1
				index_2 -= 1

if __name__ == "__main__":
	palindrome = 0
	for i in range(100, 1000, 1):
		for j in range(100, 1000, 1):
			result = i * j
			if check_palindrome(result):
				if result > palindrome:
					palindrome = result
print(palindrome)