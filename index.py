# ------------------------------------- V2 runnable -------------------------------------

from AddressBook import AddressBookOperations

from DataClass.ContactReq import ContactReq
from DataClass.Contact import Email,Address,PhoneNumbers
from Displaydata.Display import DisplayContact

reqOne = ContactReq(
    "Pruthvi Patel",
    [Email("personal","pruthvi@gmail.com"),Email("work","pruthvi@vayana.com")],
    [PhoneNumbers("personal","1234567890",),PhoneNumbers("work","9876543210")],
    [Address("personal","Vaodara"),Address("work","Ahmedabad")]
)



addContactOne=AddressBookOperations.addContact(reqOne)


displayContact= DisplayContact(addContactOne)

print("Contact Added: \n",displayContact.display())