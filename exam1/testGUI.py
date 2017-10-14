import pygtk
pygtk.require('2.0')
import gtk
import glib
import time
import MySQLdb as mdb
import serial
from xbee import ZigBee
import re
from scipy.integrate import simps, trapz
import numpy as np
import pygame.mixer
import matplotlib.pyplot as plt
pygame.mixer.init()

serial_port = serial.Serial('/dev/ttyAMA0', 9600)
zb = ZigBee(serial_port)

con = mdb.connect('localhost', 'root', 'hems', 'appliances')
con2 = mdb.connect('localhost', 'root', 'hems', 'HEMS')
con3 = mdb.connect('localhost','root','hems','Plug')


cur = con.cursor()
cur1 = con.cursor()
cur2 = con3.cursor()
cur3 = con.cursor()
cur4 = con2.cursor()
cur5 = con2.cursor()
cur6 = con2.cursor()

#---------------------------------------------------------------Processing--------------------------------------------------------------------------------
loggit1 = """SELECT * FROM budget"""            
cur1.execute(loggit1)

for x4 in range(cur1.rowcount):        
    row = cur1.fetchone()
    price = float (row[1])

budget = np.empty(24, dtype=np.float)
budget.fill (price/720)

qavg = range(24)

qavgdaily = 0
for x1 in range(0 , 24) :
    qavgdaily = qavgdaily + qavg[x1]
qavgdaily = qavgdaily / 24

# Sort and Give order to qavg
qavgorder = range(24)
qavgcheck = np.sort(qavg)
qavgduplicate = list(qavg)
ordercount = 24

for x2 in range(0 , 24) :
    for x3 in range (0 , 24) :
        if (qavgcheck[x2] == qavgduplicate [x3]) :
            qavgorder [x3] = ordercount
            qavgduplicate [x3] = -9999
            break
    ordercount = ordercount - 1
  
# Optimize Budget For Processing
check = 24
percentage = float (0)

for x5 in range (0 , 12) :
    for x6 in range (0 , 24) :
        for x7 in range (0 , 24) :
            if (x5 + 1 == qavgorder[x6] and x5 + check == qavgorder[x7]) :
                percentage = float(1) - ((float(qavg[x7])) / qavgdaily)
                if (percentage < 0) :
                    percentage = percentage * -1
                budget[x6] = (float(percentage) * float(budget[x6])) + (float(budget[x6]))
                budget[x7] = price / 720 
                break
    check = check - 2

checkalarm = True
global checkalarm
#---------------------------------------------------------------------------------------------------------------------------------------------------------

cur.execute("SELECT * FROM appliances")
cur4.execute("SELECT * FROM COMMAND")
appliances_id = range(cur.rowcount) 
appliances_name = range(cur.rowcount)
appliances_power = range(cur.rowcount)
appliances_kind = range(cur.rowcount)
appliances_plug = range(cur.rowcount)
global appliances_plug
button_on = range(cur.rowcount)
button_off = range(cur.rowcount)
button_status = range(cur.rowcount)
button_baht = range(cur.rowcount)
ID_Device = range(cur4.rowcount)
ID = range(cur4.rowcount)
PIN = range(cur4.rowcount)
global button
for i in range(cur.rowcount):
    row = cur.fetchone()
    appliances_id [i] = row[0]
    appliances_name[i] = str(row[1])
    appliances_power [i] = row[2]
    appliances_kind [i] = row[3]
    appliances_plug [i] = row[4]

for i2 in range(cur4.rowcount) :
    row2 = cur4.fetchone()
    ID_Device[i2] = row2[0]
    ID[i2] = row2[3]
    PIN[i2] = row2[4]

looptime = 5
alarmtime = 0
global alarmtime

def column(matrix, t):
    return [powercolumn[t] for powercolumn in matrix]

