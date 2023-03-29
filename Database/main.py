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
    
    def deleteContactFromDB(self):
        session.query(Email).filter(Email.uid == self.uid).delete()
        session.commit()
        return self.uid
    
    def updateContactToDB(self):
        session.query(Contact).filter(Contact.uid == self.uid).update({Contact.name: self.name})
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
    
    def deleteEmailFromDB(self):
        session.delete(self)
        session.commit()
        return self.uid


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
    
    def deleteAddressFromDB(self):
        session.delete(self)
        session.commit()
        return self.uid


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
    
    def deletePhoneFromDB(self):
        session.delete(self)
        session.commit()
        return self.uid


# To create all table from the class created above
Base.metadata.create_all(bind=engine)


# c1 = Contact("Pruthvi Patel")
# session.add(c1)
# session.commit()

# e2 = Email(c1.uid, "work", "Pruthvi@vayana.com")
# session.add(e2)
# session.commit()

# a1 = Address(c1.uid, "personal", "Vaodara")
# a2 = Address(c1.uid, "work", "Ahmedabad")

# p1 = PhoneNumbers(c1.uid, "personal", 1234567890)
# p2 = PhoneNumbers(c1.uid, "work", 9876543210)


# print(session.query(Contact).all())
# session.add(e2)
# session.add(p1)
# session.add(p2)
# session.add(a1)
# session.add(a2)
