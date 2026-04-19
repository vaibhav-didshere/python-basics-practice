num = 7
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
    
print("prime" if is_prime else "not prime")