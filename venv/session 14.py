import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class customer:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def showCustomerDetails(self):
        print(">> Name:{} Phone:{} Email:{}".format(self.name,self.phone,self.email))
# Use a service account
cred = credentials.Certificate('raj.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
"""
cref=customer("RAJ","+91 98786 54356","imcoolrajeev9226@gmail.com")
data=cref.__dict__
db.collection("customer").document().set(data)
print(cref.name,"saved")
"""
docs = db.collection("customer").stream()

for doc in docs:
    print(doc.id, doc.to_dict())