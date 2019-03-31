#!/usr/bin/python3
import serial
import io
import json
import time

from kafka import KafkaProducer

# Read temperature
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
sio.write(str("A"))
sio.flush()
temperature = sio.read().strip()

# Encode JSON object
reading = {}
reading['raw'] = temperature
reading['time'] = int(time.time())
# https://create.arduino.cc/projecthub/karimmufte/using-a-temp-sensor-with-arduino-tmp36-temperature-sensor-1e1d0b
reading['raw'] = temperature
reading['celsius'] = float(temperature) * 0.48828125
reading['farenheit'] =  1.8 * reading['celsius'] + 32.0;

# Publish to Kafka topic
producer = KafkaProducer(bootstrap_servers='mahkonen.org:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
future = producer.send('cottage.mahkonen.org.temperature', reading)
result = future.get(timeout=60)
print(result)
