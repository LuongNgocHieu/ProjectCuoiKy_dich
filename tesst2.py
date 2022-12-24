from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator
root=Tk()
root.title('GOOGLE TRANSLATE')
root.geometry("640x960")
root.iconbitmap('logo.ico')

load=Image.open('bg2.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root, image=render)
img.place(x=0,y=0)

name=Label(root,text="Translator",fg="#FF83FA",bd=0,bg="#98F5FF")
name.config(font=("Transformers Movie",32))
name.pack(pady=10)

box=Text(root,width=64,height=4,font=("ARIAL",12))
box.pack(pady=170)
b1=Text(root,width=64,height=4,font=("ARIAL",12))
b1.pack(pady=10)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)
    b1.delete(1.0, END)

def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    m=Translator()
    h=m.translate(INPUT,src="vi",dest="ja")
    q=h.text
    b1.insert(END,q)

clear_button=Button(button_frame,text= " Clear all your words",font=("MONOSPACE",8,'bold','italic'),fg="#FF83FA",bg="#98F5FF",command=clear)
clear_button.place(x=47,y=335)
trans_button=Button(button_frame,text= " TRANSLATE NOW !!!",font=("MONOSPACE",8,'bold','italic'),fg="#FF83FA",bg="#98F5FF",command=translate)
trans_button.place(x=491,y=335)

root.mainloop()
