import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "melika1380"
)
mycursor = mydb.cursor()



sql = "CREATE DATABASE shop3"
mycursor.execute(sql)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "melika1380",
    database = "shop3"
)
mycursor = mydb.cursor()




# Create the category table
sql = """
       CREATE TABLE category (
       category_id int not null AUTO_INCREMENT,
       category_name VARCHAR(255),
       PRIMARY KEY (category_id)
       );
    """
mycursor.execute(sql)




sql = """
        CREATE TABLE Products(
        product_id int NOT NULL AUTO_INCREMENT,
        product_name varchar(255),
        category_id int NOT NULL,
        price int,
        quantity int,
        PRIMARY KEY (product_id),
        FOREIGN KEY (category_id) REFERENCES category (category_id)
        );
    """
mycursor.execute(sql)


#insert


sql = "INSERT INTO category ( category_id , category_name) values (1, 'Electronics'),(2, 'Books'),(3, 'Clothes'); "
mycursor.execute(sql)
mydb.commit()


sql = "INSERT INTO Products (PRODUCT_id,product_name , category_id , price , quantity) values (1, 'Laptop', 1, 500, 10),  (2, 'Mouse', 2, 10, 50),  (3, 'Keyboard', 2, 15, 40),  (4, 'Monitor', 3, 100, 20),  (5, 'Printer', 3, 150, 15);"
mycursor.execute(sql)
mydb.commit()


#Remove 

sql = "DELETE FROM Products WHERE product_id = 1 "
mycursor.execute(sql)

sql = "DELETE FROM Category WHERE category_id = 2"
mycursor.execute(sql)


#edit
sql = "SELECT * FROM Products"
mycursor.execute(sql)
mycursor.fetchall()

sql = """
        UPDATE Products SET price = 1.5 * price
    """
mycursor.execute(sql)
mydb.commit()

#Search Entries
sql = "SELECT * FROM Products WHERE product_name = Printer"
mycursor.execute(sql)
mycursor.fetchall()


#Display 
sql = "SELECT product_name FROM Products"
mycursor.execute(sql)
mycursor.fetchall()

sql = "SELECT category_name FROM Category"
mycursor.execute(sql)
mycursor.fetchall()







