from OperationCommand.ContactsRealtedCommands.AddContactCommand import AddContactCommand
from OperationCommand.ContactsRealtedCommands.DeleteContactCommand import DeleteContactCommand
from OperationCommand.ContactsRealtedCommands.UpdateContactCommand import UpdateContactCommand
from OperationCommand.ContactsRealtedCommands.SearchContactCommand import SearchContactCommand
from Storage.Storage import Storage

class AddressBookOperations:
    
    def addContact(contact):
         command =  AddContactCommand(contact)
         createdContact=command.execute()
         return createdContact
    
    def deleteContact(id):
        command = DeleteContactCommand(id)
        deletedContact=command.execute()
        return deletedContact
    
    def updateContact(id,contact):
        command = UpdateContactCommand(id,contact)
        updatedContact=command.execute()
        print("Name",contact.name)
        return updatedContact
    
    def searchContact(searchTerm):
        command = SearchContactCommand(searchTerm)
        contact= command.execute()
        return contact
    
    def getAllContacts():
        return Storage.contactList

