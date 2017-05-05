num_sum = [] 

for i in range(1000):
	if (i % 3 == 0 or i % 5 == 0):
		num_sum.append(i)


b = sum(num_sum)
print b
