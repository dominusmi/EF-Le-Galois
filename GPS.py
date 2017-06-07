from time import sleep, time
from threading import Thread
import datetime

class GPS:

    th = None

    def __init__(self, ser):

        self.lat    = 0
        self.long   = 0
        self.alt    = 0



        ## Variables to do with the
        ## Thread that reads serial and saves necessary information
        self.last_received = ''
        self.stopped = False
        self.th = Thread(target=self.serial_thread, args=(ser,))
        self.th.start()


    def format_data(self):
        data_array = self.last_received.split(",")

        if( data_array[0] == "$GPGGA"):
            f1 = open('GPS_dump.txt', 'a')
            f1.write(str(datetime.timedelta(seconds=time()))+' '+self.last_received)
            f1.close()

            self.lat    = data_array[2]
            self.long   = data_array[3]
            self.alt    = data_array[7]



    def serial_thread(self, ser):
        thread_round = 0
        while not self.stopped:
            self.last_received = ser.readline()

            self.format_data()



            thread_round+=1
            if( thread_round == 4 ):
                print self.last_received
                thread_round = 0
                sleep(0.2)
            # buffer += ser.read(ser.inWaiting())
            # if '\n' in buffer:
            #     last_received, buffer = buffer.split('\n')[-2:]


    def stop(self):
        self.stopped = True
