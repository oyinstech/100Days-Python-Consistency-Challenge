#!/usr/bin/python3

small_deposit = 0.10
big_deposit = 0.25

small = int(input("Enter number of containers (1 litre or less): "))
big = int(input("Enter number of containers (greater than 1 litre): "))

refund = small * small_deposit + big * big_deposit
print(f"\nYou will be refunded ${refund:.2f} for your containers.")
