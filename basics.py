# Krystian Opryszek 
# Pyrhon basics 
# 2021-02-12

def factorial(n):
    """Number to calculate functional of."""
    #deal with negative inputs
    if n < 1:
        m = -n
    else:
        m = n
    # the running total - eventually the factional
    total = 1
    #loop to do the multiplications
    while m > 0:
        total = total * m
        m = m - 1
    #return the answer
    if n < 1:
        return -total
    else:
        return total

#test the function
n = -20
#calculate the factorial of n
print(f"The functional of {n} is {factorial(n)}.")