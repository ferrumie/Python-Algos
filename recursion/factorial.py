def fact(n):
    # identify the recursive case
    # n! = n * (n-1) * (n-2) * 2 * 1
    if int(n) == 1 or 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))