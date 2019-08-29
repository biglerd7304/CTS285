# -*- coding: utf-8 -*-
"""
Daniel Bigler
biglerd7304
M1HW_BiglerDaniel
CTS-285-0001
"""
def display_menu():
    print("Welcome to the calculator program.")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    
def repeat_menu():
    print("1. Repeat")
    print("2. Main menu")
    
def num():
    input1 = float(input("Enter a number: "))
    input2 = float(input("Enter a number: "))
    return (input1, input2)

def main():
    input1 = ''
    input2 = ''
    output = ''
    option = ''
    returnMainMenu = 2
    
    while returnMainMenu == 2:
        display_menu()
        option = int(input("Enter a menu option number: "))
        print("")
        repeat = 1
        
        if option == 1:
            while repeat == 1:
                print("")
                print("Add")
                input1, input2 = num()
                output = input1 + input2
                print(input1, "+" , input2 , "=", output)
                repeat_menu()
                repeat = int(input("Enter a number: "))
            
        elif option == 2:
            while repeat == 1:
                print("")
                print("Subtract")
                input1, input2 = num()
                output = input1 - input2
                print(input1, "-" , input2 , "=", output)
                repeat_menu()
                repeat = int(input("Enter a number: "))
                
        elif option == 3:
            while repeat == 1:
                print("")
                print("Divide")
                input1, input2 = num()
                output = input1 / input2
                print(input1, "/" , input2 , "=", output)
                repeat_menu()
                repeat = int(input("Enter a number: "))
                
        elif option == 4:
            while repeat == 1:
                print("")
                print("Multiply")
                input1, input2 = num()
                output = input1 * input2
                print(input1, "*" , input2 , "=", output)
                repeat_menu()
                repeat = int(input("Enter a number: "))
                
        elif option == 5:
            print("")
            print("Goodbye")
            returnMainMenu = 0
        else:
            print("You must enter a valid menu number.")
            
main()