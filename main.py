
from AddressBook import AddressBookOperations


def main():
    contactOne = {
        "name": "Pruthvi",
        "age": 21,
        "phone": 1234567890,
    }
    contactTwo = {
        "name": "Jeet",
        "age": 21,
        "phone": 9876543210,
    }
#  ----------- Adding Contact to List ----------------
    addedContactOne=AddressBookOperations.addContact(contactOne)
    addedContactTwo=AddressBookOperations.addContact(contactTwo)

    print("Contact Added: \n",addedContactOne["id"])
    print("Contact Added: \n",addedContactTwo)

#  ----------- Deleting Contact from List ----------------
    deletedContactOne=AddressBookOperations.deleteContact(addedContactOne["id"])

    print("Contact Deleted sucessfully: \n",deletedContactOne)

#  ----------- Updating Contact in List ----------------
    contactOne["name"]="Pruthvi Patel"
    updatedContactOne=AddressBookOperations.updateContact(addedContactOne["id"],contactOne)
    
    print("Contact Updated sucessfully: \n",updatedContactOne)

#  ----------- Search Contact from List ----------------

    searchTerm ="Pruthvi Patel" 
    searchResult=AddressBookOperations.searchContact(searchTerm)

    print("Contact Found: \n",searchResult)


   



if __name__ == "__main__":
    main()
