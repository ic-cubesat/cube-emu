import serial
import time
import signal
import sys

#test = 146
data = '0'

ser = serial.Serial('COM16', 57600, timeout = 0.1, interCharTimeout = None)
print("connected to: " + ser.portstr)

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    #target.close()
    ser.close()
    sys.exit(0) 

signal.signal(signal.SIGINT, signal_handler)
#data = raw_input("Send stuff?")
#if(data != '0'):
    #ser.write(data)
    #ser.write(test)
time.sleep(1) #needed for some reason...

#f = open('C:\Users\Alex\Dropbox\CubeSat Project\Systems Eng\Comm\NRF24 Code and Library\Python TX code\image.jpeg' , 'rb')
#contents = f.read()
#data_len = len(contents)
#print "Data Length" , data_len
#print len(contents)
#contents = contents
#print len(contents)

#f_2 = open('C:\Users\Alex\Dropbox\CubeSat Project\Systems Eng\Comm\NRF24 Code and Library\Python TX code\image_bytes_sent.jpeg' , 'wb')

def confirm_receive(serial_port,sent_data):
    i = 0
    while(1):
        tdata = serial_port.read(1)
        if(tdata == sent_data):
            return True
        else:
            i = 1
            if (i == 1):
                return False
            
def readdata(serial_port,data_size):
    tdata = serial_port.read(data_size)
    if(len(tdata) > 0):
        #print tdata
        return tdata
        
def echo(port, byte):
    port.write(str(byte))
    return readdata(port,10)     
    
def send_file(port, data):
    packet_length = 1 #number of bytes to transmit at a time
    length = int(len(data) / packet_length)
    for i in range(length): 
        to_send = data[i*packet_length:(i*packet_length)+packet_length]
        print i, to_send
        port.write(to_send)
        #f_2.write(to_send)
        #f_2.flush()
        time.sleep(0.1)
        if(confirm_receive(port,to_send)):
            print i, "Packet Confirmed!"
        else:
            print i, "Not confirmed!"
            break
    if((len(contents) % packet_length) != 0):
        print "Writing remainder", i, (len(data) % packet_length) , data[i:(i+(len(data) % packet_length))]
        to_send  = data[i:(i+(len(data) % packet_length))]  
        port.write(to_send)
        #f_2.write(to_send)
        #f_2.flush()  

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

print "Initial Reading: ", ser.readline()
time.sleep(0.2)
data_array = format_string("1234567890")
print "Data_array" , data_array, check(data_array[0])

#send_string(data_array)

data = raw_input("Send?")
if(data != '0'):
    send_string(data_array)
ser.close()
print"Done"  
