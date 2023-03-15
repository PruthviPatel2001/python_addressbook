
class Email:
    def __init__(self,email,type):
        self.email=email
        self.type=type

class Address:
    def __init__(self,address,type):
         self.address=address
         self.type=type

class PhoneNumbers:
    def __init__(self,phone,type):
         self.phone=phone
         self.type=type         


class Contact:
    def __init__(self,name,email:list[Email],phone:list[PhoneNumbers],address:list[Address]):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address