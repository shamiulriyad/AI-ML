def prime(n):
    if n <=1:
        return 0
    i =2
    while i*i<=n:
        if n%i==0:
            return 0
        i+=1
    return 1

num = [2, 3, 4, 5, 6, 7, 8,9,10]

for n in num:
    if prime(n):
        print(n, end=" ")