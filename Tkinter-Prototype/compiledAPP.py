#MODULES


import random
import tkinter as tk
import tkintermapview as op

gui=tk.Tk() 



#ALL CONSTANTS



Weather=['29 ˚C','65%','20%','14 km/h','Partly Cloudy ⛅']

P=[8.9,26.8,22,55.5,0.3] 
M=[9.1,24.8,15,40,2]
Ma=[8.9,26.8,25,40,2]



#GENERAL FUNCTIONS



def back(frame):
    frame.destroy()



#WATER SPECIFIC FUNCTIONS



def WQI(LAKE):
    QPh=(LAKE[0]/8.5)*100 
    QTemp=(LAKE[1]/25)*100 # in celsius
    QBod=(LAKE[2]/10)*100 #in mg/L, 1 FOR DRINKING, LAKES AVG HAVE 20+ BOD
    QTurb=(LAKE[3]/5)*100
    QAmm=(LAKE[4]/1.2)*100 #in mg/L
    A=(QPh*0.0910+QTemp*0.0309+QBod*0.0774+QTurb*0.1549+QAmm*0.6455)
    return str(A)

def WQIPut():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    map= op.TkinterMapView(frame1, width=370, height= 415, corner_radius=40)
    map.place(x=5 ,y=330)
    a=map.set_position(12.8904, 77.5872, marker=True)
    a.set_text('Puttenahalli Lake')
    
    aqi=tk.Label(frame1, text="𝑾𝑸𝑰:", font=('georgia', 35), bg='#2A2A2C')
    aqi.place(x=85, y=50)
    aqi=tk.Label(frame1, text=WQI(P), font=('arial', 120), fg='RED',bg='#2A2A2C')
    aqi.place(x=115, y=105)

    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)
    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)


def WQIMah():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    map= op.TkinterMapView(frame1, width=370, height= 415, corner_radius=40)
    map.place(x=5 ,y=330)
    a=map.set_position(12.9871, 77.6926, marker=True)
    a.set_text('Mahadevapura Lake')
    aqi=tk.Label(frame1, text="𝑾𝑸𝑰:", font=('georgia', 35), bg='#2A2A2C')
    aqi.place(x=85, y=50)
    aqi=tk.Label(frame1, text=WQI(M), font=('arial', 120), fg='RED',bg='#2A2A2C')
    aqi.place(x=115, y=105)
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)
    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)

def WQIMad():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    map= op.TkinterMapView(frame1, width=370, height= 415, corner_radius=40)
    map.place(x=5 ,y=330)
    a=map.set_position(12.907502, 77.617260, marker=True)
    a.set_text('Madiwala Lake')
    aqi=tk.Label(frame1, text="𝑾𝑸𝑰:", font=('georgia', 35), bg='#2A2A2C')
    aqi.place(x=85, y=50)
    aqi=tk.Label(frame1, text=WQI(Ma), font=('arial', 120), fg='RED',bg='#2A2A2C')
    aqi.place(x=115, y=105)
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)
    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)

def WQICalc2(a, b, c, d, e):
    global frame1
    QPh=(a/8.5)*100 
    QTemp=(b/25)*100 # in celsius
    QBod=(c/10)*100 #in mg/L, 1 FOR DRINKING, LAKES AVG HAVE 20+ BOD
    QTurb=(d/5)*100
    QAmm=(e/1.2)*100 #in mg/L
    A=(QPh*0.0910+QTemp*0.0309+QBod*0.0774+QTurb*0.1549+QAmm*0.6455)
    label=tk.Label(frame1, text= A)
    label.place(x=185 ,y=310)

def WQICalc():
    global frame1
    frame1=tk.Frame(gui, bg='#4B4E53')
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)
    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)
    
    labelph=tk.Label(frame1, text='Enter PH:', fg='#FFFFFF', bg='#4B4E53', font=('georgia', 20))
    labelph.place(x=10, y=50)
    ph=tk.Entry(frame1)
    ph.place(x=175, y=50)

    labeltemp=tk.Label(frame1, text='Enter Temp:', fg='#FFFFFF', bg='#4B4E53', font=('georgia', 20))
    labeltemp.place(x=10, y=100)
    temp=tk.Entry(frame1)
    temp.place(x=175, y=100)
    
    labelbod=tk.Label(frame1, text='Enter BOD:', fg='#FFFFFF', bg='#4B4E53', font=('georgia', 20))
    labelbod.place(x=10, y=150)
    bod=tk.Entry(frame1)
    bod.place(x=175, y=150)

    labelturb=tk.Label(frame1, text='Enter Turbidity:', fg='#FFFFFF', bg='#4B4E53', font=('georgia', 20))
    labelturb.place(x=10, y=200)
    turb=tk.Entry(frame1)
    turb.place(x=175, y=200)

    labelamm=tk.Label(frame1, text='Enter Ammonia:', fg='#FFFFFF', bg='#4B4E53', font=('georgia', 20))
    labelamm.place(x=10, y=250)
    amm=tk.Entry(frame1)
    amm.place(x=175, y=250)

    button=tk.Button(frame1, text="Calculate", command=lambda: WQICalc2(int(ph.get()), int(temp.get()), int(bod.get()), int(turb.get()), int(amm.get())))
    button.place(x=10,y=300)



