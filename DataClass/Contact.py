class Email:
    def __init__(self,type,email):
        self.type=type
        self.email=email

class Address:
    def __init__(self,type,address,):
         self.type=type
         self.address=address

class PhoneNumbers:
    def __init__(self,type,phone):
         self.type=type         
         self.phone=phone


class Contact:
    def __init__(self,name,email:list[Email],phone:list[PhoneNumbers],address:list[Address]):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address