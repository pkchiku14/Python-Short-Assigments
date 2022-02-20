# -*- coding: utf-8 -*-
"""Write a python program to find the sum of tuple elements
Input : test_tup = (7, 8, 9, 1, 10, 7)

Output : 42
"""

test_tup = (7, 8, 9, 1, 10, 7)
sum = 0
for i in test_tup:
  sum += i

print(sum)
