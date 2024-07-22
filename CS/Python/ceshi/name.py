'''
Author: 崩布猪
Date: 2024-04-16 09:54:07
LastEditors: 崩布猪
LastEditTime: 2024-04-16 09:56:31
FilePath: \P_code\ceshi\name.py
Description: 

'''
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Please enter your first name: ")
    if first == 'q':
        break
    last = input("Please enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tYour formatted name is:", formatted_name)