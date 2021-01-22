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


def deleteAircraft():
    
    mno = aircraftInfo1.get()
    
    deleteSql = "delete from "+aircraftTable+" where mno = '"+mno+"'"
    deleteDeliver = "delete from "+deliverTable+" where mno = '"+mno+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteDeliver)
        con.commit()
        messagebox.showinfo('Success',"Aircraft Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Model NO")
    

    print(mno)

    aircraftInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global aircraftInfo1,aircraftInfo2,aircraftInfo3,aircraftInfo4,Canvas1,con,cur,aircraftTable,root
    
    root = Tk()
    root.title("Aircraft Squadron")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="ForestGreen")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="GoldenRod",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Aircraft", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Model No to Delete
    lb2 = Label(labelFrame,text="Model No : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    aircraftInfo1 = Entry(labelFrame)
    aircraftInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteAircraft)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
