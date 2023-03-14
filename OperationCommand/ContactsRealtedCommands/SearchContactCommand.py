
from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface

class SearchContactCommand (CommandInterface ): 
    def __init__ ( self , contact_name ): 
        self . contact_name = contact_name

    def execute(self):
        contact_details = Storage.getContact(self.contact_name)
        return contact_details
