# ------------------------------------- V2 runnable -------------------------------------

from AddressBook import AddressBookOperations

from DataClass.ContactReq import ContactReq
from DataClass.Contact import Email,Address,PhoneNumbers
from Displaydata.Display import DisplayContact

# reqOne = ContactReq(
#     "Pruthvi Patel",
#     [Email("personal","pruthvi@gmail.com"),Email("work","pruthvi@vayana.com")],
#     [PhoneNumbers("personal","1234567890",),PhoneNumbers("work","9876543210")],
#     [Address("personal","Vaodara"),Address("work","Ahmedabad")]
# )

reqTwo = ContactReq(
    "Dinesh Patel",
    [Email("personal","Dinesh@gmail.com"),Email("work","Dinesh@vayana.com")],
    [PhoneNumbers("personal","874578653",),PhoneNumbers("work","987454786")],
    [Address("personal","vadodara"),Address("work","surat")]
)


# addContactOne=AddressBookOperations.addContact(reqOne)

addContactTwo=AddressBookOperations.addContact(reqTwo)



displayContact= DisplayContact(addContactTwo)

print("Contact Added: \n",displayContact.display())