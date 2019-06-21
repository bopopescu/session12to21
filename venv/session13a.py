from tkinter import *


#import session12
#from session12 import customer
#from  session12 import DBHelper
from session13 import *

# cRef = Session13.Customer("John", "+91 99999 88888", "john@example.com")
# cRef.showCustomerDetails()

def onClick():
    def ADD():
        cref.name = enteryName.get()
        cref.phone = enteryPhone.get()
        cref.email = enteryEmail.get()
        cref.showCustomerDetails()
        db = DBHelper()
        db.saveCustomerINDB(cref)
    def update():
        cref.cid=entryCID.get()
        cref.name = enteryName.get()
        cref.phone = enteryPhone.get()
        cref.email = enteryEmail.get()
        cref.showCustomerDetails()

        db = DBHelper()
        db.updateCustomerINDB(cref)
    def delete():
        cref.cid = entryCID.get()
        db = DBHelper()
        db.deleteCustomerINDB(cref)
        print(cref.cid,"deleted")
    print("Button clicked")
    if (i.get()==1):
        lblName = Label(window, text="Add Customer Name")
        lblName.pack()
        enteryName = Entry(window)
        enteryName.pack()
        lblPhone = Label(window, text="Add Customer Phone")
        lblPhone.pack()
        enteryPhone = Entry(window)
        enteryPhone.pack()
        lblEmail = Label(window, text="Add Customer Email")
        lblEmail.pack()
        enteryEmail = Entry(window)
        enteryEmail.pack()
        cref = customer(None, None, None)
        buttonADD=Button(window,text="ADD",command=ADD)
        buttonADD.pack()
    elif (i.get()==2):
        lblCID=Label(window,text="CID")
        lblCID.pack()
        entryCID=Entry(window)
        entryCID.pack()
        lblName = Label(window, text="Add Customer Name")
        lblName.pack()
        enteryName = Entry(window)
        enteryName.pack()
        lblPhone = Label(window, text="Add Customer Phone")
        lblPhone.pack()
        enteryPhone = Entry(window)
        enteryPhone.pack()
        lblEmail = Label(window, text="Add Customer Email")
        lblEmail.pack()
        enteryEmail = Entry(window)
        enteryEmail.pack()
        cref = customer(None, None, None)
        buttonADD = Button(window, text="ADD", command=update)
        buttonADD.pack()

    elif (i.get() == 3):
        lblCID = Label(window, text="CID")
        lblCID.pack()
        entryCID = Entry(window)
        entryCID.pack()
        cref=customer(None,None,None)
        buttondel = Button(window, text="DELETE", command=delete)
        buttondel.pack()


window=Tk()
i=IntVar()
r1 = Radiobutton(window, text="ADD Customer" ,value=1,variable=i)
r2 = Radiobutton(window, text="Update Data",value=2,variable=i)
r3 = Radiobutton(window,text="DELETE",value=3,variable=i)
r1.pack()
r2.pack()
r3.pack()



lblTitle = Label(window, text="Add Customer Details")
lblTitle.pack()
btnAddCustomer = Button(window, text="OK", command=onClick)
btnAddCustomer.pack()

window.mainloop() #keep om running the program
""""

    Phase-I
    CRUD Operations with GUI

    Phase-II
    Loyalty Points : 100 -> 1Point 1Re
    > Shopping Amount should be Entered
    > 2 : 3500 | 10Percent | 350+100 = 450
    > Check Loyalty Points
    > Redeem Loyalty Points
        shopping amount > 500
        in 1 billing only 150 can be redeemed maximum
"""