#------------------------------------------------------------------------------------------------------------------------
# Program name – draw_shape.py
# Written by – Naylene
# Date – April 9, 2017
# Imports and Calls
#--------------------------------------------------------------------------------------------------------------------------

import turtle
from draw import *

#Constant Variables
DRAW_SQUARE_CHOICE =1
DRAW_RECTANGLE_CHOICE =2
DRAW_ANYSHAPE_CHOICE =3
QUIT_CHOICE = 4

def main():
    """Main function"""
    myTurtle = turtle.Turtle()
    choice = 0

    while choice != 4:
        choice = int(userMenu())

        if choice == 1:
            size = float(input("Please enter a side length: "))
            drawSquare(myTurtle, size)

        elif choice == 2:
            size = float(input("Please enter the small side length: "))
            drawRectangle(myTurtle, size)

        elif choice == 3:
            logo = int(input("If you want the full logo, type 1. If you want the eye only, type 2: "))
            nightVale(myTurtle, logo)

        elif choice == 4:
            print("Quiting...")
            
        else:
            print("Not a valid entry.")

def userMenu():
    """User menu function"""
    print()
    print("~~~  Menu ")
    print("(1) Create a Square")
    print("(2) Create a Rectangle")
    print("(3) Night Vale Logo")
    print("(4) Quit")

    print("\nWhat do you want to do?")
    user = input()

    return user


main()  #Call main
