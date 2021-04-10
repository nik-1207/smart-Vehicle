import serial

import sys 

import time

import requests

import http.client as http_client

http_client.HTTPConnection.debuglevel = 1

Webhost = 'http://dcs.glaitm.org:7080'

App_key = '9fb4f6fa-b295-4e9d-8059-198be086dad9'

ThingName1 = 'EvehicleThing'

ThingName2 = 'EVsensor'

P1 = 'CarStatus'

P2 = 'Front'

P3 = 'FrontLeft'

P4 = 'FrontRight'

P5 = 'MotorTemp'

P6 = 'Rear'

P7 = 'RearLeft'

P8 = 'RearRight'

Property = 'location'

headers = {'Content-Type': 'application/json', 'appKey': App_key } 

data1 = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 0.8)

data2 = serial.Serial("/dev/ttyACM1", baudrate = 9600, timeout = 0.2)

while True:

    data1Read = str(data1.readline())

    #print(data1Read)

    data2Read = str(data2.readline())

    data1Slice = data1Read[2:-1]

    data2Slice = data2Read[2:21]

    ultra = data1Slice.split(",")

    location = data2Slice.split(",")

    print(location)

    print(ultra)

    if len(data1Slice) > 14:

        payload1 = { P1: 1 , P2 : ultra[0] , P3 : ultra[1], P4 : ultra[2] , P5 : ultra[6], P6 : ultra[3], P7 : ultra[4], P8 : ultra[5]}

        response = requests.put(Webhost + '/Thingworx/Things/' + ThingName2 + '/Properties/*', headers = headers, json = payload1, verify = False)

           

    if len(data2Slice) > 15:

        print("lat in degrees:", location[0]," long in degree: ", location[1], '\n')

        if float(location[0]) > 0.0 and float(location[1]) > 0.0:

            payload2 = { Property: {"latitude": location[0], "longitude": location[1], "elevation": 0}}

            response = requests.put(Webhost + '/Thingworx/Things/' + ThingName1 + '/Properties/*', headers = headers, json = payload2, verify = False)
