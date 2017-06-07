from time import sleep, time
from threading import Thread
import datetime

class GPS:

    th = None

    def __init__(self, ser):

        self.lat    = 0
        self.lat_i  = '' ## N or S
        self.long   = 0
        self.long_i = '' ## E or W
        self.alt    = 0
        self.v      = 0  ## In km/h



        ## Variables to do with the
        ## Thread that reads serial and saves necessary information
        self.last_received = ''
        self.stopped = False
        self.th = Thread(target=self.serial_thread, args=(ser,))
        self.th.start()

    def exctract_data(self):
        data_array = self.last_received.split(",")
        print data_array

        if( data_array[0] == "$GPGGA"):
            f1 = open('GPS_dump.txt', 'a')
            f1.write(str(datetime.timedelta(seconds=time()))+' '+self.last_received)
            f1.close()

            self.lat    = data_array[2]
            self.lat_i  = data_array[3]
            self.long   = data_array[4]
            self.long_i = data_array[5]
            self.alt    = data_array[9]

        if( data_array[0] == "$GPVTG"):
            f1 = open('GPS_dump.txt', 'a')
            f1.write(str(datetime.timedelta(seconds=time()))+' '+self.last_received)
            f1.close()

            self.heading= data_array[1]
            self.v      = data_array[7]


    def serial_thread(self, ser):
        thread_round = 0
        while not self.stopped:
            self.last_received = ser.readline()

            self.exctract_data()



            thread_round+=1
            if( thread_round == 4 ):
                thread_round = 0
                sleep(0.2)
            # buffer += ser.read(ser.inWaiting())
            # if '\n' in buffer:
            #     last_received, buffer = buffer.split('\n')[-2:]


    def stop(self):
        self.stopped = True
