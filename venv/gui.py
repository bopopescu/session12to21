from tkinter import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('raj.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#import session12
#from session12 import customer
#from  session12 import DBHelper
from session13 import *

# cRef = Session13.Customer("John", "+91 99999 88888", "john@example.com")
# cRef.showCustomerDetails()

def onClick():
    print("Button clicked")
    cref=customer(None,None,None)
    cref.name=enteryName.get()
    cref.phone=enteryPhone.get()
    cref.email=enteryEmail.get()
    cref.showCustomerDetails()

    data=cref.__dict__
    db.collection("customer").document().set(data)

    print(cref.name,"Saved")


    #db=DBHelper()
    #db.saveCustomerINDB(cref)

window=Tk()
lblTitle=Label(window,text="Add Customer Details")
lblTitle.pack()
lblName=Label(window,text="Add Customer Name")
lblName.pack()

enteryName=Entry(window)
enteryName.pack()
lblPhone=Label(window,text="Add Customer Phone")
lblPhone.pack()
enteryPhone=Entry(window)
enteryPhone.pack()
lblEmail=Label(window,text="Add Customer Email")
lblEmail.pack()
enteryEmail=Entry(window)
enteryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()
window.mainloop() #keep om running the program
