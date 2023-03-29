from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface
from DataClass.Contact import Contact
import uuid
class AddContactCommand(CommandInterface):
    def __init__(self, contact):
        
        self.contact = Contact(name=contact.name,email=contact.email,phone=contact.phone,address=contact.address)
        
        

    def execute(self):
       
       StoredData= Storage.addContact(self.contact)
       return StoredData
        
  
