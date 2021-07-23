decimal, base = map(int, input("Enter the decimal, then the base, separated by a comma. ").split(','));

repTable = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 :'4',
5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',
14 : 'E', 15 : 'F'};

def decimalToRep(decimal,base):
    if decimal == 0:
        return "0";
    elif base == 10:
        return str(decimal);
    elif base == 2:
        return str(bin(decimal)[2:]);
    else:
        rep = ""
        while decimal > 0:
            remainder = decimal % base;
            decimal = str(decimal // base);
            rep = str(decimal + repTable[remainder]);
            if rep[0] == '0':
                rep_NoZero = rep[1:];
                return str(rep_NoZero);
            else:
                return rep;

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
    print(str(decimalToRep(decimal,base)));

if __name__ == "__main__":
    main();
