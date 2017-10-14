import time
import urllib2
import json
import MySQLdb
import socket
import smtplib
import datetime




conn= MySQLdb.connect("52.74.229.80","pepo","zxcvasdf1234") # One Pi 1 @192.168.1.25 namal localhost
c = conn.cursor()

while (True):#6481734ed070e007
    f = urllib2.urlopen('https://api.darksky.net/forecast/1f2dfd5851b00f9ad81e67197733379c/13.8220504,100.5924439?units=auto')
    json_string = f.read()


    parsed_json = json.loads(json_string)
            #print parsed_json

    #print parsed_json

    current = range(0,6,1)
    hourly_0 = range(0,7,1)
    hourly_1 = range(0,7,1)
    hourly_2 = range(0,7,1)
    hourly_3 = range(0,7,1)
    hourly_4 = range(0,7,1)
    hourly_5 = range(0,7,1)
    hourly_6 = range(0,7,1)
    hourly_7 = range(0,7,1)
    hourly_8 = range(0,7,1)
    hourly_9 = range(0,7,1)
    hourly_10 = range(0,7,1)
    hourly_11 = range(0,7,1)
    hourly_12 = range(0,7,1)
    hourly_12 = range(0,7,1)
    hourly_13 = range(0,7,1)
    hourly_14 = range(0,7,1)
    hourly_15 = range(0,7,1)
    hourly_16 = range(0,7,1)
    hourly_17 = range(0,7,1)
    hourly_18 = range(0,7,1)
    hourly_19= range(0,7,1)
    hourly_20 = range(0,7,1)
    hourly_21 = range(0,7,1)
    hourly_22 = range(0,7,1)
    hourly_23 = range(0,7,1)
    hourly_24 = range(0,7,1)

    current[0] = (parsed_json['currently']['time'])
    current[1] = (parsed_json['currently']['temperature'])
    current[2] = (parsed_json['currently']['humidity'])
    current[3] = (parsed_json['currently']['precipIntensity'])
    current[4] = (parsed_json['currently']['precipProbability'])
    current[5] = (parsed_json['currently']['cloudCover'])

    hourly_0[1] = (parsed_json['hourly']['data'][0]['time'])
    hourly_0[2] = (parsed_json['hourly']['data'][0]['temperature'])
    hourly_0[3] = (parsed_json['hourly']['data'][0]['humidity'])
    hourly_0[4] = (parsed_json['hourly']['data'][0]['precipIntensity'])
    hourly_0[5] = (parsed_json['hourly']['data'][0]['precipProbability'])
    hourly_0[6] = (parsed_json['hourly']['data'][0]['cloudCover'])

    hourly_1[1] = (parsed_json['hourly']['data'][1]['time'])
    hourly_1[2] = (parsed_json['hourly']['data'][1]['temperature'])
    hourly_1[3] = (parsed_json['hourly']['data'][1]['humidity'])
    hourly_1[4] = (parsed_json['hourly']['data'][1]['precipIntensity'])
    hourly_1[5] = (parsed_json['hourly']['data'][1]['precipProbability'])
    hourly_1[6] = (parsed_json['hourly']['data'][1]['cloudCover'])

    hourly_2[1] = (parsed_json['hourly']['data'][2]['time'])
    hourly_2[2] = (parsed_json['hourly']['data'][2]['temperature'])
    hourly_2[3] = (parsed_json['hourly']['data'][2]['humidity'])
    hourly_2[4] = (parsed_json['hourly']['data'][2]['precipIntensity'])
    hourly_2[5] = (parsed_json['hourly']['data'][2]['precipProbability'])
    hourly_2[6] = (parsed_json['hourly']['data'][2]['cloudCover'])

    hourly_3[1] = (parsed_json['hourly']['data'][3]['time'])
    hourly_3[2] = (parsed_json['hourly']['data'][3]['temperature'])
    hourly_3[3] = (parsed_json['hourly']['data'][3]['humidity'])
    hourly_3[4] = (parsed_json['hourly']['data'][3]['precipIntensity'])
    hourly_3[5] = (parsed_json['hourly']['data'][3]['precipProbability'])
    hourly_3[6] = (parsed_json['hourly']['data'][3]['cloudCover'])

    hourly_4[1] = (parsed_json['hourly']['data'][4]['time'])
    hourly_4[2] = (parsed_json['hourly']['data'][4]['temperature'])
    hourly_4[3] = (parsed_json['hourly']['data'][4]['humidity'])
    hourly_4[4] = (parsed_json['hourly']['data'][4]['precipIntensity'])
    hourly_4[5] = (parsed_json['hourly']['data'][4]['precipProbability'])
    hourly_4[6] = (parsed_json['hourly']['data'][4]['cloudCover'])

    hourly_5[1] = (parsed_json['hourly']['data'][5]['time'])
    hourly_5[2] = (parsed_json['hourly']['data'][5]['temperature'])
    hourly_5[3] = (parsed_json['hourly']['data'][5]['humidity'])
    hourly_5[4] = (parsed_json['hourly']['data'][5]['precipIntensity'])
    hourly_5[5] = (parsed_json['hourly']['data'][5]['precipProbability'])
    hourly_5[6] = (parsed_json['hourly']['data'][5]['cloudCover'])

    hourly_6[1] = (parsed_json['hourly']['data'][6]['time'])
    hourly_6[2] = (parsed_json['hourly']['data'][6]['temperature'])
    hourly_6[3] = (parsed_json['hourly']['data'][6]['humidity'])
    hourly_6[4] = (parsed_json['hourly']['data'][6]['precipIntensity'])
    hourly_6[5] = (parsed_json['hourly']['data'][6]['precipProbability'])
    hourly_6[6] = (parsed_json['hourly']['data'][6]['cloudCover'])


    hourly_7[1] = (parsed_json['hourly']['data'][7]['time'])
    hourly_7[2] = (parsed_json['hourly']['data'][7]['temperature'])
    hourly_7[3] = (parsed_json['hourly']['data'][7]['humidity'])
    hourly_7[4] = (parsed_json['hourly']['data'][7]['precipIntensity'])
    hourly_7[5] = (parsed_json['hourly']['data'][7]['precipProbability'])
    hourly_7[6] = (parsed_json['hourly']['data'][7]['cloudCover'])

    hourly_8[1] = (parsed_json['hourly']['data'][8]['time'])
    hourly_8[2] = (parsed_json['hourly']['data'][8]['temperature'])
    hourly_8[3] = (parsed_json['hourly']['data'][8]['humidity'])
    hourly_8[4] = (parsed_json['hourly']['data'][8]['precipIntensity'])
    hourly_8[5] = (parsed_json['hourly']['data'][8]['precipProbability'])
    hourly_8[6] = (parsed_json['hourly']['data'][8]['cloudCover'])

    hourly_9[1] = (parsed_json['hourly']['data'][9]['time'])
    hourly_9[2] = (parsed_json['hourly']['data'][9]['temperature'])
    hourly_9[3] = (parsed_json['hourly']['data'][9]['humidity'])
    hourly_9[4] = (parsed_json['hourly']['data'][9]['precipIntensity'])
    hourly_9[5] = (parsed_json['hourly']['data'][9]['precipProbability'])
    hourly_9[6] = (parsed_json['hourly']['data'][9]['cloudCover'])

    hourly_10[1] = (parsed_json['hourly']['data'][10]['time'])
    hourly_10[2] = (parsed_json['hourly']['data'][10]['temperature'])
    hourly_10[3] = (parsed_json['hourly']['data'][10]['humidity'])
    hourly_10[4] = (parsed_json['hourly']['data'][10]['precipIntensity'])
    hourly_10[5] = (parsed_json['hourly']['data'][10]['precipProbability'])
    hourly_10[6] = (parsed_json['hourly']['data'][10]['cloudCover'])

    hourly_11[1] = (parsed_json['hourly']['data'][11]['time'])
    hourly_11[2] = (parsed_json['hourly']['data'][11]['temperature'])
    hourly_11[3] = (parsed_json['hourly']['data'][11]['humidity'])
    hourly_11[4] = (parsed_json['hourly']['data'][11]['precipIntensity'])
    hourly_11[5] = (parsed_json['hourly']['data'][11]['precipProbability'])
    hourly_11[6] = (parsed_json['hourly']['data'][11]['cloudCover'])

    hourly_12[1] = (parsed_json['hourly']['data'][12]['time'])
    hourly_12[2] = (parsed_json['hourly']['data'][12]['temperature'])
    hourly_12[3] = (parsed_json['hourly']['data'][12]['humidity'])
    hourly_12[4] = (parsed_json['hourly']['data'][12]['precipIntensity'])
    hourly_12[5] = (parsed_json['hourly']['data'][12]['precipProbability'])
    hourly_12[6] = (parsed_json['hourly']['data'][12]['cloudCover'])

    hourly_13[1] = (parsed_json['hourly']['data'][13]['time'])
    hourly_13[2] = (parsed_json['hourly']['data'][13]['temperature'])
    hourly_13[3] = (parsed_json['hourly']['data'][13]['humidity'])
    hourly_13[4] = (parsed_json['hourly']['data'][13]['precipIntensity'])
    hourly_13[5] = (parsed_json['hourly']['data'][13]['precipProbability'])
    hourly_13[6] = (parsed_json['hourly']['data'][13]['cloudCover'])

    hourly_14[1] = (parsed_json['hourly']['data'][14]['time'])
    hourly_14[2] = (parsed_json['hourly']['data'][14]['temperature'])
    hourly_14[3] = (parsed_json['hourly']['data'][14]['humidity'])
    hourly_14[4] = (parsed_json['hourly']['data'][14]['precipIntensity'])
    hourly_14[5] = (parsed_json['hourly']['data'][14]['precipProbability'])
    hourly_14[6] = (parsed_json['hourly']['data'][14]['cloudCover'])

    hourly_15[1] = (parsed_json['hourly']['data'][15]['time'])
    hourly_15[2] = (parsed_json['hourly']['data'][15]['temperature'])
    hourly_15[3] = (parsed_json['hourly']['data'][15]['humidity'])
    hourly_15[4] = (parsed_json['hourly']['data'][15]['precipIntensity'])
    hourly_15[5] = (parsed_json['hourly']['data'][15]['precipProbability'])
    hourly_15[6] = (parsed_json['hourly']['data'][15]['cloudCover'])

    hourly_16[1] = (parsed_json['hourly']['data'][16]['time'])
    hourly_16[2] = (parsed_json['hourly']['data'][16]['temperature'])
    hourly_16[3] = (parsed_json['hourly']['data'][16]['humidity'])
    hourly_16[4] = (parsed_json['hourly']['data'][16]['precipIntensity'])
    hourly_16[5] = (parsed_json['hourly']['data'][16]['precipProbability'])
    hourly_16[6] = (parsed_json['hourly']['data'][16]['cloudCover'])

    hourly_17[1] = (parsed_json['hourly']['data'][17]['time'])
    hourly_17[2] = (parsed_json['hourly']['data'][17]['temperature'])
    hourly_17[3] = (parsed_json['hourly']['data'][17]['humidity'])
    hourly_17[4] = (parsed_json['hourly']['data'][17]['precipIntensity'])
    hourly_17[5] = (parsed_json['hourly']['data'][17]['precipProbability'])
    hourly_17[6] = (parsed_json['hourly']['data'][17]['cloudCover'])

    hourly_18[1] = (parsed_json['hourly']['data'][18]['time'])
    hourly_18[2] = (parsed_json['hourly']['data'][18]['temperature'])
    hourly_18[3] = (parsed_json['hourly']['data'][18]['humidity'])
    hourly_18[4] = (parsed_json['hourly']['data'][18]['precipIntensity'])
    hourly_18[5] = (parsed_json['hourly']['data'][18]['precipProbability'])
    hourly_18[6] = (parsed_json['hourly']['data'][18]['cloudCover'])

    hourly_19[1] = (parsed_json['hourly']['data'][19]['time'])
    hourly_19[2] = (parsed_json['hourly']['data'][19]['temperature'])
    hourly_19[3] = (parsed_json['hourly']['data'][19]['humidity'])
    hourly_19[4] = (parsed_json['hourly']['data'][19]['precipIntensity'])
    hourly_19[5] = (parsed_json['hourly']['data'][19]['precipProbability'])
    hourly_19[6] = (parsed_json['hourly']['data'][19]['cloudCover'])

    hourly_20[1] = (parsed_json['hourly']['data'][20]['time'])
    hourly_20[2] = (parsed_json['hourly']['data'][20]['temperature'])
    hourly_20[3] = (parsed_json['hourly']['data'][20]['humidity'])
    hourly_20[4] = (parsed_json['hourly']['data'][20]['precipIntensity'])
    hourly_20[5] = (parsed_json['hourly']['data'][20]['precipProbability'])
    hourly_20[6] = (parsed_json['hourly']['data'][20]['cloudCover'])

    hourly_21[1] = (parsed_json['hourly']['data'][21]['time'])
    hourly_21[2] = (parsed_json['hourly']['data'][21]['temperature'])
    hourly_21[3] = (parsed_json['hourly']['data'][21]['humidity'])
    hourly_21[4] = (parsed_json['hourly']['data'][21]['precipIntensity'])
    hourly_21[5] = (parsed_json['hourly']['data'][21]['precipProbability'])
    hourly_21[6] = (parsed_json['hourly']['data'][21]['cloudCover'])

    hourly_22[1] = (parsed_json['hourly']['data'][22]['time'])
    hourly_22[2] = (parsed_json['hourly']['data'][22]['temperature'])
    hourly_22[3] = (parsed_json['hourly']['data'][22]['humidity'])
    hourly_22[4] = (parsed_json['hourly']['data'][22]['precipIntensity'])
    hourly_22[5] = (parsed_json['hourly']['data'][22]['precipProbability'])
    hourly_22[6] = (parsed_json['hourly']['data'][22]['cloudCover'])

    hourly_23[1] = (parsed_json['hourly']['data'][23]['time'])
    hourly_23[2] = (parsed_json['hourly']['data'][23]['temperature'])
    hourly_23[3] = (parsed_json['hourly']['data'][23]['humidity'])
    hourly_23[4] = (parsed_json['hourly']['data'][23]['precipIntensity'])
    hourly_23[5] = (parsed_json['hourly']['data'][23]['precipProbability'])
    hourly_23[6] = (parsed_json['hourly']['data'][23]['cloudCover'])

    hourly_24[1] = (parsed_json['hourly']['data'][24]['time'])
    hourly_24[2] = (parsed_json['hourly']['data'][24]['temperature'])
    hourly_24[3] = (parsed_json['hourly']['data'][24]['humidity'])
    hourly_24[4] = (parsed_json['hourly']['data'][24]['precipIntensity'])
    hourly_24[5] = (parsed_json['hourly']['data'][24]['precipProbability'])
    hourly_24[6] = (parsed_json['hourly']['data'][24]['cloudCover'])


    current[0]  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current[0]))
    hourly_0[0] = current[0]
    hourly_1[0] = current[0]
    hourly_2[0] = current[0]
    hourly_3[0] = current[0]
    hourly_4[0] = current[0]
    hourly_5[0] = current[0]
    hourly_6[0] = current[0]
    hourly_7[0] = current[0]
    hourly_8[0] = current[0]
    hourly_9[0] = current[0]
    hourly_10[0] = current[0]
    hourly_11[0] = current[0]
    hourly_12[0] = current[0]
    hourly_13[0] = current[0]
    hourly_14[0] = current[0]
    hourly_15[0] = current[0]
    hourly_16[0] = current[0]
    hourly_17[0] = current[0]
    hourly_18[0] = current[0]
    hourly_19[0] = current[0]
    hourly_20[0] = current[0]
    hourly_21[0] = current[0]
    hourly_22[0] = current[0]
    hourly_23[0] = current[0]
    hourly_24[0] = current[0]

    hourly_0[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_0[1]))
    hourly_1[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_1[1]))
    hourly_2[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_2[1]))
    hourly_3[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_3[1]))
    hourly_4[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_4[1]))
    hourly_5[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_5[1]))
    hourly_6[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_6[1]))
    hourly_7[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_7[1]))
    hourly_8[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_8[1]))
    hourly_9[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_9[1]))
    hourly_10[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_10[1]))
    hourly_11[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_11[1]))
    hourly_12[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_12[1]))
    hourly_13[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_13[1]))
    hourly_14[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_14[1]))
    hourly_15[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_15[1]))
    hourly_16[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_16[1]))
    hourly_17[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_17[1]))
    hourly_18[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_18[1]))
    hourly_19[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_19[1]))
    hourly_20[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_20[1]))
    hourly_21[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_21[1]))
    hourly_22[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_22[1]))
    hourly_23[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_23[1]))
    hourly_24[1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hourly_24[1]))

    print current

    print hourly_0
    print hourly_1
    print hourly_2
    print hourly_3
    print hourly_4
    print hourly_5
    print hourly_6
    print hourly_7
    print hourly_8
    print hourly_9
    print hourly_10
    print hourly_11
    print hourly_12
    print hourly_13
    print hourly_14
    print hourly_15
    print hourly_16
    print hourly_17
    print hourly_18
    print hourly_19
    print hourly_20
    print hourly_21
    print hourly_22
    print hourly_23
    print hourly_24


    c.execute("INSERT INTO forecast.current VALUES  %r ;" % (tuple(current),))
    c.execute("INSERT INTO forecast.hourly_0 VALUES  %r ;" % (tuple(hourly_0),))
    c.execute("INSERT INTO forecast.hourly_1 VALUES  %r ;" % (tuple(hourly_1),))
    c.execute("INSERT INTO forecast.hourly_2 VALUES  %r ;" % (tuple(hourly_2),))
    c.execute("INSERT INTO forecast.hourly_3 VALUES  %r ;" % (tuple(hourly_3),))
    c.execute("INSERT INTO forecast.hourly_4 VALUES  %r ;" % (tuple(hourly_4),))
    c.execute("INSERT INTO forecast.hourly_5 VALUES  %r ;" % (tuple(hourly_5),))
    c.execute("INSERT INTO forecast.hourly_6 VALUES  %r ;" % (tuple(hourly_6),))
    c.execute("INSERT INTO forecast.hourly_7 VALUES  %r ;" % (tuple(hourly_7),))
    c.execute("INSERT INTO forecast.hourly_8 VALUES  %r ;" % (tuple(hourly_8),))
    c.execute("INSERT INTO forecast.hourly_9 VALUES  %r ;" % (tuple(hourly_9),))
    c.execute("INSERT INTO forecast.hourly_10 VALUES  %r ;" % (tuple(hourly_10),))
    c.execute("INSERT INTO forecast.hourly_11 VALUES  %r ;" % (tuple(hourly_11),))
    c.execute("INSERT INTO forecast.hourly_12 VALUES  %r ;" % (tuple(hourly_12),))
    c.execute("INSERT INTO forecast.hourly_13 VALUES  %r ;" % (tuple(hourly_13),))
    c.execute("INSERT INTO forecast.hourly_14 VALUES  %r ;" % (tuple(hourly_14),))
    c.execute("INSERT INTO forecast.hourly_15 VALUES  %r ;" % (tuple(hourly_15),))
    c.execute("INSERT INTO forecast.hourly_16 VALUES  %r ;" % (tuple(hourly_16),))
    c.execute("INSERT INTO forecast.hourly_17 VALUES  %r ;" % (tuple(hourly_17),))
    c.execute("INSERT INTO forecast.hourly_18 VALUES  %r ;" % (tuple(hourly_18),))
    c.execute("INSERT INTO forecast.hourly_19 VALUES  %r ;" % (tuple(hourly_19),))
    c.execute("INSERT INTO forecast.hourly_20 VALUES  %r ;" % (tuple(hourly_20),))
    c.execute("INSERT INTO forecast.hourly_21 VALUES  %r ;" % (tuple(hourly_21),))
    c.execute("INSERT INTO forecast.hourly_22 VALUES  %r ;" % (tuple(hourly_22),))
    c.execute("INSERT INTO forecast.hourly_23 VALUES  %r ;" % (tuple(hourly_23),))
    c.execute("INSERT INTO forecast.hourly_24 VALUES  %r ;" % (tuple(hourly_24),))



    conn.commit()
    time.sleep(60*5)
