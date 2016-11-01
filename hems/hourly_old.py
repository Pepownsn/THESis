import time
import urllib2
import json
import MySQLdb


conn= MySQLdb.connect("52.74.229.80","pepo","zxcvasdf1234") # One Pi 1 @192.168.1.25 namal localhost
c = conn.cursor()


while (True):#6481734ed070e007
    f = urllib2.urlopen('http://api.wunderground.com/api/6481734ed070e007/conditions/hourly/q/13.8220504,100.5924439.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    #print parsed_json
    temp = range(0,12,1)
    hum = range(0,12,1)
    rain = range(0,12,1)
    sky = range(0,12,1)
    condi = range(0,12,1)
    current = range(0,5,1)

    current[0] = int(parsed_json['current_observation']['local_epoch']) #time_s
    current[1]= int(parsed_json['current_observation']['temp_c'])#temp_s
    current[2] = str(parsed_json['current_observation']['relative_humidity']) #hum_s
    current[3] = (parsed_json['current_observation']['solarradiation'])#solar_s
    current[4] = int(parsed_json['current_observation']['precip_1hr_metric'])#rain_1h_s

    if (current[3] == '--'):
        current[3] = 0
    else : current[3] = int(current[3])

    i = 0
    while (i <= 11):

        temp[i] = int(parsed_json['hourly_forecast'][i]['temp']['metric'])
        hum[i] = int(parsed_json['hourly_forecast'][i]['humidity'])
        rain[i] = int(parsed_json['hourly_forecast'][i]['pop'])
        sky[i] = int(parsed_json['hourly_forecast'][i]['sky'])
        condi[i] = str(parsed_json['hourly_forecast'][i]['condition'])
        i += 1


    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current[0]))
    current[0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current[0]))
    print "current" , current
    print "Temp", temp
    print "Hum" , hum
    print "RAIN" , rain
    print "Sky", sky
    print "Condi", condi
    print ""
    #print current+temp+hum+rain+sky+condi
    #print len(current+temp+hum+rain+sky+condi)

    #print ("INSERT INTO Test.weather VALUES  %r ;" % (tuple(current+temp+hum+rain+sky+condi),))
    #print ("%r" % (tuple(temp),hum))


    c.execute("INSERT INTO Test.weather VALUES  %r ;" % (tuple(current+temp+hum+rain+sky+condi),))
    conn.commit()
    time.sleep(60*15)
