# -*- coding: utf-8 -*-
"""Write a program that reads a string from keyboard and display:

* The number of uppercase letters in the string
* The number of lowercase letters in the string
* The number of digits in the string
* The number of whitespace characters in the string
Input: Stay home during the COVID-19 outbreak.

Output: The number of uppercase letters: 6

The number of lowercase letters: 24

The number of digits: 2

The number of whitespace characters: 5
"""

sentence = input("Give the sentence")
up = low = digit = space = 0
for i in sentence:
  if i.isupper():
    up += 1
  elif i.islower():
    low += 1
  elif i.isdigit():
    digit += 1
  elif i == ' ':
    space += 1

print(f'the count of upper, lower, digit and space in the sentence is {up},{low},{digit} and {space} respectively')
