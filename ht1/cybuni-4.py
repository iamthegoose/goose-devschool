def isNumPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
# for i in range(20):
#     print(f"Число {i} просте: {isNumPrime(i)}")