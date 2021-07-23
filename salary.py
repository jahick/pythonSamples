# Inputs

startingSalary = float(input("Enter the starting salary: $"));
annualPercentageIncrease = float(input("Enter the annual % increase: "));
annualIncrease = float(annualPercentageIncrease / 100); #converting percent into decimal
yearsOfExperience = int(input("Enter the number of years: "))


# Table 

print("Year   Salary");
print("-------------");
print("%2d%11.2f" % (1,startingSalary));


# Loop

for year in range(2,yearsOfExperience + 1):
    startingSalary = float(startingSalary + (startingSalary * annualIncrease));
    print("%2d%11.2f" % (year,startingSalary));
