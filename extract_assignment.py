import re
fhandle = open('regex_sum_1733495.txt')
lst = list()
y = re.findall("[0-9]+", fhandle.read())
for i in y:
    lst.append(i)
sum = 0
for i in lst:
    sum = sum + float(i)
print("The sum is", sum)

