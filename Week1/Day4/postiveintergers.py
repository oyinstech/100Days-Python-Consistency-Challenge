#!/usr/bin/python3

# A program that reads a positive integer, n, from the user
# and displays the sum of all of the integers from 1 to n.

n = int(input("Enter a positive number: "))

sum = (n * (n + 1)) / 2
print(f"The sum of the first {n} positive integers is {sum}.")
