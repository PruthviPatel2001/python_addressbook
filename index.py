# ------------------------------------- V2 runnable -------------------------------------

from AddressBook import AddressBookOperations
from DataClass.ContactReq import ContactReq
from DataClass.ContactRes import ContactRes
from Database.main import Contact
from DataClass.Contact import Email,Address,PhoneNumbers
from Displaydata.Display import DisplayContact

reqOne = ContactReq(
    "Pruthvi Patel",
    [Email("personal","pruthvi@gmail.com"),Email("work","pruthvi@vayana.com")],
    [PhoneNumbers("personal","1234567890",),PhoneNumbers("work","9876543210")],
    [Address("personal","Vaodara"),Address("work","Ahmedabad")]
)

reqTwo = ContactReq(
    "Dinesh Patel",
    [Email("personal","Dinesh@gmail.com"),Email("work","Dinesh@vayana.com")],
    [PhoneNumbers("personal","874578653",),PhoneNumbers("work","987454786")],
    [Address("personal","vadodara"),Address("work","surat")]
)



# ---- ADD CONTACT----

addContactOne=AddressBookOperations.addContact(reqOne)

# addContactTwo=AddressBookOperations.addContact(reqTwo)


# displayContact= DisplayContact(addContactTwo)

# print("Contact Added: \n",displayContact.display())

# ------ DELETE CONTACT ---- 
# deleteContact=AddressBookOperations.deleteContact("2ea555ff-a3b2-4ba6-8f5c-5f6c74a5240f")
# print("Deleted Contact",deleteContact)

# ---- UPADE CONTACT ----

# reqTwo.name="Dinesh"
# updateContact=AddressBookOperations.updateContact("4b6bd41a-fee8-43bd-8c12-d0a16d4a409c",reqTwo)
# displayContact= DisplayContact(updateContact)

# print("Contact Added: \n",displayContact.display())


# ---- Get all Contacts ---- 
getContacts = Contact.getContactsWithDetails()

print("All Contacts: \n",getContacts)

