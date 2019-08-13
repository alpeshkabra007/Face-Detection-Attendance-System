
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
def chooseBranch():
    
    root=Tk()
    sizex = 200
    sizey = 200
    posx  = 40
    posy  = 20
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    itemsforlistbox=['CSE','EE','ECE','IT']

    def CurSelect(evt):
        values.append(str((mylistbox.get(mylistbox.curselection()))))
        #print(value)

    mylistbox=Listbox(root,width=60,height=10,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelect)
    mylistbox.place(x=32,y=90)

    for items in itemsforlistbox:
        mylistbox.insert(END,items)
    root.mainloop()


def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#recognizer = #$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"
    message.configure(text= res)

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

'''
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
'''
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    RollNo=(txt.get())
    name=(txt2.get())
    branch=""
    if(len(values)>0):
        branch=values[0]
        values[:] = []
    if(is_number(RollNo) and name.isalpha() and branch.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                sampleNum=sampleNum+1
                cv2.imwrite("TrainingImage\ "+name +"."+RollNo +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('frame',img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for RollNo : " + RollNo +" Name : "+ name
        row = [RollNo , name , branch]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        #conn = sqlite3.connect('database.db')
        #c = conn.cursor()
        #c.execute('INSERT INTO users (id,name) VALUES (?,?)', row)

        
        message.configure(text= res)
        TrainImages()
    else:
        if(is_number(RollNo)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)

    
lbl = tk.Label(window, text="Enter Roll No.",width=12  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
lbl.place(x=220, y=300)

txt = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
txt.place(x=400, y=300)

lbl2 = tk.Label(window, text="Enter your Name",width=12  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
lbl2.place(x=570, y=300)

txt2 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
txt2.place(x=800, y=300)

lbl3 = tk.Label(window, text="Current Status : ",width=12  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold underline ')) 
lbl3.place(x=220, y=400)

message = tk.Label(window, text="" ,bg="DarkOrange2"  ,fg="green"  ,width=25  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=400, y=400)

takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=430, y=350)
#trainImg = tk.Button(window, text="Train Model", command=TrainImages  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
#trainImg.place(x=1200, y=100)


ChooseBranch = tk.Button(window, text="Choose Branch", command=chooseBranch  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=12  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
ChooseBranch.place(x=220, y=350)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=680, y=600)


window.mainloop()
