'''Q2: Write a program that accepts a three digit number
from user and check whether it is palindrome or not.'''

number = int(input("enter the three digit number (100-999): "))

if 100 <= number <= 999:
    num_str = str(number)
    if num_str == num_str[::-1]:
        print(f"{number} number is palindrom .")
    else:
        print(f"{number} number is not palindrom .")
else:
    print("please enter only three digit  number  (100-999).")
