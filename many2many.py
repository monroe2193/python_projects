#Many to many relationships in SQL
#foreign key has many tracks points to one album that has the primary key( many2one) most common
#many to many example author has wtritten several books and books may have several authors
#to model a many to many we need a 'connection' table with two foreign keys
#you decompose the relationship into 2 seperate many to one relationships

#course to user
#  course table        Member table                    user table
#  id       <<<<       course_id                       name
#  title                user_id        >>>>>>           id
#                                                      email
#(member table used to construct many to many)
#

#CREATE TABLE User (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#name TEXT,
#email TEXT
#)
#CREATE TABLE Course (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#title TEXT
#)
#CREATE TABLE Member (
#user_id INTEGER,
#course_id INTEGER,
#role INTEGER,
#PRIMARY KEY ( (user_id, course_id)
#)
#
#INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
#INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
#INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');
#INSERT INTO Course (title) VALUES ('Python');
#INSERT INTO Course (title) VALUES ('SQL');
#INSERT INTO Course (title) VALUES ('PHP')
#;
#INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
#INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
#INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
#INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
#INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
#INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
#INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
#
#SELECT User.name, Member.role, Course.title
#FROM User JOIN Member JOIN Course
#ON Member.user_id = User.id AND Member.course_id = Course.id
#ORDER BY Course.title, Member.role DESC, User.name
