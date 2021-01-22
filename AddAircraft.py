from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

# Add your own database name and password here to reflect in the code
conn = mysql.connector.connect(user='root', password=mypass, host='localhost', database='db')
cursor = conn.cursor()

aircraftTable = "aircrafts" 
def aircraftRegister():
    
    mno = aircraftInfo1.get()
    name = aircraftInfo2.get()
    manufac = aircraftInfo3.get()
    status = aircraftInfo4.get()
    status = status.lower()
    
    insertAircrafts = "insert into "+aircraftTable+" values('"+mno+"','"+name+"','"+manufac+"','"+status+"')"
    try:
        cur.execute(insertAircrafts)
        con.commit()
        messagebox.showinfo('Success',"Aircraft added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(mno)
    print(name)
    print(manufac)
    print(status)


    root.destroy()
    
def addAircraft(): 
    
    global aircraftInfo1,aircraftInfo2,aircraftInfo3,aircraftInfo4,Canvas1,con,cur,aircraftTable,root
    
    root = Tk()
    root.title("Aircraft Squadron")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="Bisque")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="Gold",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Aircrafts", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Model No
    lb1 = Label(labelFrame,text="Model No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    aircraftInfo1 = Entry(labelFrame)
    aircraftInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    aircraftInfo2 = Entry(labelFrame)
    aircraftInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Aircraft manufacturer
    lb3 = Label(labelFrame,text="Manufac : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    aircraftInfo3 = Entry(labelFrame)
    aircraftInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Aircraft Status
    lb4 = Label(labelFrame,text="Status(Avail/del) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    aircraftInfo4 = Entry(labelFrame)
    aircraftInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='GainsBoro', fg='black',command=aircraftRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='LightYellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
