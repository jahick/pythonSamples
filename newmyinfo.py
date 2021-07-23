import re

isNameValid = False

while isNameValid == False:
    name = str(input("Enter your name..."));

    regex = r"[0-9]";
    match = re.search(regex,name,re.MULTILINE);

    if match != None:
        print("Invalid name. Name cannot contain numbers.");
    else:
        isNameValid = True;

isAgeValid = False;

while isAgeValid == False:

    try:
        age = int(input("Enter your age..."));
       
        if age < 0:
            print("Invalid age. Age must be at least 0.");
        else:
            isAgeValid = True;
    except:
        print("Invalid age. Age must be a whole number.");

    
print (name,"is",age,"years old.");
