import MySQLdb
import time
import datetime
import re
import urllib2
import socket
import smtplib

num = 1
poo8= 0
poo10= 0
t = False
en_conn = False
while(True):
    clock = time.strftime("%H:%M:%S || %d/%m/%Y")

    print "No: ", num
    print clock
    print "EN-CONN:",en_conn
    print "Email Sending:" ,t
    try:
        s = socket.socket()
        s.connect(('192.168.1.70',80))
        en_conn = True
        print "Socket_Connect OK"
        enegate_conn = urllib2.urlopen("http://192.168.1.70/index.cgi")
        response = enegate_conn.read()
        t = False
    except socket.error, exc:
        print "Can't Connect : %s \n" % exc
        en_conn = False
        en_conn = False
        #-----------------------------------------
        if t == False :
            print "Send Email ---->"
            from_u = 'driver.tum@gmail.com'
            to = 'tum.354527@gmail.com'

            aws_user = 'AKIAJGWSOWV3ZYNBW4MA'
            aws_password = 'AvDvpFYfH8F/gvRwxM3CCumhCMxLTyikN92y3WXFgqoQ'



            subject = 'Connection Down!!'




            email_text = """\
            From: %s
            To: %s
            Subject: %s

            Can't connect to http://skyfighter.ddns.net:10070/index.cgi

            %s
            """ % (from_u, to, subject, datetime.datetime.now())

            try:
                server = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587,10)
                #server.set_debuglevel(10)
                server.starttls()
                server.ehlo()
                server.login(aws_user, aws_password)
                server.sendmail(from_u, to, email_text)
                server.close()

                print 'Email sent!'
                t = True
            except:
                print 'Something went wrong...'



    if en_conn == True :

        powers = re.findall('electric_value2">(.*?)</td>',response)
        #print powers
#####################################################################################################3
    	po ={}
    	int_po = {}
    	po_all = {}

    	date = time.strftime("%d/%m/%Y")
    	#clock = time.strftime("%H:%M:%S || %d/%m/%Y")



    	num += 1


        i = 0
        for x in powers:

            #if x == "----":
            #    x = 0
            if i < 20:
            #    po[i] = float(x)
                po[i] = x
            #    if i == 8:
            #        po8 = float(x)
            #    if i == 10:
            #        po10 = float(x)
                i += 1

    #    po10 = po10/240.00/1000
    #    poo10 += po10
        #print po8
    #    po8 = po8/240.00/1000
        #print po8
    #    poo8 += po8
        #print poo8
        #print po_all
        print "\n"
        #print po


        #Connect to Databases
        #------MySQL
        #CREATE DATABASE power;

        conn= MySQLdb.connect("localhost","root","tum354527","power") # One Pi 1 @192.168.1.25 namal localhost
        
        c = conn.cursor()

        c.execute("INSERT INTO power.enegate_bkk (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (po[0],po[1], po[2], po[3], po[4], po[5], po[6], po[7], po[8], po[9],po[10], po[11], po[12], po[13], po[14], po[15], po[16], po[17], po[18], po[19]))


        conn.commit()

        #c.execute("SELECT * FROM enegate")

        #rows = c.fetchall()




    time.sleep(15)
