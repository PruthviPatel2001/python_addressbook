from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()


engine = create_engine(
    "postgresql+psycopg2://pruthvip:password@localhost:5433/addressbook", echo=True)


Session = sessionmaker(bind=engine)
session = Session()


class Contact(Base):
    __tablename__ = 'contacts'

    uid = Column("uid", UUID(as_uuid=True),
                 primary_key=True, default=uuid.uuid4)
    name = Column("name", String)

    def __init__(self, name):
        self.name = name

    def addContactToDB(self):
        session.add(self)
        session.commit()
        return self.uid

    def deleteContactFromDB(self, uid):
        contact = Contact.getContactName(uid)
        session.query(Contact).filter(Contact.uid == uid).delete()
        session.commit()
        session.close()
        return contact
    
    def updateContactInDB(self,uid):
        print("check",self.name)
        session.query(Contact).filter(
            Contact.uid == uid).update({Contact.name: self.name})
        session.commit()
        return self.uid
    
    def getContactName(uid):
        contact = session.query(Contact).filter_by(uid=uid).first()
        if contact is not None:
            return contact.name
        else:
            return None
        
    def getContactsWithDetails():
         result = []

         contacts = []
         for contact in session.query(Contact).all():
            contact_dict = {
                "uid": str(contact.uid),
                "name": contact.name,
                "emails": [],
                "addresses": [],
                "phoneNumbers": []
            }

            for email in Email.getEmailsForContact(contact.uid):
                email_dict = {"type": email.type, "email": email.email}
                contact_dict["emails"].append(email_dict)

            for address in Address.getAddressForContacts(contact.uid):
                address_dict = {"type": address.type, "address": address.address}
                contact_dict["addresses"].append(address_dict)

            for phone in PhoneNumbers.getPhoneNosForContact(contact.uid):
                print("----------here-------------:",phone.type)
                phone_dict = {"type": phone.type, "phone": phone.phone}
                contact_dict["phoneNumbers"].append(phone_dict)

            contacts.append(contact_dict)

         return contacts

        #  for contact in session.query(Contact).all():
        #     emails = Email.getEmailsForContact(contact.uid)
        #     addresses = Address.getAddressForContacts(contact.uid)
        #     phoneNumbers = PhoneNumbers.getPhoneNosForContacts(contact.uid)

        #     contact_dict = {
        #         "uid": str(contact.uid),
        #         "name": contact.name,
        #         "emails": [{"type": email.type, "email": email.email} for email in emails],
        #         "addresses": [{"type": address.type, "address": address.address} for address in addresses],
        #         "phoneNumbers": [{"type": phone.type, "phone": phone.phone} for phone in phoneNumbers]
        #     }

        #     result.append(contact_dict)

         return result


class Email(Base):
    __tablename__ = 'emails'
    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uid = Column("uid", ForeignKey("contacts.uid"))
    type = Column("type", String)
    email = Column("email", String)

    def __init__(self, uid, type, email):

        self.uid = uid
        self.type = type
        self.email = email

    def addEmailToDB(self):
        session.add(self)
        session.commit()
        return self.uid

    def deleteEmailFromDB(self,uid):

        emails = Email.getEmailsForContact(uid)

        session.query(Email).filter(Email.uid == uid).delete()
        session.commit()
        return emails
    
    def updateEmailInDB(self,uid):
        session.query(Email).filter(
            Email.uid == uid).update({Email.type: self.type, Email.email: self.email})
        session.commit()
        session.close()

        return self.uid
    
   
    def getEmailsForContact(uid):
        emails = []
        for email in session.query(Email).filter_by(uid=uid):
            emails.append(email)
        return emails



class Address(Base):
    __tablename__ = 'addresses'
    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uid = Column("uid", ForeignKey("contacts.uid"))
    type = Column("type", String)
    address = Column("address", String)

    def __init__(self,  uid, type, address):

        self.uid = uid
        self.type = type
        self.address = address

    def addAddressToDB(self):
        session.add(self)
        session.commit()
        return self.uid

    def deleteAddressFromDB(self,uid):

        addresses = Address.getAddressForContacts(uid)
        session.query(Address).filter(Address.uid == uid).delete()
        session.commit()
        return addresses
    
    def updateAddressInDB(self,uid):
        session.query(Address).filter(
            Address.uid == uid).update({Address.type: self.type, Address.address: self.address})
        session.commit()
        session.close()

        return self.uid
    
    def getAddressForContacts(uid):
        addresses = []
        for address in session.query(Address).filter_by(uid=uid):
            addresses.append(address)
        return addresses


class PhoneNumbers(Base):
    __tablename__ = 'phonenumbers'
    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uid = Column("uid", ForeignKey("contacts.uid"))
    type = Column("type", String)
    phone = Column("phone", String)

    def __init__(self, uid, type, phone):
        self.uid = uid
        self.type = type
        self.phone = phone

    def addPhoneToDB(self):
        session.add(self)
        session.commit()
        return self.uid

    def deletePhoneFromDB(self,uid):
        phoneNos=PhoneNumbers.getPhoneNosForContact(uid)

        session.query(PhoneNumbers).filter(PhoneNumbers.uid==uid).delete()

        session.commit()

        return phoneNos
    
    def updatePhoneInDB(self,uid):
        session.query(PhoneNumbers).filter(
            PhoneNumbers.uid == uid).update({PhoneNumbers.type: self.type, PhoneNumbers.phone: self.phone})
        session.commit()
        session.close()

        return self.uid
    
    def getPhoneNosForContact(uid):
        phoneNos = []
        for phoneNo in session.query(PhoneNumbers).filter_by(uid=uid):
            phoneNos.append(phoneNo)
        return phoneNos


# To create all table from the class created above
Base.metadata.create_all(bind=engine)