#AIR SPECIFIC FUNCTIONS



def healthhazards():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)

    aqi=tk.Label(frame1, text='''Bengaluru was found to have an annual average PM2.5
    concentration of 29.01 μg/m3, which is 5.8 times higher
    than the safe levels (5 µg/m3) set by the WHO.
    The city’s annual average PM10 concentration was
    found to be 55.14 μg/m3, 3.7 times higher than the
    safe levels (15 μg/m3).''', bg='#2A2A2C')
    aqi.place(x=0, y=50)
    aqi.configure(width=40, height=10)

    aqi=tk.Label(frame1, text='''Q) What are the diseases associated with Air pollution?
    A)-Heart Diseases, asthma or respiratory diseases.
    -Illness associated with Lung infection, bronchitis, flu,
    especially in small kids and older people.''', bg='#2A2A2C')
    aqi.place(x=0, y=150)
    aqi.configure(width=40, height=10)

    aqi=tk.Label(frame1, text='''Q) What are the Pysical effects on a human body?
    A)-Skin diseases or skin rashes, as the fine dust particles
    settle easily on skin.
    -Watery eyes, headaches, sinusitis,
     or any from of allergies.''', bg='#2A2A2C')
    aqi.place(x=0, y=270)
    aqi.configure(width=40, height=10)

    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)

def AQIBang():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)

    aqi1=tk.Label(frame1, text="--Bangalore--", font=('georgia', 35), bg='#2A2A2C')
    aqi1.place(x=85, y=25)

    Mainlabel=tk.Label(frame1, bg='#4B4E53')
    Mainlabel.place(x=25, y=80)
    Mainlabel.configure(width=35, height=25)

    list1 = [76,78,79,81,83.4,83,82,84.5, 84.6,88,89.2,90,91.3,96,98,99,92,92.7]
    a=random.randint(0,17)
    A=list1[a]
    if A>=85:
        aqi=tk.Label(frame1, text="AQI", font=('georgia', 20), bg='#4B4E53')
        aqi.place(x=25, y=100)
        aqi.configure(width=10, height=2)
        aqi1=tk.Label(frame1, text=A, font=('arial', 23), fg='RED',bg='#4B4E53')
        aqi1.place(x=250, y=110)

    else:
        aqi=tk.Label(frame1, text="AQI", font=('georgia', 20), bg='#4B4E53')
        aqi.place(x=25, y=100)
        aqi.configure(width=10, height=2)
        aqi1=tk.Label(frame1, text=A, font=('arial', 23), fg='YELLOW',bg='#4B4E53')
        aqi1.place(x=250, y=110)

    aqi=tk.Label(frame1, text="PM", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=150)
    aqi.configure(width=10, height=2)
    aqi1=tk.Label(frame1, text="68", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=160)

    aqi=tk.Label(frame1, text="NO", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=200)
    aqi.configure(width=10, height=2)
    aqi1=tk.Label(frame1, text="47", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=210)

    aqi=tk.Label(frame1, text="CO", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=250)
    aqi.configure(width=10, height=2)
    aqi1=tk.Label(frame1, text="93", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=260)

    aqi=tk.Label(frame1, text="O3", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=300)
    aqi.configure(width=10, height=2)   
    aqi1=tk.Label(frame1, text="42", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=310)
        

    aqi=tk.Label(frame1, text="SO2", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=350)
    aqi.configure(width=10, height=2)
    aqi1=tk.Label(frame1, text="2", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=360)    

    aqi=tk.Label(frame1, text="NO2", font=('georgia', 20), bg='#4B4E53')
    aqi.place(x=25, y=400)
    aqi.configure(width=10, height=2)
    aqi1=tk.Label(frame1, text="47", font=('arial', 23), fg='YELLOW',bg='#4B4E53')
    aqi1.place(x=250, y=410)

    button=tk.Button(frame1, text='How does my Air affect Me?', command= healthhazards)
    button.place(x=75, y=520)

    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)



