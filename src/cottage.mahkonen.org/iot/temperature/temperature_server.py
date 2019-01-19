#!/usr/bin/python
import serial
import io
import SimpleHTTPServer
import SocketServer
import json
import time

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        sio.write(unicode("A"))
        sio.flush()
        temperature = sio.read().strip()
        ret = {}
        ret['temperature'] = temperature
        ret['raw'] = int(time.time())
        # https://create.arduino.cc/projecthub/karimmufte/using-a-temp-sensor-with-arduino-tmp36-temperature-sensor-1e1d0b
        ret['celsius'] = float(temperature) * 0.48828125
        self._set_headers()
        self.wfile.write(json.dumps(ret))

def main():
    Handler = MyRequestHandler
    server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
