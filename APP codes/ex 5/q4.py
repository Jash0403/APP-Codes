import sqlite3

connection = sqlite3.connect('job.db')

sql_command = """ CREATE TABLE job (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title VARCHAR(400) NOT NULL,
    Min_salary INT(11) NOT NULL,
    Max_salary INT(11) NOT NULL
);
"""
connection.execute(sql_command)
connection.commit()

sql_command = """ INSERT INTO job
    VALUES(101, "Software Engineer", 100, 200);
"""
connection.execute(sql_command)

sql_command = """ INSERT INTO job
    VALUES(102, "Software Architect", 300, 500);
"""
connection.execute(sql_command)

sql_command = """ INSERT INTO job
    VALUES(103, "Software Developer", 400, 600);
"""
connection.execute(sql_command)

for i in connection.execute("SELECT * FROM job"):
    print(i)
