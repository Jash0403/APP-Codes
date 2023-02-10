import sqlite3
connection = sqlite3.connect('course.db')

sql_command = """ CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prod_name VARCHAR(400) NOT NULL,
    supplier_id INT(11) NOT NULL,
    unit_price INT(11) NOT NULL,
    package VARCHAR(400) NOT NULL,
    order_id INT(11) NOT NULL
);
"""

connection.execute(sql_command)
connection.commit()
sql_command = """ CREATE TABLE orderitem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    unit_price INT(11) NOT NULL,
    quantity INT(11) NOT NULL,
    FOREIGN KEY (id) REFERENCES product(id),
    FOREIGN KEY (order_id) REFERENCES product(order_id)
);
"""
connection.execute(sql_command)
connection.commit()


sql_command = """ INSERT INTO product
    VALUES(101, "Flutter", 19, 10, "App Dev", 1);
"""
connection.execute(sql_command)


sql_command = """ INSERT INTO product
    VALUES(102, "Ionic", 21, 20, "Web Dev", 2);
"""
connection.execute(sql_command)


sql_command = """ INSERT INTO product
    VALUES(103, "SQL", 12, 30, "Backend", 3);
"""
connection.execute(sql_command)


sql_command = """ INSERT INTO orderItem
    VALUES(101, 1, 1, 10, 14);
"""
connection.execute(sql_command)


sql_command = """ INSERT INTO orderItem
    VALUES(102, 2, 2, 20, 22);
"""
connection.execute(sql_command)

ans1 = """ SELECT product_id, quantity FROM orderItem
    GROUP BY product_id;
"""
for i in connection.execute(ans1):
    print(i)

ans2 = connection.execute("SELECT * FROM product ORDER BY supplier_id")
for i in ans2:
    print(i)

ans3 = connection.execute(
    "SELECT prod_name, order_id, supplier_id FROM product")
for i in ans3:
    print(i)
