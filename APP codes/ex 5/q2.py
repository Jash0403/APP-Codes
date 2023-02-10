import sqlite3

connection = sqlite3.connect('movie.db')


sql_command = """ CREATE TABLE movie (
    Movie_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Movie_Name VARCHAR(400) NOT NULL,
    Genre VARCHAR(400) NOT NULL,
    Language VARCHAR(400) NOT NULL,
    Rating VARCHAR(400) NOT NULL
);
"""
connection.execute(sql_command)
connection.commit()

sql_command = """ INSERT INTO movie
    VALUES(101, "The Avengers", "Action", "English", "2");
"""
connection.execute(sql_command)

sql_command = """ INSERT INTO movie
    VALUES(102, "The Batman", "Action", "English", "3.5");
"""
connection.execute(sql_command)

sql_command = """ INSERT INTO movie
    VALUES(103, "Spiderman", "Action", "English", "3");
"""
connection.execute(sql_command)

sql_command = """ UPDATE movie
    SET Rating = Rating * 1.1;
"""

connection.execute(sql_command)

sql_command = """ DELETE FROM movie
    WHERE Movie_ID = 102;
"""

connection.execute(sql_command)

for i in connection.execute("SELECT * FROM movie"):
    print(i)

print("Movie Rating greater than 3")

ans = connection.execute("SELECT * FROM movie WHERE Rating > 3")
for i in ans:
    print(i)
