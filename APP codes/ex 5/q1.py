import sqlite3

connection = sqlite3.connect('recipe.db')

sql_command = """ CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(400) NOT NULL,
    description TEXT,
    category_id INT(11) NOT NULL,
    chef_id INT(11) NOT NULL,
    created DATETIME
);
"""
connection.execute(sql_command)

sql_command = """ INSERT INTO recipes
    VALUES(1, "Noodles", "Chinese", 1, 'BL000002', "2020-01-01");
"""

connection.execute(sql_command)

sql_command = """ INSERT INTO recipes
    VALUES(2, "Chowmein", "Chinese", 2, 'BL000005', "2020-01-01");
"""

connection.execute(sql_command)

# pasta
sql_command = """ INSERT INTO recipes
    VALUES(3, "Pasta", "Italian", 3, 'BL000003', "2020-01-01");
"""

connection.execute(sql_command)

ans1 = connection.execute(
    "SELECT COUNT(*) FROM recipes WHERE description = 'Chinese'")

ans2 = connection.execute(
    "SELECT id, name FROM recipes WHERE chef_id = 'BL000002'")

ans3 = connection.execute(
    "SELECT description FROM recipes WHERE name LIKE 'P%'")

connection.commit()

# print name

for i in ans1:
    print(i)
for i in ans2:
    print(i)
for i in ans3:
    print(i)
