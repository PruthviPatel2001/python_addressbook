import unittest
from AddressBook import AddressBookOperations



class TestAddressBook(unittest.TestCase):

    def test_add_contact(self):
        address_book = AddressBookOperations()
        contactThree = {
        "name": "Xyz",
        "age": 21,
        "phone": 9876543210,
    }
        addeddContact=AddressBookOperations.addContact(contactThree)
        getcontact = AddressBookOperations.searchContact("Xyz")
        self.assertEqual(addeddContact, getcontact[0])

    def test_remove_contact(self):
        address_book = AddressBookOperations()
        contactThree = {
        "name": "Xyz",
        "age": 21,
        "phone": 9876543210,
    }
        addeddContact=AddressBookOperations.addContact(contactThree)
        deletedContact=AddressBookOperations.deleteContact(addeddContact["id"])
        self.assertEqual(deletedContact, addeddContact)  

    def test_update_contact(self):
        address_book = AddressBookOperations()
        contactThree = {
        "name": "Xyz",
        "age": 21,
        "phone": 9876543210,
    }
        addeddContact=AddressBookOperations.addContact(contactThree)
        contactThree["name"]="Xyz Patel"
        updatedContact=AddressBookOperations.updateContact(addeddContact["id"],contactThree)
        self.assertEqual(updatedContact, contactThree)    

    def test_search_contact(self):
        address_book = AddressBookOperations()
        contactThree = {
        "name": "Pruthvi",
        "age": 21,
        "phone": 9876543210,
    }
        addeddContact=AddressBookOperations.addContact(contactThree)
        searchResult=AddressBookOperations.searchContact("Pruthvi")
        
        self.assertEqual(searchResult[0], addeddContact)      


if __name__ == '__main__':
    unittest.main()
   
