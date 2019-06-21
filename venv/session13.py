"""
    DataBase : MySQL
    Prog Lang : SQL -> Structured Query Language
    Relational DataBase management System | RDBMS
    1. Create DataBase
        DataBase is collection of Tables
        Tables can be related to each other : 1 to 1 or 1 to many | has-a or is-a
    2. Create Table in DataBase
        Table is a collection of rows and columns eg: excel sheet
        ORM : Object Relational Mapping
        Your Object's Attributes should be Table's Column Names
        But in Table we can have 1 additional column and we call it as Primary Key and Auto Increment
        1 2 3 4 5 6....
        class Customer:
            def __init__(self, name, phone, email):
                self.name = name
                self.phone = phone
                self.email = email
        create table Customer(
            cid int primary key auto_increment,
            name varchar(256),
            phone varchar(20),
            email varchar(256)
        )
    3. Insert Data in Table
    cRef = Customer('John', '+91 99999 88888', 'john@example.com')
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')
    4. Install Library mysql-connector
    5. Create a DBHelper which will be accessing database
"""
import mysql.connector

class DBHelper:

    def saveCustomerINDB(self,Customer):
        sql="insert into customer values(null,'{}','{}','{}')".format(Customer.name,Customer.phone,Customer.email)
        con=mysql.connector.connect(user="root",password="",host="localhost",database="shop")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()

        print(Customer.name,"saved")

    def updateCustomerINDB(self, Customer):
        sql = "update customer set name='{}',phone='{}',email='{}' where cid='{}'".format(Customer.name, Customer.phone,
                                                                                        Customer.email, Customer.cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="shop")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(Customer.name,"updated")


    def deleteCustomerINDB(self, Customer):
        sql = "delete from customer where cid='{}'".format(Customer.cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="shop")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

    def fetchAllCustomers(self):
        sql="select * from customer"
        con = mysql.connector.connect(user="root", password="", host="localhost", database="shop")
        cursor = con.cursor()
        cursor.execute(sql)

        rows=cursor.fetchall()
        for row in rows:
            print(row)


    def fetchCustomer(self,cid):
        sql="select * from customer where cid='{}'".format(cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="shop")
        cursor = con.cursor()
        cursor.execute(sql)

        row=cursor.fetchone()
        print(row)


class customer:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def showCustomerDetails(self):
        print(">> Name:{} Phone:{} Email:{}".format(self.name,self.phone,self.email))
"""
print("Options:")
print("1. create new customer:")
print("2.Update data:")
print("3.Delete:")
print("4.Fetch all data")
choice=int(input("Enter choice:"))

if choice==1:
    cref=customer(None,None,None)
    cref.name=input("Enter customer name:")
    cref.phone=input("Enter customer phone:")
    cref.email=input("Enter customer email:")

    cref.showCustomerDetails()

    save = input("would you like to save(yes/no):")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerINDB(cref)
elif choice==2:
    db = DBHelper()
    cref = customer(None, None, None)
    cref.cid=input("Enter the customer Id:")
    db.fetchCustomer(cref.cid)
    cref.name = input("Enter customer name:")
    cref.phone = input("Enter customer phone:")
    cref.email = input("Enter customer email:")

    save = input("would you like to Update(yes/no):")
    if save == "yes":
        db = DBHelper()
        db.updateCustomerINDB(cref)
        cref.showCustomerDetails()


elif choice==3:
    cref = customer(None, None, None)
    cref.cid = input("Enter the customer Id:")
    save = input("would you like to Delete(yes/no):")
    if save=="yes":
        db = DBHelper()
        db.deleteCustomerINDB(cref)
        print(cref.cid, "deleted")
elif choice==4:
    db=DBHelper()
    db.fetchAllCustomers()
"""