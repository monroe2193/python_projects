#databases - contains many tables
#relation(table)- contains tuples and attributes
#tuple(row) - a set of fields that generally represent an object like a person or a music track
#attributes(also a column or field) - one of the many elemtents of data corresponding to object represented in the row

#Structured query language SQL (api between application and database)
#language we use to issue commands to database
#create a table
#retrieve some data
#update
#delete data
#C.R.U.D
#Application developer- creates the logic for the app, the look and feel of the app, moniters for problems
#database administrator -  moniters and adjusts the database
#developers create application software and stuff that the end user gets work with(writes code that talks sql with the database)

#database administrator(DBA) they talk to database
#database is both storage and software so it can take sql queries from many different sources (application or database tools)
#DBA runs commands straight to database
#developer has no acces to real database
#DBA way first where we use database browser to talk to the data base (by writing SQL and creating table and putting stuff in them

#basic pattern, read data.. clean it up.. stick it in the database in an organized way.. write other applications to make sense of it and analyz the data..

#database model/schema - contract describing the shape that we want the data
#database systems companies- oracle, mySQL, sqlserver
#sqllite designed to be real small
#

#single table C.R.U.D
#SQL codes
#INSERT INTO user(name,email) VALUES('Jason', 'triplej55@yahoo.com')
#DELETE FROM user WHERE email='triplej55@yahoo.com' #where is like an if statement, delete only rows that match the email adress
#UPDATE user SET name='Jorden Monroe' WHERE email='jorden_monroe@yahoo.com'
#SELECT * FROM user WHERE email='Jorden_monroe@yahoo.com' (will choose all rows and all columns that fit the where statement)
        ^ (list of columns)
#SELECT * FROM user ORDER BY name

#Joining the title from album and the name of the artist from artist where the foreign key= primary key (so they link up)
#select Album.title, Artist.name from Album JOIN Artist on Album.artist_id = Artist.id (can also use where instead of on)
#Joining the title from track and the name of the genre from genre where the foreign key= primary key (so they link up)
#select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id (can also use where instead of on)
#the on clause or where cluase specifies we want the ones that match
#without the on clause or where clause, it gives you all possible combinations

import sqlite3
connect = sqlite3.connect('trackdb.sqlite') #making a connection with sql database
curr = connect.cursor() #file handle like or in this case database handle
curr.executescript( '''
#write your SQL database code here and it will be done int the database;
seperate by semi colons between commands just like in execute sql box
''')


