# -*- coding: utf-8 -*-
"""Write a program for prime number in a given range
"""

def prime_check(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print(f'{number} is a prime number')
  else:
    print(f'{number} is a not prime number')


start = int(input("give the start number"))
end = int(input("give the end number"))

for k in range(start,end):
  prime_check(k)
