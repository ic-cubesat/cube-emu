""" These modules implement an emulator for the on-board systems """

import time

from communication import basic
from monitoring import sensors


def process(command):
    if command.code == basic.READ_TEMP:
        return sensors.read(command.target)
    return None


def pprint(string):
    print '{:10}'.format(string),


def main():

    while True:
        pprint('[CmdRead]')
        command = basic.readCommandQueue()
        print command

        if command:
            pprint('[Process]')
            result = process(command)
            print ' = ', result
            pprint('[Send]')
            basic.send(basic.DataPacket(result))
            pprint('[Sleep]')
            print '...'
            time.sleep(5)


if __name__ == '__main__':
    main()
