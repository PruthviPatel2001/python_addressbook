class DisplayContact:
    def __init__(self, contact_res):
        self.uid = contact_res.uid
        self.name = contact_res.name
        self.email = contact_res.email
        self.phone = contact_res.phone
        self.address = contact_res.address
        
    def display(self):
        print(f"UID: {self.uid}")
        print(f"Name: {self.name}")

        for email in self.email:
            print(f"Email: {email.email}")
            print(f"Type: {email.type}")
        for phone in self.phone:
            print(f"Phone: {phone.phone}")
            print(f"Type: {phone.type}")

        for address in self.address:
            print(f"Address: {address.address}")
            print(f"Type: {address.type}")        
       
