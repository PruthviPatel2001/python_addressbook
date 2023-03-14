from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface
import uuid
class AddContactCommand(CommandInterface):
    def __init__(self, contact):
        self.id=uuid.uuid1()
        contact["id"]=self.id
        self.contact = contact
        

    def execute(self):
       StoredData= Storage.addContact(self.contact,self.id)

       return StoredData
        
  
