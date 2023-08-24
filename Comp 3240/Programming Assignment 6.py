'''
Jack Bianca
jab0261
Comp 3240 - 001
Programming Assignment 6
'''
'''
Factorizes the number passed into n into its prime factors and returns those
factors as a list.
n - integer to factor
Returns an array list containing the integer prime factors of n
'''
def trial_division(n: int) -> list:
a = []
divise = 2
while n > 1:
if n % divise == 0:
a.append(divise)
n //= divise
else:
divise += 1
return a

'''
This is the entry point for the program when you are running it on your
local machine. This function will not be executed when it is graded by
Gradescope.
'''
numToFactorize = 72
factors = trial_division(numToFactorize)
print(factors)
