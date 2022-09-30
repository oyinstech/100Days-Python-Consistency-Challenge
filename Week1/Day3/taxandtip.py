#!/usr/bin/python3

tax_rate = 0.04
tip_rate = 0.18

cost = float(input("Enter the cost of the meal: $"))

tax = cost * tax_rate
tip = cost * tip_rate
total = cost + tax + tip

print(f"The tax for the meal is ${tax:.2f})
print(f"The tip for the meal is ${tip:.2f}")
print(f"The total cost of the meal is ${total:.2f}")
