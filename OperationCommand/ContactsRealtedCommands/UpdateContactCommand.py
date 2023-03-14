from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface

class UpdateContactCommand(CommandInterface):
    def __init__(self, contact_id, contact_data):
        self.contact_id = contact_id
        self.contact_data = contact_data

    def execute(self):
        updatedContact = Storage.updateContact(self.contact_id, self.contact_data)
        return updatedContact