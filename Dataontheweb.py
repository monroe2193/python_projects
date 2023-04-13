#Exchanging data betweens programs using the request and response html cylcle
# we came up with an agreed way to represtent data and goin between networks and accross networks
#Two common formats,  XML and JSON
#wire protocol --->
#python dictionary ----> send accross network ---> to another system, say java hashmap
#                      ^^^ wire protocol^^^
#We cant just send python data or java data we need to come up with an agreed format
# Xml is one of the wire formats agreed upon
#take the data that is in a python dictionary ---> say, info on a person name phone # ect.. ---> send it
# agreed on format that is just text
# serialization is the process of putting the data on the wire
# deserializing it is taking it off the wire
#python dictionary--> serialize--> <3615859305> < jorden monroe> --> deserialize --> java hash map

#XML ******
#serialization format
#rules you have start tags and end tags
# <people> (outer tag)
#     <person>
#        <name>Jorden</name>
#        <phone>3615859305></phone>
#     </person>
#     <person>
#        <name>DanelyToress</name> #nodes  (text content is danely torres)
#        <phone>3615859305></phone> #nodes
#     </person>
# </people> (outer tag)

# simple elements - name, phone
#complex elements - person, people
# <start> tag and </end> tag have same name
# self closing tabs look like    <email hide="yes"/>    (attribute is hide="yes")
# attributes are KEY="STRING"  attributes are key value pairs on the opening tag
#always an outer tag

#serialization is taking and internal structure tranforming it into an agreed upon format and sending it down the wire
#deserialization is taking the agreed upon data off the wire and turning it into an its own readable data
# nodes
#you have the outaer tag thats the parent node at top of tree, then splits into child nodes, and the texts within is a child node of the child nodes
#attributes are also children node from the tag they are held within

#must have double quotes for the value of attributes

#XML SCHEMA
# describes the legal format of xml
#Validation is the act of verifying the data is in the right format

#DATE/TIME format   1993-02-01T08:00:35Z  year-month-dayThour:min:secZ   Z is time zone

#PARSING XML IN PYTHON
import xml.etree.ElementTree as ET
data = '''
<person>
  <name>chuck</name>
    <phone type="intl">
      +1 361-585-9305
    </phone>
    <email hide="yes"/>
</person>'''
# ''' means "theres a multiline string inside of it"
tree = ET.fromstring(data) #fromstring takes the string we pass into it and turns it into a tree
print('Name:', tree.find('name').text) #finds name on tree ,prints the text between the name tags or text node
print('Attr:', tree.find('email').get('hide')) #finds email on tree and gets the hide attribute, prints yes

input = ''' <stuff> 
  <users>
    <user x="2">
       <id>009</id>
       <name>Brent</name>
    </user>
    <user x="7">
       <id>001</id>
       <name>chuck</name>
    </user>
  </users>
</stuff>'''
stuff = ET.fromstring(input) #creates tree in python
lst = stuff.findall('users/user') # under users there are user tags, find all puts them in a list. list of 2 user treeslst
print('user count:', len(lst)) #prints size of list/ number of users
for tag in lst: #iterates through the list of trees
    print('Name', tag.find('name').text) #finds name child node and gets text
    print('Id', tag.find('id').text) #finds id tag under user and and gets text
    print('Attribute', tag.find('user').get("x")) #gets attrbute values from x key

