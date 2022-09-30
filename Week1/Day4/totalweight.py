#!/usr/bin/python3

# Reads the number of widgets and the number of gizmos in an order
# from the user and displays the total weight of the order

widget_weight = 75
gizmo_weight = 112

widget = int(input('Enter the number of widgets order: '))
gizmo = int(input('Enter the number of gizmos order: '))

total_weight =  widget * widget_weight + gizmo * gizmo_weight

print(f"The total weight of the order is {total_weight:.2f}kg")
