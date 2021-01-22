from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
from AddAircraft import *
from DeleteAircraft import *
from ViewAircrafts import *
from DeliverAircraft import *
from ReturnAircraft import *
# Add your own database name and password here to reflect in the code
conn = mysql.connector.connect(user='root', password=mypass, host='localhost', database='db')
cursor = conn.cursor()

root = Tk()
root.title("Aircraft Squadron")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("tejas.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="DarkSalmon",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Aircraft Squadron", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Aircraft Details",bg='black', fg='white', command=addAircraft)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Aircraft",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Aircraft List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Deliver Aircraft to IAF",bg='black', fg='white', command = deliverAircraft)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Aircraft",bg='black', fg='white', command = returnAircraft)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
