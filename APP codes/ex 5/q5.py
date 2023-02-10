import sqlite3


connection = sqlite3.connect('job_history.db')


sql_command = """ CREATE TABLE job_history (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    job_id INT(11) NOT NULL,
    department_id INT(11) NOT NULL
);
"""
connection.execute(sql_command)
connection.commit()


sql_command = """ INSERT INTO job_history
    VALUES(101, "2019-01-01", "2020-01-01", 101, 1);
"""
connection.execute(sql_command)


sql_command = """ INSERT INTO job_history
    VALUES(102, "2019-01-01", "2020-01-01", 102, 1);
"""
connection.execute(sql_command)

for i in connection.execute("SELECT * FROM job_history"):
    print(i)
