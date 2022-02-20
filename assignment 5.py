# -*- coding: utf-8 -*-
"""take an input as list of numbers , and print all the numbers that are divisible by 10

input : 1 3 20 25 30 output : 2 explanation : 20,30 are both divisbile 10 , you need to return output as 2
"""

number = list(input('input numbers').split())
count = 0
for i in number:
  if int(i) % 10 == 0:
    count += 1

print(f'output: {count}')
