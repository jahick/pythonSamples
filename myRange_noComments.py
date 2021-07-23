
# File: testmyrange.py
# Project 6.10
# Defines a function that behaves like Python's range function.


def myRange (stop, start = 0, step = 1):            
                                                        
    if start == "" or start == None:                
        start = 0
    else:
        start = int(start)
    if step == "" or step == None or step == 0:
        step = 1
    else:
        step = int(step)
    
    lyst = []
    n = start

    if step < 0:
        while n > stop:
            lyst.append(n)
            n = n + step
    else:
        while n < stop:
            lyst.append(n)
            n = n + step

    return lyst

def main():
    stop = input("Enter a stop value or press enter to exit program: ")
    
    while stop != "":
        
        start = input("Enter a start value or press enter for default: ")
        step = input("Enter a step value or press enter for default: ")
        print(myRange(int(stop), start, step))
        stop = input("Enter a stop value or press enter to exit program: ")
        
if __name__ == '__main__':
    main()
    
    