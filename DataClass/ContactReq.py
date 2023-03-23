from DataClass.Contact import Email
from DataClass.Contact import Address
from DataClass.Contact import PhoneNumbers

class ContactReq:
    def __init__(self,name,email:list[Email],phone:list[PhoneNumbers],address:list[Address]):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address