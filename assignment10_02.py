#assignment10_02
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
handle = open(name)
hourcount = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) < 5:
        continue
    time = words[5]
    splt_time = time.split(':')
    hour = splt_time[0]
    hourcount[hour] = hourcount.get(hour, 0) + 1
lst = list()
sortedlst = sorted([(k,v) for k,v in hourcount.items()])
for k,v in sortedlst:
    print(k,v)
