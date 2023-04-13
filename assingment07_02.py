# reading through a file, finding the lines that start with X-DSPAM-Confidence:
#counting the number of line
#finding where the number starts and ends
#parsing the line to take only the number, turning it into a float, and adding them all together
# then printing the average which is sum/count
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    num_start = line.find('.')
    num_end = line.find(' ', num_start)
    value = line[num_start - 1: num_end]
    value = float(value)
    total = total + value

print("Average spam confidence:", total/count)
