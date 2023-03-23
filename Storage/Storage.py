import uuid
from Database.main import Contact,Email,Address,PhoneNumbers

from DataClass.ContactRes import ContactRes

class Storage:
    contactList = {}

    @staticmethod
    def addContact(contact):
        uid=1
        Storage.contactList[uid] = contact


        addContactName = Contact(name=contact.name)
        ContactUUID=addContactName.addContactToDB()

        for i in range(len(contact.email)):
            addContactEmail= Email(uid=ContactUUID,type=contact.email[i].type,email=contact.email[i].email)
            addContactEmail.addEmailToDB()

        for i in range(len(contact.phone)):
            addContactPhone= PhoneNumbers(uid=ContactUUID,type=contact.phone[i].type,phone=contact.phone[i].phone)
            addContactPhone.addPhoneToDB()
            
        for i in range(len(contact.address)):
            addContactAddress= Address(uid=ContactUUID,type=contact.address[i].type,address=contact.address[i].address)
            addContactAddress.addAddressToDB()       


        
        return ContactRes(uid=ContactUUID,name=contact.name,email=contact.email,phone=contact.phone,address=contact.address)

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
            


