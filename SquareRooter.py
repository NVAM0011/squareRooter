def squareroot(x):
    factor1 = x*0.5
    factor2 = x/factor1
    while not (abs(factor1-factor2)<(5/(10**16))):
        factor2 = x/factor1
        factor1 = (factor1+factor2)/2
    return (factor1+factor2)/

print(squareroot(float(input("What number would you like to square root?\n"))))