def timer_cb():
    global appliances_plug
    global alarmtime
    global button_status
    global checkalarm
    con4 = mdb.connect('localhost','root','hems','Plug')
    con5 = mdb.connect('localhost', 'root', 'hems', 'HEMS')
    con6 = mdb.connect('localhost', 'root', 'hems', 'appliances')
    cur7 = con4.cursor()
    cur8 = con5.cursor()
    cur9 = con6.cursor()
    power = 0
    mytime = time.time()
    
    myset = time.localtime()
    year = str(myset[0])
    if (myset[1] < 10 ) :
        mon = "0" + str(myset[1])
    if (myset[1] > 9 ) :
        mon = str(myset[1])
    if (myset[2] < 10 ) :
        day = "0" + str(myset[2])
    if (myset[2] > 9 ) :
        day = str(myset[2])
    date = day + "-" + mon + "-" + year
    retrivepower = float (0)
    
    for x99 in range (0,cur.rowcount) :
        
        
        try :
            loggit ="""SELECT * FROM Plug%s WHERE Date = '%s' ORDER BY Time DESC LIMIT 1""" % (appliances_plug[x99],date)
            
            cur7.execute(loggit)
            row2 = cur7.fetchone()
            print row2
            retrivepower += float (row2[3])
            
        except :
            retrivepower = 0
            row2 = [0,0,0,0]
        
        
        if (float(row2[2]) > float(0.02) and checkalarm) :
            button_status[x99].set_label("On")
        if (float(row2[2]) <= float (0.02) and checkalarm) :
            button_status[x99].set_label("Off")
    

    
    #Generate Info---------------------------------------------------------------------
    loggit ="""SELECT * FROM S0013A2004070F6F4 ORDER BY DATE DESC LIMIT 1"""
    cur8.execute(loggit)
    row2 = cur8.fetchone()
    loggit1 = """SELECT * FROM budget"""            
    cur9.execute(loggit1)
    row3 = cur9.fetchone()
    recommend.set_label("Current Power : %s Watt Temp : %.1f C Budget : %s Baht" % (retrivepower,row2[2],row3[1]))
    retrivepower = float (retrivepower) / float (1000)
    indicate = budget[myset[3]] / float (3.2315)
    print retrivepower
    print "--------------------------------------------------------------------------------------"

    
    
    #Alarm------------------------------------------------------------------------------
    if (mytime > alarmtime + 1350 and retrivepower > indicate and not checkalarm ):
        loggit7 = """UPDATE COMMAND SET C_Motion = 1""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Temp = 1""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Light = 1""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Time = 1""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        for x99 in range (0,cur.rowcount) :
            if (appliances_kind [x99] == 1) :
                loggit7 = """UPDATE COMMAND SET C_Motion = 0 WHERE ID_Device = %s""" % (appliances_plug[x99])
                try :
                    cur6.execute(loggit7)
                    con2.commit()
                except :
                    con2.rollback()
                loggit7 = """UPDATE COMMAND SET C_Temp = 0 WHERE ID_Device = %s""" % (appliances_plug[x99])
                try :
                    cur6.execute(loggit7)
                    con2.commit()
                except :
                    con2.rollback()
                loggit7 = """UPDATE COMMAND SET C_Light = 0 WHERE ID_Device = %s""" % (appliances_plug[x99]) 
                try :
                    cur6.execute(loggit7)
                    con2.commit()
                except :
                    con2.rollback()
        checkalarm = True
        
    if (retrivepower < indicate):
        loggit7 = """UPDATE COMMAND SET C_Motion = 0""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Temp = 0""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Light = 0""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        loggit7 = """UPDATE COMMAND SET C_Time = 0""" 
        try :
            cur6.execute(loggit7)
            con2.commit()
        except :
            con2.rollback()
        shifttime_label.set_label("")
        shifttime_label2.set_label("")
        checkalarm = True

    if (retrivepower > indicate and checkalarm ):             
        
        pygame.mixer.music.load(open("glass_ping.wav"))
        pygame.mixer.music.play()
        
        for x99 in range (0,cur.rowcount) :
            boolean_history = True
            try :
                loggit ="""SELECT * FROM Plug%s WHERE Date = '%s' ORDER BY Time DESC LIMIT 720""" % (appliances_plug[x99],date)
                cur7.execute(loggit)
                row2 = cur7.fetchall()
                for x in range (0,cur7.rowcount) :
                    if (row2 [x][2] <= 0.02) :
                        boolean_history = False
                        break
                if (boolean_history) :
                    button_status[x99].set_label("appliances has turned for a long time")
                historyrow_power = column (row2,3)
                baht = (simps(historyrow_power, dx=float (5)/float(3600))) / float(1000) * float(3.9361) * float (24) * float (30) #float(looptime)/float(3600)
                button_baht[x99].set_label("%.2f" % (baht))
            except:
                print "fail"
                break
        #------------------------------------------------------------------------------------------------
        shifttime = range(4)
        shifttime_store = range (17)
        for x2 in range (0,17) :
            shifttime_store [x2] = qavgorder[x2+6]        
        for x2 in range (0,4) :            
            shifttime[x2] = np.argmax(shifttime_store) + 6
            shifttime_store [np.argmax(shifttime_store)] = 0             
        shifttime_label.set_label("1. Increase all air conditioner temperature from 25 C to 27 C")
        shifttime_label2.set_label("2. Suggest Time For Run Appliances : %s:00 %s:00 %s:00 %s:00" % (shifttime[0],shifttime[1],shifttime[2],shifttime[3]))
       
        #-------------------------------------------------------------------------------------------------
        checkalarm = False
        alarmtime = mytime
    cur7.close()
    cur8.close()
    cur9.close()
    return True



#------------------On Button------------------------------------------
def callback_on(widget, data=None):
    button_status[data[0]-1].set_label("Proceeding")
    
    for x6 in range (0,cur4.rowcount) :
        if (PIN[x6] == 'D' + str (data[0]-1)) :
            try :
                Device = re.sub("(..)", r"\x\1",ID[x6]) #locate device
                Device = Device.decode('string_escape')
                zb.send('tx', dest_addr_long = Device, dest_addr = '\xFF\xFE', frame_id = '\x01', data = PIN[x6] + 'Open')
                break
            except :
                break
    
    
    button_status[data[1]].set_label("On")

    
    
