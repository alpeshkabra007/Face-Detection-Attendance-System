
from tkinter import *
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
import tkinter as tk

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

'''
ChooseSub = tk.Button(window, text="Choose Subject", command=chooseSubject  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=12  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
ChooseSub.place(x=230, y=480)
'''








def SearchByRollNumber():
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName=date+"_"+Hour+"-"+Minute+"-"+Second
    db_name=fileName+".db"
    fileName=fileName+".csv"
    rollNo=rollNo_entry.get()
    import sqlite3
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    import pandas as pd
    import numpy as np
    import os,csv
    df=pd.read_csv("commonFile.csv")
    df.dropna(thresh=1,inplace=True)
  
    
    df.to_sql("CETdata", conn, if_exists="replace")
    
    df=pd.read_sql_query("select * from CETdata where RollNo = {} ".format(rollNo), conn)

    import pandas as pd
    df.to_csv(fileName)
    
    res=fileName
    message3.configure(text=res)
    conn.commit()
    conn.close()
    import os
    os.remove(db_name)



label_rollNo=tk.Label(window, text="Search By RollNo",width=12  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold  underline')) 
label_rollNo.place(x=230, y=100)


rollNo_entry = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
rollNo_entry.place(x=430, y=100)


  
RollNoButton = tk.Button(window, text="Search ", command=SearchByRollNumber  ,fg="red"  ,bg="DarkOrange2"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
RollNoButton.place(x=600, y=100)



                
label3 = tk.Label(window, text="Open this file   ",width=12  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold')) 
label3.place(x=750, y=100)


message3 = tk.Label(window, text="" ,fg="green"   ,bg="DarkOrange2",activeforeground = "green",width=30  ,height=1  ,font=('times', 15, ' bold ')) 
message3.place(x=930, y=100)







day_label = tk.Label(window, text="Day",width=10  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
day_label.place(x=230, y=150)

day_entry = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
day_entry.place(x=405, y=150)

month_label = tk.Label(window, text="Month",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
month_label.place(x=580, y=150)

month_entry = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
month_entry.place(x=755, y=150)    

year_label = tk.Label(window, text="Year",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
year_label.place(x=930, y=150)

year_entry = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
year_entry.place(x=1105, y=150)    

day_label1 = tk.Label(window, text="Day",width=10  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
day_label1.place(x=230, y=190)

day_entry1 = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
day_entry1.place(x=405, y=190)

month_label1 = tk.Label(window, text="Month",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
month_label1.place(x=580, y=190)

month_entry1 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
month_entry1.place(x=755, y=190)    

year_label1 = tk.Label(window, text="Year",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
year_label1.place(x=930, y=190)

year_entry1 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
year_entry1.place(x=1105, y=190)    


def SearchByDate():
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName=date+"_"+Hour+"-"+Minute+"-"+Second
    db_name=fileName+".db"
    fileName=fileName+".csv"
    day=day_entry.get()
    month=month_entry.get()
    year=year_entry.get()
    day2=day_entry1.get()
    month2=month_entry1.get()
    year2=year_entry1.get()
    
    import sqlite3
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    import pandas as pd
    import numpy as np
    import os,csv
    df=pd.read_csv("commonFile.csv")
    df.dropna(thresh=1,inplace=True)
  
    date1=day+" "+month+" "+year
    date2=day2+" "+month2+" "+year2
    date_time = datetime.datetime.strptime(date1, '%d %m %Y')
    date_time2 = datetime.datetime.strptime(date2, '%d %m %Y')
    
    df.to_sql("CETdata", conn, if_exists="replace")
    
    df=pd.read_sql_query("select * from CETdata where Date Between  '{}'  and '{}' ".format((date_time.date()),(date_time2.date())), conn)
    #ans=df[(df['Date']<=date_time) & (df['Date'] <=date_time2)]    
    #df.to_sql("CETdata1", conn, if_exists="replace")
    #print(df)    
    #df=pd.read_sql_query("select * from CETdata1 where Date Between {} And {} ;".format(date1,date2), conn)
    #print(df)
    df.to_csv(fileName)


    import pandas as pd
    #df.to_csv(fileName)
    res=fileName
    message4.configure(text=res)
    conn.commit()
    conn.close()
    
    import os
    os.remove(db_name)
    
    
def SearchByDateAndRollNo():
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName=date+"_"+Hour+"-"+Minute+"-"+Second
    db_name=fileName+".db"
    fileName=fileName+".csv"
    day=day_entry2.get()
    month=month_entry2.get()
    year=year_entry2.get()
    rollNo=Date_rollNo_entry.get()
    import sqlite3
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    import pandas as pd
    import numpy as np
    import os,csv
    df=pd.read_csv("commonFile.csv")
    df.dropna(thresh=1,inplace=True)
  
    date1=day+" "+month+" "+year
    date_time_obj = datetime.datetime.strptime(date1, '%d %m %Y')

    df.to_sql("CETdata", conn, if_exists="replace")
    
    df=pd.read_sql_query("select * from CETdata where Date =  '{}'  and RollNo = {} ".format((date_time_obj.date()),rollNo), conn)
    #ans=df[(df['Date']==date1) & (df['RollNo'] == rollNo)]    
    #df.to_sql("CETdata1", conn, if_exists="replace")
    #print(df)    
    #df=pd.read_sql_query("select * from CETdata1 where Date Between {} And {} ;".format(date1,date2), conn)
    #print(df)
    df.to_csv(fileName)
    
    
    import pandas as pd
    #df.to_csv(fileName)
    res=fileName
    status_record.configure(text=res)
    conn.commit()
    conn.close()
    import os
    os.remove(db_name)
    


searchDate = tk.Button(window, text="Search By Date", command=SearchByDate  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
searchDate.place(x=230, y=230)


    
label_Date = tk.Label(window, text="Open this file ",width=15  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold')) 
label_Date.place(x=480, y=230)


message4 = tk.Label(window, text="" ,fg="green"   ,bg="DarkOrange2",activeforeground = "green",width=20  ,height=1  ,font=('times', 15, ' bold ')) 
message4.place(x=780, y=230)



###status = tk.Label(window, text="Open this file ",width=23  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold')) 
#status.place(x=620, y=750)


status_record = tk.Label(window, text="" ,fg="green"   ,bg="DarkOrange2",activeforeground = "green",width=20  ,height=1  ,font=('times', 15, ' bold ')) 
status_record.place(x=1000, y=330)

searchRecord = tk.Button(window, text="Access Record", command=SearchByDateAndRollNo  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
searchRecord.place(x=740, y=330)

Date_rollNo_entry = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
Date_rollNo_entry.place(x=530, y=330)
                
label_Date_Roll = tk.Label(window, text="Enter RollNO ",width=23  ,fg="maroon4"  ,bg="DarkOrange2"  ,height=1 ,font=('times', 15, ' bold')) 
label_Date_Roll.place(x=230, y=330)

day_label2 = tk.Label(window, text="Day",width=10  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
day_label2.place(x=230, y=300)

day_entry2 = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
day_entry2.place(x=405, y=300)

month_label2 = tk.Label(window, text="Month",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
month_label2.place(x=580, y=300)

month_entry2 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
month_entry2.place(x=755, y=300)    

year_label2 = tk.Label(window, text="Year",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
year_label2.place(x=930, y=300)

year_entry2 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
year_entry2.place(x=1105, y=300)    




'''



day_label4 = tk.Label(window, text="Day",width=10  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
day_label4.place(x=230, y=400)

day_entry4 = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
day_entry4.place(x=405, y=400)

month_label4 = tk.Label(window, text="Month",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
month_label4.place(x=580, y=400)

month_entry4 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
month_entry4.place(x=755, y=400)    

year_label4 = tk.Label(window, text="Year",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
year_label4.place(x=930, y=400)

year_entry4 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
year_entry4.place(x=1105, y=400)    

day_label5 = tk.Label(window, text="Day",width=10  ,height=1  ,fg="maroon4"  ,bg="DarkOrange2" ,font=('times', 15, ' bold ') ) 
day_label5.place(x=230, y=450)

day_entry5 = tk.Entry(window,width=10  ,bg="DarkOrange2" ,fg="maroon4",font=('times', 15, ' bold '))
day_entry5.place(x=405, y=450)

month_label5 = tk.Label(window, text="Month",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
month_label5.place(x=580, y=450)

month_entry5 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
month_entry5.place(x=755, y=450)    

year_label5 = tk.Label(window, text="Year",width=10  ,fg="maroon4"  ,bg="DarkOrange2"    ,height=1 ,font=('times', 15, ' bold ')) 
year_label5.place(x=930, y=450)

year_entry5 = tk.Entry(window,width=10  ,bg="DarkOrange2"  ,fg="maroon4",font=('times', 15, ' bold ')  )
year_entry5.place(x=1105, y=450)    


def SearchByDateAndSub():
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName=date+"_"+Hour+"-"+Minute+"-"+Second
    db_name=fileName+".db"
    fileName=fileName+".csv"
    day=day_entry4.get()
    month=month_entry4.get()
    year=year_entry4.get()
    day2=day_entry5.get()
    month2=month_entry5.get()
    year2=year_entry5.get()
    
    import sqlite3
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    import pandas as pd
    import numpy as np
    import os,csv
    df=pd.read_csv("commonFile.csv")
    df.dropna(thresh=1,inplace=True)
  
    date1=day+" "+month+" "+year
    date2=day2+" "+month2+" "+year2
    date_time = datetime.datetime.strptime(date1, '%d %m %Y')
    date_time2 = datetime.datetime.strptime(date2, '%d %m %Y')
    
    df.to_sql("CETdata", conn, if_exists="replace")
    
    df=pd.read_sql_query("select * from CETdata where Date Between  '{}'  and '{}' ".format((date_time.date()),(date_time2.date())), conn)
    #ans=df[(df['Date']<=date_time) & (df['Date'] <=date_time2)]    
    #df.to_sql("CETdata1", conn, if_exists="replace")
    #print(df)    
    #df=pd.read_sql_query("select * from CETdata1 where Date Between {} And {} ;".format(date1,date2), conn)
    #print(df)
    df.to_csv(fileName)


    import pandas as pd
    #df.to_csv(fileName)
    res=fileName
    message5.configure(text=res)
    conn.commit()
    conn.close()
    
    import os
    os.remove(db_name)
    

'''

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="maroon4"  ,bg="DarkOrange2"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=680, y=600)


window.mainloop()

