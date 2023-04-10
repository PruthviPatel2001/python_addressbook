import uuid
from Database.main import Contact, Email, Address, PhoneNumbers

from DataClass.ContactRes import ContactRes


class Storage:
    contactList = {}

    @staticmethod
    def addContact(contact):
        uid = 1
        Storage.contactList[uid] = contact

        addContactName = Contact(name=contact.name)

        # TO GET UUID OF CONTACT FROM MAIN CLASS
        ContactUUID = addContactName.addContactToDB()

        for i in range(len(contact.email)):
            addContactEmail = Email(
                uid=ContactUUID, type=contact.email[i].type, email=contact.email[i].email)
            addContactEmail.addEmailToDB()

        for i in range(len(contact.phone)):
            addContactPhone = PhoneNumbers(
                uid=ContactUUID, type=contact.phone[i].type, phone=contact.phone[i].phone)
            addContactPhone.addPhoneToDB()

        for i in range(len(contact.address)):
            addContactAddress = Address(
                uid=ContactUUID, type=contact.address[i].type, address=contact.address[i].address)
            addContactAddress.addAddressToDB()

        return ContactRes(uid=ContactUUID, name=contact.name, email=contact.email, phone=contact.phone, address=contact.address)

    @staticmethod
    def deleteContact(id):
        # dataToBeDeleted = Storage.contactList.get(id)
        # Storage.contactList.pop(id)

        uid = uuid.UUID(id)

        deleteContactEmail = Email(uid="", type="", email="")
        deleteContactEmail.deleteEmailFromDB(uid)

        deleteContactAddress = Address(uid="", type="", address="")
        deleteContactAddress.deleteAddressFromDB(uid)

        deleteContactPhone = PhoneNumbers(uid="", type="", phone="")
        deleteContactPhone.deletePhoneFromDB(uid)

        deleteContactName = Contact(name="")
        deleteContactName.deleteContactFromDB(uid)

        return {
            "name": deleteContactName,
            "emails": deleteContactEmail,
            "address": deleteContactAddress,
            "phoneNumber": deleteContactPhone
        }

    @staticmethod
    def updateContact(id, contact):
        # Storage.contactList[id] = contact
        uid = uuid.UUID(id)

        updateContactName = Contact(name=contact.name)
        updateContactName.updateContactInDB(id)

        for i in range(len(contact.email)):
            updateContactEmail = Email(
                uid=uid, type=contact.email[i].type, email=contact.email[i].email)
            updateContactEmail.updateEmailInDB(id)

        for i in range(len(contact.phone)):
            updateContactPhone = PhoneNumbers(
                uid=uid, type=contact.phone[i].type, phone=contact.phone[i].phone)
            updateContactPhone.updatePhoneInDB(id)

        for i in range(len(contact.address)):
            updateContactAddress = Address(
                uid=uid, type=contact.address[i].type, address=contact.address[i].address)
            updateContactAddress.updateAddressInDB(id)

        return ContactRes(uid=id, name=contact.name, email=contact.email, phone=contact.phone, address=contact.address)

    @staticmethod
    def getContact(searchTerm):

        contact = Contact.getContactName(searchTerm)
        emails = Email.getEmailsForContact(searchTerm)
        phones = PhoneNumbers.getPhoneNosForContact(searchTerm)
        addresses = Address.getAddressForContacts(searchTerm)

        return ContactRes(uid=searchTerm, name=contact, email=emails, phone=phones, address=addresses)


    @staticmethod
    def getContactsWithDetails():
        contacts = Contact.getContactsWithDetails()
        return contacts