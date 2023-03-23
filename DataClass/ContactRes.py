from DataClass.Contact import Email
from DataClass.Contact import Address
from DataClass.Contact import PhoneNumbers

class ContactRes:
    def __init__(self,uid,name,email:list[Email],phone:list[PhoneNumbers],address:list[Address]):
        self.uid=uid
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address