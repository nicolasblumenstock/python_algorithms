# factors = []
# prime_factors = []

# for i in range(2, 13195):
# 	if (13195 % i == 0):
# 		factors.append(i)


# for j in factors:
# 	for k in range(2, j):
# 		if j % k == 0:
# 			factors.remove(j)



# print factors
# print prime_factors


# print factors


def prime_factors(n):
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(d)
			n = n/d
		d = d + 1
	print max(factors)

prime_factors(600851475143)

