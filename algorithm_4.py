def the_sieve(n):
    prime_list = [2,3]
    i = 4
    while len(prime_list) <= n - 1:
        for j in prime_list:
            is_prime = True
            if i % j == 0:
                is_prime = False
                break
        if is_prime:		
            prime_list.append(i)
        i += 1	
    
    print prime_list[-1]

the_sieve(10001)