#------------------Off Button------------------------------------------
def callback_off(widget, data=None):
    button_status[data[0]-1].set_label("Proceeding")
    for x6 in range (0,cur4.rowcount) :
        
        if (PIN[x6] == 'D' + str (data[0]-1)) :
            try:
                Device = re.sub("(..)", r"\x\1",ID[x6]) #locate device
                Device = Device.decode('string_escape')
                zb.send('tx', dest_addr_long = Device, dest_addr = '\xFF\xFE', frame_id = '\x01', data = PIN[x6] + 'Close')
                break
            except :
                break
    checkalarm = True
    
    button_status[data[1]].set_label("Off")
#-------------------Graph Button------------------------------------------
def graph(widget, data=None):
    myset2 = time.localtime()
    year2 = str(myset2[0])
    if (myset2[1] < 10 ) :
        mon2 = "0" + str(myset2[1])
    if (myset2[1] > 9 ) :
        mon2 = str(myset2[1])
    if (myset2[2] < 10 ) :
        day2 = "0" + str(myset2[2])
    if (myset2[2] > 9 ) :
        day2 = str(myset2[2])
    date2 = day2 + "-" + mon2 + "-" + year2
    
    con7 = mdb.connect('localhost','root','hems','Plug')
    cur10 = con7.cursor()
    powergraph_y = np.empty(720, dtype=np.float)
    powergraph_y.fill(float (0))
    powergraph_x = np.linspace(60, 0, 720)
    
    for x6 in range (0,cur.rowcount):
        try :
            loggit ="""SELECT * FROM Plug%s WHERE Date = '%s' ORDER BY Time DESC LIMIT 720""" % (x6+1,date2) 
            cur10.execute(loggit)
            row3 = cur10.fetchall()
            for x8 in range (0,cur10.rowcount):
                powergraph_y[x8] += row3 [x8][3]
                
        except :
            print "fail"
    
    baht2 = ( simps(powergraph_y, dx = float(looptime)/float(3600) )) / float(1000) * float(3.9361)
    plt.title('Load Curve ,Total Cost : %.2f Baht' % (baht2))
    #plt.bar (powergraph_x ,powergraph_y,width =float(61)/float(1600))
    plt.plot (powergraph_x ,powergraph_y)
    
    plt.xlabel ('Time (minute)')
    plt.ylabel ('Power (Watt)')
    plt.show()
    
            
    
    
def show_cb(widget, data=None):
    glib.timeout_add_seconds(5, timer_cb)

def destroy_cb(widget, data=None):
    gtk.main_quit()

# Generate Gui Element
def main():
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)

    window.connect("show", show_cb)

    window.connect("destroy", destroy_cb)

    table = gtk.Table(cur.rowcount + 6, 20, True)
    global button
    global y
    global button_baht
    global button_status
    for y in range (0,cur.rowcount) :
        label = gtk.Label(appliances_name[y])
        button_on[y] = gtk.Button("On")
        button_off[y] = gtk.Button("Off")
        button_status[y] = gtk.Label("")
        button_baht[y] = gtk.Label("")
        button_on[y].connect("clicked", callback_on, [appliances_plug[y],y])
        button_off[y].connect("clicked", callback_off, [appliances_plug[y],y])
	
        
        table.attach(label, 0, 3, y+1, y+2)
        table.attach(button_status[y], 3, 13, y+1, y+2)
        table.attach(button_baht[y], 13, 18, y+1, y+2)
        table.attach(button_on[y], 18, 19, y+1, y+2)
        table.attach(button_off[y], 19, 20, y+1, y+2)
        button_on[y].show()
        button_off[y].show()
        button_baht[y].show()
        button_status[y].show()
        label.show() 	
        table.set_row_spacing(y,6)

    global recommend    
    recommend = gtk.Label("")
    name = gtk.Label("Name")
    status = gtk.Label("Status")
    Money = gtk.Label("Expected Cost of Electricity (Baht)")
    button_graph = gtk.Button("Show Hourly Load Curve")
    #----------------------------------------------------------------------------------------------------
    global shifttime_label
    global shifttime_label2
    shifttime_label = gtk.Label("")
    table.attach(shifttime_label, 0, 20, cur.rowcount+4, cur.rowcount+5)
    shifttime_label.show()
    shifttime_label2 = gtk.Label("")
    table.attach(shifttime_label2, 0, 20, cur.rowcount+5, cur.rowcount+6)
    shifttime_label2.show()
    #----------------------------------------------------------------------------------------------------
    button_graph.connect("clicked", graph, 0)
    table.attach(button_graph, 0, 20, cur.rowcount+2, cur.rowcount+3)
    table.attach(name, 0, 3, 0, 1)
    table.attach(status, 3, 13, 0, 1)
    table.attach(Money,13,18,0,1)
    name.show()
    status.show()
    recommend.show()
    Money.show()
    button_graph.show()
    table.attach(recommend,0,20,cur.rowcount+1,cur.rowcount+2)
    table.set_row_spacing(cur.rowcount,10)
    
    window.add(table)
    table.show()
    window.show()

    gtk.main()

if __name__ == "__main__":
    main()


#close Database-------------------------------------------------------------------------------------
cur.close()
cur1.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()
cur6.close()
