sub_twenty_dict = {
	0:"",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen",
	}

tens_dict = {
	0:"",
	20:"twenty",
	30:"thirty",
	40:"forty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninety"
	}

hundreds_dict = {
	0:"",
	100:"onehundred",
	200:"twohundred",
	300:"threehundred",
	400:"fourhundred",
	500:"fivehundred",
	600:"sixhundred",
	700:"sevenhundred",
	800:"eighthundred",
	900:"ninehundred",
}

def english(n, sub_twenty_dict, tens_dict, hundreds_dict):
	if n < 20:
		return sub_twenty_dict[n]
	elif n < 100:
		tens_part = (n // 10) * 10
		ones_part = n - tens_part
		return tens_dict[tens_part] + sub_twenty_dict[ones_part]
	elif n < 1000:
		hundreds_part = (n // 100) * 100
		if (n - hundreds_part) in sub_twenty_dict and (n - hundreds_part) != 0:
			return hundreds_dict[hundreds_part] + "and" + sub_twenty_dict[(n - hundreds_part)]
		tens_part = ((n - hundreds_part) // 10) * 10
		ones_part = (n - hundreds_part - tens_part)
		if tens_part == 0 and ones_part == 0:
			return hundreds_dict[hundreds_part]
		else:
			return hundreds_dict[hundreds_part] + "and" + tens_dict[tens_part] + sub_twenty_dict[ones_part]
	else:
		return "onethousand"

my_string = ""
for i in range(1, 1001, 1):
	print(english(i, sub_twenty_dict, tens_dict, hundreds_dict))
	my_string += english(i, sub_twenty_dict, tens_dict, hundreds_dict)
print(len(my_string))