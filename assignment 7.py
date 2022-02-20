# -*- coding: utf-8 -*-
"""Given a List of Numbers, you are required to find the second maximum number?

Note - List Contains duplicate numbers

Example:
Input : [0,2,8,5,4,6,3,5,7,8,7]
Output : 7
"""

list1 = list(input('input numbers').split())
list2 = []
for i in list1:
  if i not in list2:
    list2.append(i)

list2.sort()
print(f'the second largest number is {list2[-2]}')
