#dictionaries (data structure) collection, just like a list is a collection
#bag of values, each with its own label
#label = key
#other names:associative array, hash maps, property bags
#memory based, key calued stores
#examples
purse = dict()
purse['money'] = 12 #money is the key, 12 is the value, putting it into purse, but storing it under the key name 'money'
purse['candy'] = 3 #key name- candy
purse['tissues'] = 75 #key name - tissues
#so inside of purse we have
print(purse)
# {'money': 12, 'candy': 3, 'tissues': 75}
#to pull something out
print(purse['candy'])
#3

#we index the things we want to store with a lookup tag
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
#5

purse['candy'] = 100
print(purse['candy'])
#100

#you can make a dictionary from scratch
jjj = {'money': 12, 'candy': 3, 'tissues': 75}

names = dict()
names['jorden'] = 1
names['jeff'] = 1
names['jorden'] = names['jorden'] +1
print(names)
# start a running tally, like a histogram  {'jorden': 2, 'jeff': 1}

#makes new keys with count 1, then upadates the count when it finds copies of the name
counts = dict()
names = ['jeff', 'jorden', 'sally', 'fred', 'jorden', 'sally', 'fred', 'fred']
for name in names:
    if not name in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#Alternate get method
counts = dict()
names = ['jeff', 'jorden', 'sally', 'fred', 'jorden', 'sally', 'fred', 'fred']
for name in names:
    counts[name] = counts.get(name, 0) +1
print(counts)
#get is a "method" for dictionaries
#go look up in counts, get the key value, and put 0 as the default if it doesnt exist
# get method - If there's no key in the dictionary, put it in. If there is a key in the dictionary, do something to the existing value that's already there

x = counts.get(name, 0)

#splits then counts each word using a dictionary
dick = dict()
x = 'in this moment of orangutans, wolves, and scavengers,\
    of high heat redesigning the north & south poles\
    and the wanderings of new tribes in limousines,'\

words = x.split()
for word in words:
    dick[word] = dick.get(word, 0) + 1
bigword = None
bigcount = None
for k,v in dick.items():
    if bigword is None or bigcount < v:
        bigword = k
        bigcount = v
print(bigword , bigcount)


#prints the key names as list
#print(list(dick))
#keys method prints the keys as list
#print(dick.keys())
#values method prints the values as list
#print(dick.values())
#items method prints the pairs as "tuples", key and value
#print(dick.items())

#prints the pairs k-key v-value are easy as iteration variables
for k,v in dick.items():
    print(k,v)
