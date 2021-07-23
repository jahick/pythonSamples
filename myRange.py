
# File: testmyrange.py
# Project 6.10
# Defines a function that behaves like Python's range function.



# Function "myRange" is defined here.

def myRange (stop, start = 0, step = 1):            # Header for function "myRange". Contains required "stop" and optional "start" and "step".

    if start == "" or start == None:                # If/else statement to check if default value needs to be used for "start".
        start = 0                                   # If condition: Empty string input causes "start" to default to 0, the default value.
    else:
        start = int(start)                          # Else condition: Assumes a number was input and uses the input instead of 0, the default value.
    
    if step == "" or step == None or step == 0:     #If/else statement to check if default value needs to be used for "step".
        step = 1                                    #If condition: Empty string input causes "step" to default to 1, the default value.
    else:
        step = int(step)                            # Else condition: Assumes a number was input and uses the input instead of 1, the default value.
    
    lyst = []                                       # Empty list. A loop will send the start value and its increments to the list. Will contain the desired range.
    n = start                                       # Variable "n" is used to keep "start" pure.

    if step < 0:                                    # If/else statement to decide whether "myRange" will count upward or downward. Depends on the sign of "step".
        
        while n > stop:                             # While loop for counting downward. Loop continues until "n" increment is less than the boundary defined by "stop".
            lyst.append(n)                          # Adds "n" and each increment of "n" onto "lyst". Each "n" value is not added until the iteration after its definition.
            n = n + step                            # Increments "n" by the number defined by "step".
    else:
        
        while n < stop:                             # While loop for counting upward. Loop continues until "n" increment is greater than the boundary defined by "stop".
            lyst.append(n)                          # Adds "n" and each increment of "n" onto "lyst". Each "n" value is not added until the iteration after its definition.
            n = n + step                            # Increments "n" by the number defined by "step".

    return lyst                                     # Returns "lyst", the list of numbers in the range

def main():
    stop = input("Enter a stop value or press enter to exit program: ")         # Requests "stop" from the user. No input here ends program.
    
    while stop != "":                                                           # While loop to continue program until user terminates on "stop" input. Loop is entered when the first prompt for "stop" is not an empty string.
        
        start = input("Enter a start value or press enter for default: ")       # Requests "start" from the user. If/else statement within "myRange" will check for an empty string for default.
        step = input("Enter a step value or press enter for default: ")         # Requests "step" from the user. If/else statement within "myRange" will check for an empty string for default.
        print(myRange(int(stop), start, step))                                  # Calls myRange function with user's input(s) as arguments.
        stop = input("Enter a stop value or press enter to exit program: ")     # Requests "stop" from user. Loop will continue calling function to act on inputs until "stop" is an empty string.
        
if __name__ == '__main__':                                                      # Calls the main function and runs the program.
    main()
    
    