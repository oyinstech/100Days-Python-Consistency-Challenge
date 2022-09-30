#!/usr/bin/python3

# A program that asks the user to enter the width and length of a room
# and display the area of the room
# The length and the width are entered as floating point numbers

length = float(input("Enter the length of the room in feet : "))
width = float(input("Enter the width of the room in feet : "))

area = length * width

print(f"The Area of the room = {area} square feet")
