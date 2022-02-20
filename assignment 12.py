# -*- coding: utf-8 -*-
"""
Write a python program for a number is Armstrong number or not
"""

number = int(input("Which number do you want to test ? : "))
order = len(str(number))

sum = 0

temp = number
while temp > 0:
  digit = temp % 10
  sum += digit ** order
  temp //= 10

if number == sum:
  print(f'the given number {number} is an Armstrong number')
else:
  print(f'the given number {number} is not an Armstrong number')
