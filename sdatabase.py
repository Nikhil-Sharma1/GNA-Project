import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="NIKHIL@098sharma",
    database="testdb2"
    
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb2")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE users (email VARCHAR(255), pwd VARCHAR(255),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table[0])

# sqlStuff="INSERT INTO users (email,pwd) VALUES (%s,%s)"
# record1=("akankshamaurya0100@gmail.com","akanksha123")
# mycursor.execute(sqlStuff,record1)
# mydb.commit()

from tkinter import *
from tkcalendar import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg



def geti():
    count=0
    var1=loginent.get()       #entry box widget for username
    var2=passwordent.get()    #entry box widget for password
    mycursor.execute("SELECT username FROM users")
    myresult=mycursor.fetchall()

    for row in myresult:
        if(row[0]==var1):
            count=1
            
    mycursor.execute("SELECT pwd FROM users")
    myresult=mycursor.fetchall()

    for row in myresult:
        if(row[0]==var2):
            count=count+1
            print(count)   

    
    if count==2:

        frame1.pack_forget()
        
        frame2.pack_forget()
        f1.pack(padx=20,pady=70,side=LEFT,anchor="center")
        f2.pack(padx=20,pady=(70,0),side=TOP)
        f3.pack(padx=20,side=TOP)
        tmsg.showinfo("user Login","Login successful")
    if (count==1):
        tmsg.showinfo("user login","Check user id or password again ")

    if(count==0):

        tmsg.showinfo("user login","Please enter valid user id or password ")
        loginval.set('')
        passwordval.set('')
    

root=Tk()
root.geometry("450x450")
root.title("Python-Project")
root.configure(bg='#F5F5F5')
p12 = PhotoImage(file = 'Online_class_Logo2_2_400x200.png') 
  
# Setting icon of master window 
root.iconphoto(False, p12)
frame2=Frame(root,borderwidth=2)            #Adding Frame
frame2.pack(padx=23,pady=120,side=TOP)
photo=ImageTk.PhotoImage(file="Online_class_Logo2_2_400x200.png")  
lb=Label(frame2,image=photo)
lb.pack()



frame1=Frame(frame2)
frame1.pack(pady=20,padx=30)
loginval=StringVar()                                                                      
passwordval=StringVar()
label1=Label(frame1,text="Username",font="Montserrat 13 bold" )
label1.pack()
                                                                  
loginent=Entry(frame1,textvariable=loginval,borderwidth=4,font="Montserrat")     #loginent is the
loginent.pack(pady=20,padx=30,ipady=7,ipadx=16) 
label2=Label(frame1,text="Password ",font="Montserrat 13 bold")
label2.pack()            
passwordent=Entry(frame1,textvariable=passwordval,show="*",borderwidth=4,font="Montserrat")    
                                                             
passwordent.pack(pady=20,padx=30,ipady=7,ipadx=16)                                                           
Button(frame1,text="Click to login",command=geti,borderwidth=8,font="Montserrat 10 bold").pack(pady=(10,20)) 




