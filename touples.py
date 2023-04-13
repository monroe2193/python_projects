# tuples are exactly like lists in the way that they are indexed like starting at 0
a = (1, 2, 3, 4, 5, 6, 7)
friends = ('joseph', 'sally', 'jorden')
print(a[0])
#1
print(max(friends))
#sally
for num in a:
    print(num)
# 1 2 3 4 5 6 7

#unlike lists they are immutable
#so a[2]= 15 will traceback\
x = tuple()
print(dir(x))
# we can put tuples on the left hand lide of an assignment statement
(a,b) = (4, 'fred')
print(a)
print(b)

#double indexed for loops must be used with tuples
#we did this when we iterated k,v over dictionary.items() because items() for dictionaries returns tuples

#tuples are comparable for truth statements
#only takes one vvv
#(1,2,3) < (1,0,5)
#True bc 3<5
#(joe, sally) < (joe,sam)
#true bc l<m so sally < sam

#we can take advantage of the items function to turn a dictionary into a tupled list so then we can use sorted()
d = {'a': 1, 'c': 7, 'b': 2, 'e':6 }
print(d.items())
#dict_items([('a', 1), ('c', 7), ('b', 2), ('e', 6)])
print(sorted(d.items()))
#[('a', 1), ('b', 2), ('c', 7), ('e', 6)]
for k,v in d.items():
    print(k,v)
for k,v in sorted(d.items()):
    print(k,v)
#how do we sort by value?
lst = list()
for k,v in d.items():
    lst.append((v,k))
#sorted naturally sdoes min to max
lst = sorted(lst)
print(lst)
#to print from max to min
lst = sorted(lst, reverse = True)
print(lst)


fhandle = "Open the file mbox-short.txt and read it line by line. When you find a line that starts with From  like the following line: \
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 \
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. \
Hint: make sure not to include the lines that start with From:. Also look at the last line of the sample output to see how to print the count."
dictionary = dict()
for line in fhandle:
    words = line.split()
    print(words)
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
lst = list()
for k,v in dictionary.items():
    newtuple = (v,k)
    lst.append(newtuple)
sortedlist = sorted(lst, reverse=True)
print(sortedlist[:10])

#even shorter version of 64-67
sortedlist = sorted([ (v,k) for k,v in dictionary.items()], reverse=True)
