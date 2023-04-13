
#Write a program to read through the mbox-short.txt and figure out
#who has sent the greatest number of mail messages. The program
#looks for 'From ' lines and takes the second word of those lines
#as the person who sent the mail. The program creates a Python
#dictionary that maps the sender's mail address to a count of the
#number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum
#loop to find the most prolific committer.


name = input("Enter file:")
handle = open(name)
blackbook = dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    words = line.split()
    address = words[1]
    blackbook[address] = blackbook.get(address, 0) + 1

addresskey = None
addresscount = None
for key,value in blackbook.items():
    if addresskey is None or addresscount < value:
        addresskey = key
        addresscount = value
print(addresskey, addresscount)
