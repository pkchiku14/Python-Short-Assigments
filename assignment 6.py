# -*- coding: utf-8 -*-
"""Find the duplicates in a List.

Example:

Input: [1,2,2,5,5,6]

Output: 2 5
"""

list1 = list(input("input numbers").split())
list2 = []
list3= []
for i in list1:
  if i not in list2:
    list2.append(i)
  else:
    list3.append(i)

print(list3)