#MAIN CALL FUNCTIONS



def sidebar(Weather):
    frame=tk.Frame(gui, bg='#FFFFFF')
    frame.place(x=0, y=0)
    frame.configure(width=300, height=800, bg='#c3c3c3')
    frame1=tk.Frame(frame, bg='#2A2A2C')
    frame1.place(x=2, y=2)
    frame1.configure(width=296, height=796)

    label=tk.Label(frame1, text='Your Location:', font=('georgia', 15), bg='#2a2a2c')
    label.place(x=15,y=40)
    label=tk.Label(frame1, text='Bangalore, India', font=('georgia', 33),bg='#2a2a2c')
    label.place(x=15,y=60)
    label=tk.Label(frame1, text=Weather[4], font=('georgia', 15), bg='#2a2a2c')
    label.place(x=15,y=100)
    label=tk.Label(frame1, text='Weather Today:', font=('georgia', 20),bg='#2a2a2c')
    label.place(x=15,y=135)
    label=tk.Label(frame1, text='Temperature: '+Weather[0], font=('georgia', 15),bg='#2a2a2c')
    label.place(x=15,y=160)
    label=tk.Label(frame1, text='Humidity: '+Weather[1], font=('georgia', 15),bg='#2a2a2c')
    label.place(x=15,y=185)
    label=tk.Label(frame1, text='Precipitation: '+Weather[2], font=('georgia', 15),bg='#2a2a2c')
    label.place(x=15,y=210)
    label=tk.Label(frame1, text='Wind Speed: '+Weather[3], font=('georgia', 15),bg='#2a2a2c')
    label.place(x=15,y=235)

    button=tk.Button(frame1, text='Report an Issue')
    button.place(x=15, y=750)

    button=tk.Button(frame1, text='X', command=lambda: back(frame))
    button.place(x=5, y=5)

def water():
    frame1=tk.Frame(gui, bg='#2A2A2C')
    head=tk.Label(frame1, text='Choose a Lake', font=('arial',30), bg='#2A2A2C')
    head.pack(padx=10, pady=100)
    frame1.place(x=10, y=50)
    frame1.pack_propagate(False)
    frame1.configure(width=380, height=750)

    button1=tk.Button(frame1, text='Puttenahalli Lake', command=WQIPut)
    button1.place(x=110, y=200)
    button1.configure(width=15, height=4)

    button2=tk.Button(frame1, text='Mahadevapura Lake', command=WQIMah)
    button2.place(x=110, y=300)
    button2.configure(width=15, height=4)

    button3=tk.Button(frame1, text='Madiwala Lake', command=WQIMad)
    button3.place(x=110, y=400)
    button3.configure(width=15, height=4)

    button4=tk.Button(frame1, text='Calculate WQI', command=WQICalc)
    button4.place(x=110, y=500)
    button4.configure(width=15, height=4)
    
    button=tk.Button(frame1, text='X', command=lambda: back(frame1))
    button.place(x=330, y=0)



#MAIN CODE



gui.geometry('400x800') 
gui.title('Prakriti') 
filename=tk.PhotoImage(file="apple.ppm")
background_label=tk.Label(gui,image=filename)
background_label.place(x=0,y=0)

frame1=tk.Frame(gui, bg='#FFFFFF')
frame1.place(x=0,y=0)
frame1.configure(width=400, height=50)
header=tk.Label(gui, text='𝓟𝓻𝓪𝓴𝓻𝓲𝓽𝓲', font=('arial', 25), fg='#013220')
header.place(x=145, y=10)
header.configure(bg='#FFFFFF')

header=tk.Label(gui, text='"There is divinity in the clouds."')
header.place(x=100, y=310)
header=tk.Label(gui, text='"Climate is what we expect, Weather is what we get."')
header.place(x=43, y=350)
header=tk.Label(gui, text='"To walk into nature is to witness a thousand miracles."')
header.place(x=40, y=390)

button=tk.Button(gui, text='☰', command=lambda: sidebar(Weather))
button.place(x=5, y=5)
button.configure(width=2, height=2)

button=tk.Button(gui, text='Your Air and how it affects you', command=AQIBang)
button.place(x=95, y=250)

button=tk.Button(gui, text='Water Quality Index', command=water)
button.place(x=130, y=450)

gui.mainloop()
