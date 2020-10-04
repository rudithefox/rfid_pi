#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime
import time
import logging
from influxdb import InfluxDBClient

datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
continue_reading = True

# Connecting to InfluxDB and using 'Logins' database
client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='********')
client.switch_database('Logins')

u1 = {
    "name":"Michael",
    "UID": (76,130,171,164),
    "Log Status": False,
    "Time": datetime.datetime.now()
    }

u2 = {
    "name":"Rudi",
    "UID": (67,141,77,30),
    "Log Status": False,
    "Time": datetime.datetime.now()
    }

users = (u1,u2)

# Stops the script upon no feedback.
def end_read(signal,frame):
    global continue_reading
    print "Stopping. Ctrl+C captured"
    continue_reading = False
    GPIO.cleanup()

# Logs to file and InfluxDB.
def logs(user, log_status):
    # Logging to file
    logging.basicConfig(filename='cardReader.log', filemode='a',level=logging.DEBUG)
    logging.info('========================')
    logging.info('User: ' + user)
    logging.info('UID: %s,%s,%s,%s' % (uid[0], uid[1], uid[2], uid[3]))
    logging.info(datetime.datetime.now())
    logging.info(log_status)
    logging.info('========================')
    # Logging to InfluxDB.
    influx_insert_json = [
        {
            "measurement": "logEvent",
            "tags": {
                "user": user
            },
            "time": datetime.datetime.now(),
            "fields": {
                "user": user,
                "status": log_status,
                "uid": "%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
            }
        }
    ]
    client.write_points(influx_insert_json)
    print "Records created successfully";

# Prints details to terminal, uses logs function, waits 3 seconds.
def user_auth(user, log_status):
    print "-------------------------------"
    print "User: " + user
    print "Logged In: " + log_status
    print "Card UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    print "Time:",
    print(datetime.datetime.now())
    print "-------------------------------"
    logs(user, log_status)
    time.sleep(3)
    return;

# SIGINT HOOK
signal.signal(signal.SIGINT, end_read)

# Create an object of the MFRC522 class.
MIFAREReader = MFRC522.MFRC522()

# Create a message to confirm awaiting input.
print "Awaiting Login. Press Ctrl+C to cancel"

# Create a loop to to get input, wait then get input again.
while continue_reading:

    # Scan RFID Card
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Verify users by looping.
        user = ""
        for u in users:
            if (uid[0], uid[1], uid[2], uid[3]) == u["UID"]:
                user = u["name"]
                # Find and toggle Login Status
                if u["Log Status"] == False:
                    u["Log Status"] = True
                    log_status = "Logged In"
                    user_auth(user, log_status)
                else:
                    u["Log Status"] = False
                    log_status = "Logged Out"
                    user_auth(user, log_status)
        if user == "":
            print "============================================"
            print "UID not recognised"
            print "============================================"
            time.sleep(3)
