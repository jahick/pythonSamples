print("Calculator for weekly pay.");
print(" ");

# Inputs
hourlyWage = float(input("Enter the wage...$"));
regularHours = float(input("Enter the regular hours..."));
overtimeHours = float(input("Enter the overtime hours..."));

# Calculations
regularPay = float(hourlyWage * regularHours);
overtimePay = float(overtimeHours * 1.5 * hourlyWage);
totalWeeklyPay = float(regularPay + overtimePay);

#Display
print("The total weekly pay is $",totalWeeklyPay);
