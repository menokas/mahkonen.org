#!/usr/bin/python3
import serial
import MySQLdb
import time

class Collect():
    def __init__(self, device="/dev/ttyUSB0", baudrate=9600):
        self.device = device
        self.baudrate = baudrate
        self.s = serial.Serial(self.device, self.baudrate)

    def read(self):
        return self.s.readline()

if __name__ == "__main__":
    print ("Collect sensor data")
    collector = Collect()
    db = MySQLdb.connect("localhost","root","pw4root","iot")
    cursor = db.cursor()

    # Create table as per requirement
    #sql = """CREATE TABLE IF NOT EXISTS TEMPERATURE (ID INT AUTO_INCREMENT NOT NULL, TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, RAW_READING INT, TEMPERATURE FLOAT, PRIMARY KEY(ID))"""
    #cursor.execute(sql)
    try:
        while True:
            reading = int(collector.read())
            # https://create.arduino.cc/projecthub/karimmufte/using-a-temp-sensor-with-arduino-tmp36-temperature-sensor-1e1d0b
            value = reading * 0.48828125
            print ("Data: {} ({})".format(reading, value))
            sql = "INSERT INTO TEMPERATURE (RAW_READING, TEMPERATURE) VALUES ('{}', '{}')".format(reading, value)
            print (sql)
            cursor.execute(sql)
            db.commit()
            # Sleep for 10 minutes
            time.sleep(600)
    except: 
        print("Exception")
    db.close()

