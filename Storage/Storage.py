import uuid


class Storage:
    contactList = {}

    @staticmethod
    def addContact(contact, id):
        Storage.contactList[id] = contact
        return Storage.contactList[id]

    @staticmethod
    def deleteContact(id):
        dataToBeDeleted = Storage.contactList.get(id)
        Storage.contactList.pop(id)
        return dataToBeDeleted
    
    @staticmethod
    def updateContact(id,contact):
        Storage.contactList[id]=contact
        return Storage.contactList[id]

    @staticmethod
    def getContact(searchTerm):
        
        contactsKey=[]
        resultedContacts = []

        for key, value in Storage.contactList.items():
            if searchTerm in value.values():
                contactsKey.append(key)

        for key in contactsKey:
            resultedContacts.append(Storage.contactList.get(key))       

        return resultedContacts        
            