def fun1():
    val=cal.get_date()
    print(val)
    
  
    
    if(val=='10/5/20' or val=='10/12/20' or val=='10/19/20' or val=='10/26/20'):
        f3.pack(padx=20,side=TOP)
        l1['text']="Monday"
        l1['fg']="black"
        l2['text']="10-11: MTH 705"
        l3['text']="11-12: CSE 205"
        l5['text']="04-05: CSE 000"
        l6['text']="04-05: PES 319"
        
        l4['text']="02-03: PEL 999"
        l2['bg']="#E08686"
        l6['bg']="#E08686"
                
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
    if(val=='10/6/20' or val=='10/13/20' or val=='10/20/20' or val=='10/27/20'):
        f3.pack(padx=20,side=TOP)
        l1['text']="Tuesday"
        l1['fg']="black"
        l2['text']="09-10: CSE 000"
        
        l3['text']="10-11: CSE 999"
        
        l4['text']="01-02: PEL 231"
        
        l5['text']="02-04: MTH 555"
      
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        l6.pack_forget()
        
    if(val=='10/7/20' or val=='10/14/20' or val=='10/21/20' or val=='10/28/20'):
        f3.pack(padx=20,side=TOP)
        l1['text']="Wednesday"
        l1['fg']="black"
        l2['text']="11-12: PES 319"
        
        l3['text']="02-03: MGN 231"
        
        l4['text']="03-04: ASP 380"
        
        l5['text']="04-05: RES 760"
        l6['text']="05-06: MTH 444"
        l6.pack(padx=20,pady=20,side=TOP)
        l6['bg']="#E08686"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        
    if(val=='10/8/20' or val=='10/15/20' or val=='10/22/20' or val=='10/29/20' or val=='10/1/20'):
        f3.pack(padx=20,side=TOP)
        l1['text']="Thursday"
        l1['fg']="black"
        l2['text']="10-12: CSE 250"
        
        l3['text']="01-02: PAS 487"
        
        l4['text']="03-04: CSE 320"
        
        l5['text']="04-05: CSE 211"
        l2['bg']="#E08686"
        l6.pack_forget()
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
     
        
        
    if(val=='10/9/20' or val=='10/16/20' or val=='10/23/20' or val=='10/30/20' or val=='10/2/20'):
        f3.pack(padx=20,side=TOP)
        l1['text']="Friday"
        l1['fg']="black"
        l2['text']="10-11: CSE 700"
        
        l3['text']="11-12: CSE 999"
        
        l4['text']="12-01: PEL 231"
        
        l5['text']="02-04: PES 320"
        l6['text']="05-06: MTH 440"
        l6.pack(padx=20,pady=20,side=TOP)
        l6['bg']="#E08686"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        
    if(val=='10/10/20' or val=='10/17/20' or val=='10/24/20' or val=='10/3/20'):
        f3.pack_forget()
        l1['text']="Saturday"
        l1['fg']="#CC5D5D"
        
    if(val=='10/11/20' or val=='10/18/20' or val=='10/25/20' or val=='10/4/20'):
        f3.pack_forget()
        l1['text']="Sunday"
        
        l1['fg']="#CC5D5D"

def openFile():
    import client
        
f1=Frame(root,bg="#F5F5F5")

f2=Frame(root,bg="#F5F5F5")

f3=Frame(root,bg="#F5F5F5")



cal=Calendar(f1,selectmode="day",year=2020,month=10,day=5,font="Montserrat 11")
cal.pack( pady=30,padx=30)

b1= Button(f1,text="Get Timetable",fg="#000",bg="#E08686",font="Montserrat 10",borderwidth=0,command=fun1,pady=5,padx=10)
b1.pack(padx=20,pady=20)

l1=Label(f2,text="Monday", font="Montserrat 18",bg="#F5F5F5")
l1.pack(padx=20,pady=40)

l2=Button(f3,text="10-11 : MTH 705",bg="#E08686",padx=200,pady=10,command=lambda:openFile() ,borderwidth=0,font="Montserrat 11")
l2.pack(padx=20,pady=20,side=TOP)

l3=Button(f3,text="11-12 : CSE 205",bg="#E08686",padx=200,pady=10,command=lambda:openFile() ,borderwidth=0,font="Montserrat 11")
l3.pack(padx=20,pady=20,side=TOP)

l4=Button(f3,text="02-03 : PEL 999",bg="#E08686",padx=195,pady=10,command=lambda:openFile() , borderwidth=0,font="Montserrat 11")
l4.pack(padx=20,pady=20,side=TOP)

l5=Button(f3,text="04-05 : CSE 000",bg="#E08686",padx=193,pady=10,command=lambda:openFile() ,borderwidth=0,font="Montserrat 11")
l5.pack(padx=20,pady=20,side=TOP)

l6=Button(f3,text="05-06 : PES 319",bg="#E08686",padx=193,pady=10,command=lambda:openFile() ,borderwidth=0,font="Montserrat 11")
l6.pack(padx=20,pady=20,side=TOP)
















root.mainloop()