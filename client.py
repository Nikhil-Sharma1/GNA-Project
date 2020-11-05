
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="NIKHIL@098sharma",
    database="testdb2"    
)

mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb2")

#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#     print(db)

#mycursor.execute("CREATE TABLE users (username VARCHAR(255), pwd VARCHAR(255),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table[0])

# sqlStuff="INSERT INTO users (username,pwd) VALUES (%s,%s)"
# record1=("akanksha","12345")
# mycursor.execute(sqlStuff,record1)
# mydb.commit()

# sqlStuff="INSERT INTO users (username,pwd) VALUES (%s,%s)"
# record1=("gaurav","gaurav")
# mycursor.execute(sqlStuff,record1)
# mydb.commit()


# sqlStuff="INSERT INTO users (username,pwd) VALUES (%s,%s)"
# record1=("nikhil","nikhil")
# mycursor.execute(sqlStuff,record1)
# mydb.commit()





import tkinter.messagebox as tmsg
import tkinter
from tkinter import *
root=tkinter.Tk()
from tkinter import messagebox
root.title("Client")
username=" "

topFrame=tkinter.Frame(root,relief=SUNKEN)
lblname=tkinter.Label(topFrame, text="Name: ").pack(side=tkinter.LEFT)

ent=StringVar()

entName=tkinter.Entry(topFrame,textvariable=ent)

entName.pack(side=tkinter.LEFT)



btnConnect=tkinter.Button(topFrame, text="Connect",command=lambda: connect())
btnConnect.pack(side=tkinter.LEFT)
topFrame.pack(anchor=NW,pady=(5,0))

clientFrame = tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=5,relief=SUNKEN)
lblLine = tkinter.Label(clientFrame, text="CLIENT LIST")
lblLine.pack(side=tkinter.TOP)
scrollBar = tkinter.Scrollbar(clientFrame)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
TkDisplay = tkinter.Text(clientFrame,height=100,width=20)
TkDisplay.pack(side=tkinter.LEFT, fill=tkinter.Y, padx=(5,0))
scrollBar.config(command=TkDisplay.yview)
TkDisplay.config(yscrollcommand=scrollBar.set,background="white",highlightbackground="black",state="disabled")
clientFrame.pack(side=LEFT,pady=(5,0))

leftFrame=tkinter.Frame(root,height=60,width=900,bg="grey",borderwidth=4,relief=SUNKEN)
leftDisplay=tkinter.Label(leftFrame,text="FILE WINDOW",height=2).pack()
btn=tkinter.Button(leftFrame,text="Take quiz",command=lambda:openQuizWindow()).pack(side=LEFT,anchor=SE)
cf=tkinter.Button(leftFrame, text="Leave Class",command=lambda:closewindow()).pack(side=RIGHT,anchor=SW)
leftFrame.pack(side=RIGHT,padx=50)
T= tkinter.Text(leftFrame, height=40, width=100)
T.pack(side=LEFT,padx=0,pady=15)

def closewindow():
    MsgBox = tkinter.messagebox.askquestion ('Exit Application','Are you sure you want to leave the class',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tkinter.messagebox.showinfo('Stay Back')

def openQuizWindow():  
    import srv 

displayFrame=tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=5,relief=SUNKEN)
lblLine=tkinter.Label(displayFrame, text="PUBLIC CHAT").pack()
scrollbar=tkinter.Scrollbar(displayFrame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tkDisplay=tkinter.Text(displayFrame,height=50,width=35)
tkDisplay.pack(side=tkinter.LEFT,fill=tkinter.Y,padx=(5,0))
tkDisplay.tag_config("Enter your message",foreground="blue")
scrollbar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollbar.set, background="white",highlightbackground="white",state="disabled")
displayFrame.pack(anchor=NW,pady=(5,0))


bottomFrame=tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=5,relief=SUNKEN)
tkMessage=tkinter.Text(bottomFrame,height=3,width=35)
tkMessage.pack(side=tkinter.LEFT,padx=(5,13),pady=(5,10))
tkMessage.config(highlightbackground="black",state="disabled")
tkMessage.bind("<Return>",(lambda event:getChatMessage(tkMessage.get("1.0",tkinter.END))))
bottomFrame.pack(anchor=NW,pady=(2,0))

import socket

from tkinter import messagebox

import threading
def connect():
    count=0   

    global username
    if len(entName.get())<1:
        tkinter.messagebox.showerror(title="ERRoR!!!",message="You must enter your first name")
    else:
        mycursor.execute("SELECT username FROM users")
        myresult=mycursor.fetchall()

        for row in myresult:
            if(row[0]==entName.get()):
                username=entName.get()
                connect_to_server(username)
                count=1
    if(count==0):
       tmsg.showinfo("user login","Check username")
                





        
    


def connect_to_server(name):
   
    global client, HOST_ADDR, HOST_PORT
    client=None
    HOST_ADDR="127.0.0.1"
    HOST_PORT=6537
    
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    client.connect((HOST_ADDR,HOST_PORT))
   
    client.send(bytes(name,"utf8"))
    entName.config(state=tkinter.DISABLED)
    btnConnect.config(state=tkinter.DISABLED) 
    tkMessage.config(state=tkinter.NORMAL)
        
        
    threading._start_new_thread(receive_message_from_server,(client,"m"))
   
        
def receive_message_from_server(sck,m):
    global from_server
    while True:
        from_server=sck.recv(4096)
        if not from_server:
            break
        text_chat=tkDisplay.get("1.0",tkinter.END).strip()
        text_user=tkDisplay.get("1.0",tkinter.END).strip()
        tkDisplay.config(state=tkinter.NORMAL)
        TkDisplay.config(state=tkinter.NORMAL)
        if len(text_user)<1 and len(text_chat)<1:
            print(from_server.decode("utf-8"))
            if "-" in from_server.decode("utf-8") or "exit" in from_server.decode("utf-8") :
                tkDisplay.insert(tkinter.END,from_server.decode("utf-8"))
                tkDisplay.insert(tkinter.END,"\n")
            else:
                TkDisplay.insert(tkinter.END,from_server.decode("utf-8"))
        else:
            if "-" in from_server.decode("utf-8"):
                print(from_server.decode("utf-8"))
                tkDisplay.insert(tkinter.END,from_server.decode("utf-8"))
                # tkDisplay.insert(tkinter.END,"\n")
            else:
                TkDisplay.insert(tkinter.END,from_server.decode("utf-8"))
                            
        tkDisplay.config(state=tkinter.DISABLED)
        tkDisplay.see(tkinter.END)
        TkDisplay.config(state=tkinter.DISABLED)
        TkDisplay.see(tkinter.END)
    sck.close()
    root.destroy()
    
    
    
def getChatMessage(msg):
    msg=msg.replace('\n', '')
    texts=tkDisplay.get("1.0", tkinter.END).strip()
    
    tkDisplay.config(state=tkinter.NORMAL)
    if(texts == "chavi->start quiz"):
        import srv
     
    if len(texts)<1:
        tkDisplay.insert(tkinter.END,"You->"+ msg+"\n","tag_your_message")
    else:
        tkDisplay.insert(tkinter.END, "You->"+msg+"\n","tag_your_message")
        
    tkDisplay.config(state=tkinter.DISABLED)
    send_message_to_server(msg)

    tkDisplay.see(tkinter.END)
    tkMessage.delete('1.0',tkinter.END) 
    
def send_message_to_server(msg):
    client.send(msg.encode())
    if msg=="exit":
        client.close()
        root.destroy()
    print("sending message")
            


root.mainloop()