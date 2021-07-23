# Put your code here

inputFile = input("Enter the input file name: ");
outputFile = input("Enter the output file name: ");


fExport = open(inputFile,'w');
fExport.write("Hello, I am new here.\nMy name is Lewis.");
fExport.close();


fExport = open(inputFile,'r');
for line in fExport:
    fImport = open(outputFile,'a');
    fImport.write(line);
fExport.close();
fImport.close();

fExport = open(inputFile,'r');
orgContents = fExport.read();
fImport = open(outputFile,'r');
newContents = fImport.read();
assert(orgContents == newContents);
fImport.close();
fExport.close();
print(orgContents);
print(newContents);




