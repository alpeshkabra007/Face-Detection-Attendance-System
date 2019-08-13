
from tkinter import *
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

import csv
import os.path
from os import path
flag=0
if(not path.exists('commonFile.csv')):
    flag=1
    with open('commonFile.csv','w') as newFile:
        newFileWriter=csv.writer(newFile)
        fieldnames = ('RollNo', 'Name', 'Branch','Subject' ,'Date', 'Time')
        writer = csv.DictWriter(newFile, fieldnames=fieldnames)
        writer.writeheader()


window = tk.Tk()
window.title("Face_Recognizer_Attendance")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


img = ImageTk.PhotoImage(Image.open("E:\\class.jpg"))
label = tk.Label(window, image = img)
label.pack(side = "bottom", fill = "both", expand = "yes")


values=[]
def chooseSubject():
    
    root=Tk()
    sizex = 200
    sizey = 200
    posx  = 40
    posy  = 20
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    itemsforlistbox=['Real Time System','Mobile Computing','Image Processing','Distributed System']

    def CurSelect(evt):
        values.append(str((mylistbox.get(mylistbox.curselection()))))
        #print(value)

    mylistbox=Listbox(root,width=60,height=10,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelect)
    mylistbox.place(x=32,y=90)

    for items in itemsforlistbox:
        mylistbox.insert(END,items)
    root.mainloop()

ChooseSub = tk.Button(window, text="Choose Subject", command=chooseSubject  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=12  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
ChooseSub.place(x=270, y=300)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=680, y=600)



def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['RollNo','Name','Branch','Subject','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            RollNo, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 35):
                confi=(100-conf)*1.27
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['RollNo'] == RollNo]['Name'].values
                if(confi>=70):
                    tt=aa[0]+" is pesent "
                stream=df.loc[df['RollNo'] == RollNo]['Branch'].values
                branch=""
                if(len(stream)>0):
                    branch=stream[0]
                date = datetime.datetime.fromtimestamp(ts)
                #result=[RollNo,aa[0],branch,subj,date,timeStamp]
                subj=""
                if(len(values)>0):
                    subj=values[0]
                attendance.loc[len(attendance)] = [RollNo,aa[0],branch,subj,date.date(),timeStamp]
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
                #conn1 = sqlite3.connect('AttendanceData.db')
                #cur = conn1.cursor()
                #cur.execute('INSERT INTO users (id,name,date,tim) VALUES (?,?,?,?)', result)
                
                
            else:
                RollNo='Unknown'                
                tt=str(RollNo)
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
            '''if(conf > 75):
                size_unknown=len(os.listdir("ImagesUnknown"))
                noOfFile=size_unknown+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])'''            
            
            
                    
        attendance=attendance.drop_duplicates(subset=['RollNo'],keep='first')
        #cur.execute('DELETE FROM units A WHERE EXISTS (SELECT * FROM units B WHERE A.id = B.id)')
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    message2.configure(text= res)
    import csv
    with open('commonFile.csv','a+') as newFile:
        newFileWriter=csv.writer(newFile)
        with open(fileName, 'r') as f:
            reader = csv.reader(f)
            ct=1
            #if(flag==1):
                #ct=2
            for row in reader:
                if(ct>1):
                    newFileWriter.writerow(row)
                ct=ct+1
        #import os
        #os.remove(fileName)


trackImg = tk.Button(window, text="Mark Attendance", command=TrackImages  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=22,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=440, y=300)

                
lbl3 = tk.Label(window, text="Attendance Status",width=15  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold  underline')) 
lbl3.place(x=275, y=400)


message2 = tk.Label(window, text="" ,fg="green"   ,bg="DarkOrange2",activeforeground = "green",width=35  ,height=4  ,font=('times', 15, ' bold ')) 
message2.place(x=490, y=400)


window.mainloop()
