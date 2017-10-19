f_1 = 1
f_2 = 1
f = 2
index = 2
while (len(str(f)) < 1000):
	holder = f
	f = f_1 + f_2
	f_1 = f_2
	f_2 = f
	index += 1
print(index)
print(len(str(f)))