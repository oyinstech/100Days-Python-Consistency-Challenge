#!/usr/bin/python3

# A program that reads the length and width of a farmer’s field 
# from the user in feet and display the area of the field in acres.

length = float(input("Enter the length of the field in feet : "))
width = float(input("Enter the width of the field in feet : "))

area = (length * width) / 43560

print(f"The Area of the field = {area} acres")
