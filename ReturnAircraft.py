from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

# Add your own database name and password here to reflect in the code
conn = mysql.connector.connect(user='root', password=mypass, host='localhost', database='db')
cursor = conn.cursor()

# Enter Table Names here
#Deliver Table
deliverTable = "aircrafts_delivered" 
#Aircraft Table
aircraftTable = "aircrafts" 

#List To store all Model Nos
allMno = [] 

def returnn():
    
    global SubmitBtn,labelFrame,lb1,aircraftInfo1,quitBtn,root,Canvas1,status
    
    mno = aircraftInfo1.get()

    extractMno = "select mno from "+deliverTable
    try:
        cur.execute(extractMno)
        con.commit()
        for i in cur:
            allMno.append(i[0])
        
        if mno in allMno:
            checkAvail = "select status from "+aircraftTable+" where mno = '"+mno+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'delivered':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Aircraft Modelno not present")
    except:
        messagebox.showinfo("Error","Can't fetch Aircraft Modelno")
    
    
    deliverSql = "delete from "+deliverTable+" where mno = '"+mno+"'"
  
    print(mno in allMno)
    print(status)

    updateStatus = "update "+aircraftTable+" set status = 'avail' where mno = '"+mno+"'"
    try:
        if mno in allMno and status == True:
            cur.execute(deliverSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Aircraft Returned Successfully")
        else:
            allMno.clear()
            messagebox.showinfo('Message',"Please check the aircraft ModelNo")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allMno.clear()
    root.destroy()
    
def returnAircraft(): 
    
    global aircraftInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Aircraft Squadron")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="DarkCyan")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="Pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Aircraft", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Model No to Delete
    lb1 = Label(labelFrame,text="Model No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    aircraftInfo1 = Entry(labelFrame)
    aircraftInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
