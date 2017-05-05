# factors = []
# prime_factors = []

# for i in range(1, 13195):
# 	if (13195 % i == 0):
# 		factors.append(i)
 
# # for j in range(len(factors) - 1):
# # 	if factors[j] % j == 0:
# # 		prime_factors.append(j)

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
