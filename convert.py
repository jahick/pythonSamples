# Put your code here
decimal = int(input("Enter an integer: "));
base = int(input("Enter a base number to convert to. (2, 8, 10, 16): "));

def decimalToRep(decimal,base):
    if base == 10:
        return decimal;
    elif base == 2:
        return str(bin(decimal)[2:]);
    elif base == 8:
        return oct(decimal)[2:];
    elif base == 16:
        hexString = hex(decimal)[2:];
        return hexString.upper();
    else:
        print("Please choose a valid base. (2, 8, 10, 16)");

# A main for testing your program
def main():
    """Tests the function."""
   
    print("")

    print("Testing:")
    print(decimalToRep(10, 10));
    print(decimalToRep(10, 8));
    print(decimalToRep(10, 2));
    print(decimalToRep(10, 16));
    
    print("");
    
    print("Real:")
    print(decimalToRep(decimal,base));

# The entry point for program execution
if __name__ == "__main__":
    main();
