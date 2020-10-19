# -*- coding: utf-8 -*-

cont = "y"

i = 0

while cont == "y":
    num = input("How many numbers?")
    for x in range(i, int(num) + i):
        print(x)
    i = i + int(num)
    cont = input("Continue? y or n")
    if "n":
        print("Goodbye")