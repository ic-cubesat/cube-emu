import serial
import time
import signal
import sys

ser = None

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    #target.close()
    ser.close()
    sys.exit(0)

def format_string(data):
    data_array = []
    data = str(data)
    data_len = len(data)
    #print data_len
    data_array.append(data)
    data_array_c = data_array[:]
    counter = 0
    split = data_len
    divider = 1
    while (len(data_array[0]) >= 18):
        counter += 1
        divider = counter*2
        split = data_len/divider
     #   print "Data" , data_array
        data_array_c = []
        for i in range(divider):
            print "Data Fragement" , data[(split*i):(split*(i+1))] , len(data[(split*i):(split*(i+1))])
            data_array_c.append(data[(split*i):(split*(i+1))])
        data_array = data_array_c[:]
    #print data_array
    #print split*divider,data_len
    if split*divider != data_len:
        data_array.append(data[(split*divider):])
    index = 0
    for content in data_array:
        #print "Content " , content
        if type(content) != str:
            print "Error - Content is not String!"
            return 0
        #print "T:S:" + content + "\n"
        #data_array[index] = "T:S:" + content + "\n"
        data_array[index] = "T:S:#" + content + "#\n"
        index += 1
    print data_array
    return data_array
def remove_four(data):
    return data[4:]

def strip_endline(data):
    s = ''
    for i in data:
        if i != '\n':
            s = s+i
    return s

def string_counter_format(data,counter):
    if counter < 10:
        return data[:5] + str(0) + str(counter) + data[5:]
    else:
        return data[:5] + str(counter) + data[5:]

def send_string(data_array):
    '''
    Sends a string
    '''
    ser.write("Starting")
    #print "Writing: "
    #time.sleep(0.01)
    for content in data_array:
        content_copy = content[:]
        confirmed = 0
        print "Resetting Times Sent"
        times_sent = 0
        while(confirmed == 0):
            content_copy = string_counter_format(content,times_sent)
            print "Increasing Times Sent"
            times_sent += 1
            print "SENDING " , content_copy
            ser.write(content_copy)
            #time.sleep(0.1)
            print "Checking for confirmation"
            time.sleep(0.1)
            confirm = ser.readline() # read one line
            if confirm != '' :
                confirm = strip_endline(confirm)
                print "Received: " , confirm, check(confirm) , check(remove_four(strip_endline(content_copy)))
                if confirm == str(check(remove_four(strip_endline(content_copy)))):
                    confirmed = 1
                print "1: " , confirmed,"2: " , confirm, type(confirm)   ,  "3: " ,content, check(content_copy), str(check(remove_four(content_copy)))
            #time.sleep(2)
    return data_array

def check(data):
    '''
    data is the input string to be checked!
    '''
    sum = 0
    for a in data:
        k = ord(a)
        sum += k
    return sum

def main():
  signal.signal(signal.SIGINT, signal_handler)
  time.sleep(1) #needed for some reason...

  serial_port = sys.argv[1]
  global ser
  ser = serial.Serial(serial_port, 57600, timeout = 0.1, interCharTimeout = None)
  print("connected to: " + ser.portstr)
  print "Initial Reading: ", ser.readline()
  time.sleep(0.2)
  data_array = format_string("1234567890")
  print "Data_array" , data_array, check(data_array[0])
  data = raw_input("Send?")
  if(data != '0'):
    send_string(data_array)
  ser.close()

if __name__ == '__main__':
  main()
