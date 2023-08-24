'''
Jack Bianca COMP 3240 Spring 2023 Programming Assignment 6
'''
'''
The sieve of Eratosthenes
Returns a list of prime numbers up to n
'''
def sieve_of_Eratosthenes(n):
   sieve = [True]*(n+1)
   sieve[0] = sieve[1] = False
   for i in range(2, int(n**0.5) + 1):
      if sieve[i]:
         for j in range(i*1, n+1, i):
            sieve[j] = False
   return [i for i in range(2, n+1) if sieve[i]]
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
Prime factorization
factorizes the number n into its prime factors, puts those in a list,
and uses sieve of eratosthenes to generate primes.
'''
def prime_factorization(n):
   prime_numbers = sieve_of_eratosthenes(int(n**0.5)+1)
   a = []
   for i in prime_numbers:
      while n % i == 0:
         a.append(i)
         n //= i
   if n>1:
      a.append(n)
   return a
'''
Pollard Rho algorithm
Returns a non-trivial factor of n
'''
def pollard_rho(n, c=1):
   x = y = 2
   z = 1
   while d == 1:
      x = (x*x + c) % n
      y = (y*y + c) % n
      y = (y*y + c) % n
      z = math.gcd(abs(x-y), n)
   if z == n:
      return
'''
This is the entry point for the program when you are running it on your
local machine. This function will not be executed when it is graded by
Gradescope.
'''
numToFactorize = 72
factors = trial_division(numToFactorize)
print(factors)
