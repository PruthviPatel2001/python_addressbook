
from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface

class SearchContactCommand (CommandInterface ): 
    def __init__ ( self , id ): 
        self.id = id

    def execute(self):
        contact_details = Storage.getContact(self.id)
        return contact_details
