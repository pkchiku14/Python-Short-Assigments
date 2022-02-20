# -*- coding: utf-8 -*-
"""Given a lost of numbers , convert every odd integer into even by adding 1 and convert every even integer into odd by adding 3.
* input : 2 3 4 1 8 11
* output : 5 4 7 2 11 12

explanation : odd places numbers are added by 1 and even number are added by 3.
"""

numbers = input("give the numbers list").split()
numbers = [int(i) for i in numbers]
new_number = []
for j in numbers:
  if j % 2 == 0:
    new_number.append(j + 3)
  else:
    new_number.append(j + 1)

print(new_number)
