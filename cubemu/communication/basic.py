"""On-board communication module."""

import socket

READ_TEMP = 0
TAKE_PICTURE = 1
READ_POSITION = 2

commands = ['READ_TEMP', 'TAKE_PICTURE', 'READ_POSITION']

class Command(object):
    def __init__(self, code, target = None):
        self.code = code
        self.target = target
        self.conn = None

    def __str__(self):
        return str(commands[self.code]) + ' ' + str(self.target)


class DataPacket(object):
    def __init__(self, data):
        self.data = data

    def getSizeBytes(self):
        return 0

    def serialize(self):
        return self.data


class ConnectionHandler(object):
  """Handles communication with ground station."""

  def __init__(self):
    HOST = '0.0.0.0' # localhost'
    PORT = 3000
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((HOST, PORT))

  def _unparse(self, data):
    if data == 'TMP_READ':
      # XXX sensor name should be a param of the request
      return Command(READ_TEMP, 'temp1')
    elif data == 'TAKE_PICTURE':
      return Command(TAKE_PICTURE)
    elif data == 'POS_READ':
      return Command(READ_POSITION)
    else:
      print 'ERROR -- command unparse failed - not supported'
    return None

  def send(self, command, result):
    """This is our interface with the communications infrastructure."""
    if command.code == TAKE_PICTURE:
      f = open('filename.jpg')
      while 1:
        chunk = f.read(1024)
        if not chunk:
          break
        command.conn.send(chunk)
    else:
      command.conn.sendall(result)
    command.conn.close()

  def readCommandQueue(self):
    """Waits for a command from the ground station."""
    self.s.listen(1)
    conn, addr = self.s.accept()
    while 1:
      data = conn.recv(1024)
      if not data:
        break
      # XXX should merge data for large requests
      command = self._unparse(data)
      command.conn = conn
      return command
    return None
