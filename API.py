from typing import Union
import uuid
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from AddressBook import AddressBookOperations
from Database.main import Contact


app = FastAPI()

class Email(BaseModel):
    type: str
    email: str


class Address(BaseModel):
    type: str
    address: str


class PhoneNumbers(BaseModel):
    type: str
    phone: str

# Define the request data model
class ContactReq(BaseModel):
    name: str
    email: List[Email]
    phone: List[PhoneNumbers]
    address: List[Address]


# Define the response data model
# class ContactRes(BaseModel):
#     uid: str
#     name: str
#     email: List[Email]
#     phone: List[PhoneNumbers]
#     address: List[Address]

@app.get("/contacts")
async def get_all_contacts():

    contacts = AddressBookOperations.getAllContacts()

    return contacts

@app.get("/contacts/{contact_id}")
async def get_contact(contact_id: str):

    contact = AddressBookOperations.searchContact(contact_id)

    return contact



@app.post("/contacts")
async def add_contact(contact_req: ContactReq):

    addedContact = AddressBookOperations.addContact(contact_req)

    return addedContact


@app.delete("/contacts/{conatct_id}")
async def delete_contact(conatct_id: str):

    deleted_contact = AddressBookOperations.deleteContact(conatct_id)

    return deleted_contact


@app.put("/contacts/{conatct_id}")
async def update_contact(conatct_id: str, contact_req: ContactReq):

    updated_contact = AddressBookOperations.updateContact(
        conatct_id, contact_req)

    return updated_contact



