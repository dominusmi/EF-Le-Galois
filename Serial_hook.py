from time import sleep, time
from threading import Thread

class Serial_hook:

    th = None

    def __init__(self, ser):
        self.ser = ser
        self.last_received = ''
        self.stopped = False
        self.th = Thread(target=self.receiving, args=())

        self.th.start()

    def stop(self):
        self.stopped = True

    def receiving(self):
        thread_round = 0
        while not self.stopped:
            self.last_received = self.ser.readline()

            f1 = open('GPS_dump.txt', 'a')
            f1.write(str(time())+' '+self.last_received)
            f1.close()

            thread_round+=1
            if( thread_round == 4 ):
                print self.last_received
                thread_round = 0
                sleep(0.2)
            # buffer += ser.read(ser.inWaiting())
            # if '\n' in buffer:
            #     last_received, buffer = buffer.split('\n')[-2:]
