# Put your code here
import random

inputFile = input("Enter the input file name: ");
outputFile = input("Enter the output file name: ");

fExport = open(inputFile,'w');
fExport.write("Hello, I am new here.\nMy name is Lewis.");
fExport.close();


fExport = open(inputFile,'r');
fImport = open(outputFile,'a');
for line in fExport:
    fImport.write(line);
fExport.close();
fImport.close();


fImport = open(outputFile,'r');
text = fImport.read();
print(text);
fImport.close();

