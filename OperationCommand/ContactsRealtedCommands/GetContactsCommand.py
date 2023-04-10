from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface


class GetContactsCommand(CommandInterface):
      

    def execute(self):
      conatcts=  Storage.getContactsWithDetails()
      return conatcts