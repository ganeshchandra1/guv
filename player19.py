def prime_factors2(n):
        i = 2
        factors = []
        count = 0                           
        while i * i <= n:                     
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
n=int(input())
print(' '.join(map(str,(set(prime_factors2(n))))))
