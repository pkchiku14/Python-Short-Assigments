# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iogQWR8mWD8G79f9VLHzWvMTBnZaKugh

# Write a python program to check whether the string is palindrome or not

Input: khokho

Output: The entered string is not palindrome

Input: amaama

Output: The string is palindrome
"""

string = input("get a string from the user")


def palindrome(a):
    mid = (len(a)-1)//2     
    start = 0                
    last = len(a)-1
    flag = 0
    while(start <= mid):
        if (a[start]== a[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break;
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")   
         
palindrome(string)