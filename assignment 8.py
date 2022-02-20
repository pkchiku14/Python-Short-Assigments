# -*- coding: utf-8 -*-
"""Write a Python program to drop empty Items from a given Dictionary. EXAMPLE: {'c1': 'Red', 'c2': 'Green', 'c3': None} New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
"""

d1 = {'c1':'red', 'c2':'green', 'c3': None}
d2 = {k:v for (k,v) in d1.items() if v is not None }
print(d2)
