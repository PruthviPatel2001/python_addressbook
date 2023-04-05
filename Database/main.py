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
        session.query(Contact).filter(Contact.uid == uid).delete()
        session.commit()
        return self.uid

    def updateContactToDB(self):
        session.query(Contact).filter(
            Contact.uid == self.uid).update({Contact.name: self.name})
        session.commit()
        return self.uid


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

        emails = Email.getEmailsForConatct(uuid)

        session.query(Email).filter(Email.uid == uid).delete()
        session.commit()
        return emails
    
   
    def getEmailsForConatct(self,uid):
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
    
    def getAddressForContacts(self,uid):
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
        phoneNos=PhoneNumbers.getPhoneNosForContacts(uid)

        session.query(PhoneNumbers).filter(PhoneNumbers.uid==uid).delete()

        session.commit()
        
        return phoneNos
    
    def getPhoneNosForContacts(self,uid):
        phoneNos = []
        for phoneNo in session.query(Address).filter_by(uid=uid):
            phoneNos.append(phoneNo)
        return phoneNos


# To create all table from the class created above
Base.metadata.create_all(bind=engine)
