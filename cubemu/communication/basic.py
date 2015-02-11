"""On-board communication module."""

READ_TEMP = 0

commands = ['READ_TEMP']


class Command(object):
    def __init__(self, code, target):
        self.code = code
        self.target = target

    def __str__(self):
        return str(commands[self.code]) + ' ' + str(self.target)


class DataPacket(object):
    def __init__(self, data):
        self.data = data

    def getSizeBytes(self):
        return 0

    def serialize(self):
        return self.data


def send(dataPacket):
    """This is our interface with the communications infrastructure."""
    print dataPacket.serialize()


def readCommandQueue():
    """Returns the first command in the command queue."""
    return Command(READ_TEMP, 'temp1')
