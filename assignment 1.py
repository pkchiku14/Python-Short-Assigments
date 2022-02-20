# -*- coding: utf-8 -*-
# A tree has n branches , 1st branch has 1 leaf , 2nd branch has 3 leaves , 3rd branch has 5 leaves , 4th branch has 7 leaves and so on , calculate the sum of leaves of n branhes

# input : 4 (number of branches)
# output : 16 (1+3+5+7)

branch = int(input('Number of branches'))
leaf  = 2 * branch - 1
print(f'the number of leaves are {leaf}')
sum = branch ** 2 
print(f'the sum of the leaves is {sum}')
