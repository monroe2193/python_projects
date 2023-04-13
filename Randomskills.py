#RANDOM SKILLS FOR PYTHON SEPERATED BY COMMENTS>>>

x = open("Randomskills.py")
for index in x:
    print(index)
#searching through a file (prints out each line that starts with from)
#the print statement add a new line \n and the file line also have \n so you end up with a blank space
#line.rstrip() takes care of that
for line in x:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#opposite logic but same resulting print (skips lines that dont start with from and prints the rest)
for line in x:
    line = line.strip()
    if not line.startswith('From:'):
        continue
    print(line)

#looking for a string anywhere in a line (prints)
for line in x:
    line = line.strip()
    if not '@uct.ac.za' in line:
        continue
    print(line

#bad name filess
fname = input('Input file name')
try:
    file = open(fname)
except:
    print("Invalid file name", fname)
    quit()
count = 0
for line in file:
    if line.startswith('Subject:'):
        count = count + 1
print('There were ', count, "subject line in ", file)


#spelling out banana
fruit = 'banana'
#sending banana to uppercase
x = fruit.upper()

print(x)
index = 0
sum = 'I_want_a_'
while index < len(fruit):
    sum = sum + fruit[index]
    index = index + 1
print(sum)
count = 0

#counting letters in statement/word
statement = 'Hi my name is jorden, i go to florida atlantic university. I am going to graduate in the fall'
for letter in statement:
    if letter == 'a':
        count = count + 1
print(count)

x = statement.replace('florida', 'ass')
print(x)
y = statement.replace('i', 'w')
print(y)

#lstrip(), rstrip(), strip() strips the whitespace on either side of a string
word = '    stripping the whitespace     '
print(word.lstrip())
print(word.rstrip())
print(word.strip())

#startswith() library gives back true or false, takes into account spaces so watch out
print(word.startswith('p'))
print(word.startswith(''))
print(word.lstrip().startswith('s'))

#finding the slot from right after @ to .com and slicing it out (parsing and extracting)
sample = 'jorden_monroe@yahoo.com 20/30/22 715697:2022'
at = sample.find('@')
com = sample.find('.com', at)
slice = sample[at+1:com]
print(slice)

#6.5 assignment isolate 0.8475 and print
text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
end = text.find('5', start)
value = float(text[start:end+1])
print(value)
