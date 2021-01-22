from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

# Add your own database name and password here to reflect in the code
conn = mysql.connector.connect(user='root', password=mypass, host='localhost', database='db')
cursor = conn.cursor()

# Enter Table Names here
deliverTable = "aircrafts_delivered" 
aircraftTable = "aircrafts"
    
#List To store all Aircraft Nos
allMno = [] 

def deliver():
    
    global deliverBtn,labelFrame,lb1,aircraftInfo1,aircraftInfo2,quitBtn,root,Canvas1,status
    
    mno = aircraftInfo1.get()
    deliverto = inf2.get()

    deliverBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractMno = "select mno from "+aircraftTable
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
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Aircraft ModelNo not present")
    except:
        messagebox.showinfo("Error","Can't fetch Aircraft ModelNO")
    
    deliverSql = "insert into "+deliverTable+" values ('"+mno+"','"+deliverto+"')"
    show = "select * from "+deliverTable
    
    updateStatus = "update "+aircraftTable+" set status = 'delivered' where mno = '"+mno+"'"
    try:
        if mno in allMno and status == True:
            cur.execute(deliverSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Aircraft Delivered Successfully")
            root.destroy()
        else:
            allMno.clear()
            messagebox.showinfo('Message',"Aircraft Already Delivered")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(mno)
    print(deliverto)
    
    allMno.clear()
    
def deliverAircraft(): 
    
    global deliverBtn,labelFrame,lb1,aircraftInfo1,aircraftInfo2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Aircraft Squadron")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="GreenYellow")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="Khaki",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Deliver Aircraft", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Model No
    lb1 = Label(labelFrame,text="Model No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Delivered To IAF
    lb2 = Label(labelFrame,text="Delivered To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Deliver Button
    deliverBtn = Button(root,text="Deliver",bg='#d1ccc0', fg='black',command=deliver)
    deliverBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
