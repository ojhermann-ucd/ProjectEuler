name_list = list()
with open("p022_names.txt", "r") as source:
	name_list = source.read().replace("\"","").lower().split(",")
name_list.sort()

count = 1
total = 0
for name in name_list:
	total += count * sum([ord(c) - 96 for c in list(name)]) # reduce ord(c) by 96 to reflect char score from problem
	count += 1
print(total)