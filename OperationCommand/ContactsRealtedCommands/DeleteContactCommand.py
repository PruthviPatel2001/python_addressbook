from Storage.Storage import Storage
from Command.CommandInterface import CommandInterface


class DeleteContactCommand(CommandInterface):
    def __init__(self, id):
        self.id = id

    def execute(self):
      DeletedContact=  Storage.deleteContact(self.id)
      return DeletedContact

  