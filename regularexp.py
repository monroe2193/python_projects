#regular expressions
import re
#fname = input('enter file name:')
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
#this does the exact same thing as
    if line.startswith('From:'):
        print(line)

#re.search() like .startswith() carrot or hat character '^' says at the beginning of the line
#so '^From' means F should be the first character then rom
# ^
# . is any character
# * means zero or more (anynumber of times)
# so ^X.*: means lines that start with X, followed by some # of characters, followed by a colon.
# so lines that match might be
# X-SAM2193:
# X-box playboard:
# XRated Films:

#to be more precise
# so ^X-\S+: means Starts with X, then dash, \S followed by any non-white space character, "+" 1 or more times, followed by a colon
#new results out of the three
# X-SAM2193:

x = 'my dog is 6 years old i got him on the 23rd of last month i rescued him 30 days ago'
y = re.findall('[0-9]+', y)
print(y)
# gives us a list of all matches ['6', '23','30'] POWERFULL
y = re.findall('[AEIOU]+', y)
# [] since there are no uppercase vowels

# ^F.*?:     ^F first character F, .* any number of symbols, ? not greedy so smallest match, followed by colon:

x = 'From: jorden_monroe@yahoo.com 20/30/22 715697:2022'
#\S+@\S+ \S+ one or more non-white space character, followed by @, \S+ one or more non-white space character
y = re.findall('\S+@\S+', x)
print(y)
# ['jorden_monroe@yahoo.com']

# @([^ ]*)    () extract this part, [] any single character,  [^] everything but, [^ ] everything but blank space,
# [^ ]*  everything but blank space any number of times
y = re.findall('@([^ ]*)', x)
print(y)
# ['yahoo.com']

#does the same thing
y = re.findall('^Find .*@([^ ]*)', x)
print(y)
# ['yahoo.com']

lst = list()
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM_Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    lst.append(num)
print('Maximum', max(lst))

# \ means we are really looking for the next character that comes after it, since we might need to find a character that meas something else in this language
x = 'we just recieved $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y)
# ['$10.00']

#^ Matches the beginning of a line
#$ Matches the end of the line

# . Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# + Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end
