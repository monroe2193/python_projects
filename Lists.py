for i in [1,2,3,4,5]:
    print(i)

#different ways to index
friends = ['joseph', 'sally', 'jorden']
for i in friends:
    print(i)
for friend in friends:
    print('Happy New Year', friend, '!')
for i in range(3):
    print(friends[i])
for i in range(len(friends)):
    print(i)


#changing list objects
friends[2] = 'jeffery'
print(friends)
#length of friends
print(len(friends))

#concatenating lists (doesnt change a or b)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#slicing lists
#whole list
slice1 = a[:]
#items in slot 1 and 2
slice2 = a[1:3]
#slot 1 till end
slice3 = a[1:]
#etc

x = list()
print(dir(x))

#create empty list
list_ex = list()
list_ex.append('go')
list_ex.append('fuck')
list_ex.append('yourself')
print(list_ex)

#checking if something is in the list "in" ad "not in" opperators
a= [1, 2, 3, 4, 5, 6, 7]
print(3 in a)
#true
print(8 in a)
#false
print(3 not in a)
#false

#sort funtion "sort yourself" will go to alphabetical order
friends = ['joseph', 'sally', 'jorden']
friends.sort()
print(friends)

#functions
a= [1, 2, 3, 4, 5, 6, 7]
print(sum(a))
#28
print(max(a))
#7
print(min(a))
#1
print(len(a))
#7 (count)
print(sum(a)/len(a))
#4 (average)

#creates list to be filled by input, finishes when 'done', finds average, displays average
numlist = list()
#while True:
#    x = input("Enter a number:")
#    if x == 'done': break
#    try:
#        x = float(x)
#        numlist.append(x)
#    except:
#        print('Not a valid input')
#average = sum(numlist)/len(numlist)
#print ('The average is', average)

#split() splits strings into segmented parts in a list
string1 = "what's up jorden"
list1 = string1.split()
print(list1)
print(len(list1))
print(list1[0])
for i in list1:
    print(i)

#split by a different delimiter ; instead of ' ' (it chops strings by whatever parameter you want)
string1 = "what's;up;jorden"
list1 = string1.split(;)

#finding date through mailing list of things that look like  "From Jorden@yahoo.com sat 10 20 22"
#finds line that start with from, skips the rest, splits it by the spaces into a list
#print the stuff in space 2 to get the day
fhand = open(mbox.txt)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[2])
#sat...and so on

#Double splitting "From jorden_monroe@yahoo.com saturday 10 22 34"
#split bys spaces, isolates email, split email by '@', puts into a list of pieces
words = line.split()
email = words[1]
pieces = email.split(@)
print(pieces)
#['jorden_monroe', 'yahoo.com']



