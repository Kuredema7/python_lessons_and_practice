from os import system

#Add number_one to number_two
def add(number_one, number_two):
    return (number_one + number_two)

#Subtract number_one from number_two
def subtract(number_one, number_two):
    return (number_one - number_two)

#Multiply number_one by number_two
def multiply(number_one, number_two):
    return (number_one * number_two)

#Divide number_one by number_two
def divide(number_one, number_two):
    return (number_one / number_two)
    
#Square number_one by number_two
def square(number_one, number_two):
    return (number_one ** number_two)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square
}

def calculator():
    calculating = True

    number_one = float(input('Enter your first number: '))

    for operation in operations:
        print(operation)

    while calculating:

        operation_symbol = input('Pick an operation: ')

        if operation_symbol not in operations:
            print('You provided invalid operation symbol.\n')
            continue
        else:
            next_number = float(input('Enter the next number: '))
            
            result = operations[operation_symbol](number_one, next_number)
            print(f"{number_one} {operation_symbol} {next_number} = {result}")
            
            choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start new calculation, or type 'q' to exit: ").lower()
            
            if (choice != 'y') and (choice != 'n'):
                # Exiting the program
                calculating = False
            elif choice == 'y':
                #It assigns the result to the previous number
                number_one = result
            else:
                #Stopping the while loop
                calculating = False

                #Clears the display
                system('cls') 

                #Starting a new calculation
                calculator()

calculator()