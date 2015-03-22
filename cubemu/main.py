""" These modules implement an emulator for the on-board systems """

import time

from communication import basic
from monitoring import sensors
from camera import webcam


def process(command):
    if command.code == basic.READ_TEMP:
        return str(sensors.read(command.target))
    elif command.code == basic.TAKE_PICTURE:
        return webcam.takePicture()[0]
    elif command.code == basic.READ_POSITION:
        return str(sensors.getPosition())
    return None


def pprint(string):
    print '{:10}'.format(string),


def main():

    connhandler = basic.ConnectionHandler()

    while True:
        print "Waiting for command..."
        pprint('[CmdRead]')
        command = connhandler.readCommandQueue()
        print command

        if command:
          pprint('[Process]')
          result = process(command)
          print ' = ', result
          pprint('[Send]')
          connhandler.send(command, result)
          pprint('[Sleep]')
          print '...'
          time.sleep(5)


if __name__ == '__main__':
    main()
