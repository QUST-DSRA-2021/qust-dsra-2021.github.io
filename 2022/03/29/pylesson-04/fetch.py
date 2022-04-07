#!/usr/bin/env Python
# -*- coding: utf-8 -*-
try:
    num = int(input("Input an Integer: "))
    print(num ** 2)
except NameError as err:
    print("Invalid Input, which cannot convert to a num!")
except ValueError as err:
    print("Invalid Input, which is not an integer!")