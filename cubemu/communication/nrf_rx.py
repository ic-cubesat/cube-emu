import serial
import signal
import sys
from time import gmtime, strftime

ser = serial.Serial(port='COM17', baudrate=57600, timeout=0, interCharTimeout = None)

print("connected to: " + ser.portstr)
count=0

def check(data):
    '''
    data is the input string to be checked!
    '''
    sum = 0
    for a in data:
        k = ord(a)
        sum += k
    return sum

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    ser.close()
    sys.exit(0)

def strip_endline(data):
    s = ''
    for i in data:
        if i != '\n':
            s = s+i
    return s

def strip(data):
    output = ''
    for i in range(len(data)):
        if data[i] != '#' and i>2:
            output = output + data[i]
    return output

signal.signal(signal.SIGINT, signal_handler)

received = []
receive = 1
while receive == 1:
    content = ser.readline()
    content = strip_endline(content)
    if content != '':
        print content
        if len(content) >= 3:
            if content[0] == '#' and content[-1] == '#':
                print "Writing ack" , content, str(check(content))
                received.append(content)
                ser.write("T:S:" + str(check(content)) + "\n")
                print "Done Writing"
                print received
                for i in range(len(received)):
                    received[i] = strip(received[i])
                print received

ser.close()
