#asks for file saves as handle, opens as variable, loops cuts the newline indicators(non ptniting characters)
#counts the lines in the file, and prints every line as all upper case
fhandle = input('Enter file name:')
file = open(fhandle)
count = 0
for line in file:
    line = line.rstrip()
    count = count + 1
    print(line.upper())
print('There are ', count, 'lines in ', file)

