fib_list = [1, 1]
f = 1
even_list = []
while f <= 4000000:
	f = fib_list[-1] + fib_list[-2]
	fib_list.append(f)

del fib_list[-1]

for i in fib_list:
	if i % 2 == 0:
		even_list.append(i)

print sum(even_list)



		


