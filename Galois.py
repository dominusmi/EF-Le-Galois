import serial
import sys
import os
from GPS import GPS
from threading import Thread
from time import sleep

## E/F Le Galois ##

## Boolean variable that will represent
## whether or not GPS connected

connected = False


## Main loop
while True:

    ## Catches KeyboardInterrupt
    try:

        if( connected == False ):
            device='/dev/ttyACM0'
            ser = None
            try:
                ## Sets ttyACM0 to baudrate 9600, and then tries to connect
                print 'Trying to connect to', device
                os.system('stty -F /dev/ttyACM0 9600')
                ser = serial.Serial(device, 9600)

                ## If no exception --> all goes well, set connected accordingly
                connected=True
            except:
                print "Failed to connect on",device
                sys.exit()

            ## Creates thread which handles writing GPS data to file
            if( connected ):
                try:
                    GPS = GPS(ser)
                except Exception as e:
                    print "Error on thread"
                    sys.exit()

        # No need to be constantly running
        sleep(0.1)

    except KeyboardInterrupt:
        print "Ah! KeyboardInterrupt!"
        ## Stops the thread
        GPS.stop()
        ## Clean exit
        sys.exit(0)
