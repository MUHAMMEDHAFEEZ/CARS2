from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\cars_sara\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def check():
    if entry_user.get()=="sara" and entry_pass.get()=="123":
        LOGIN.destroy()
        
#new_invice()
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "sara"
    phone = "0000-0000-000"
    subtotal = sum(item[1] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
   
    new_invoice()    


def enter_data(descz,pricez):
    
    # Create Table
    conn = sqlite3.connect('data1.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS cars_data 
            (descz TEXT, pricez FLOAT )
    '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO cars_data ( descz, pricez) VALUES 
    (?,?)'''
    data_insert_tuple = (descz, pricez)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
 

window = Tk()

window.geometry("1440x950+0+0")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#create  a tree 
columns = ('desc', 'price')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.place(x=164,
    y=733,
    width=1112,
    height=270)

#button tree new invo
button_tree_new= customtkinter.CTkButton(master=window,
                                 #text="LOGIN",
                                 width=120,
                                 height=93,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=0,
                                 text="NEW",
                                 command=lambda: new_invoice())
button_tree_new.place(x=1296,y=730)


#button tree gen 
button_tree_GEN= customtkinter.CTkButton(master=window,
                                 #text="LOGIN",
                                 width=120,
                                 height=93,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=0,
                                 text="GENERATE",
                                 command=lambda: generate_invoice())
button_tree_GEN.place(x=1296,y=840)

invoice_list = []

# cars 

def add_car():
         desc = "lamborghini EVO"
         price = 1200.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car1():
         desc = "BMW Z4"
         price = 1000.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car2():
         desc = "Ferrari F8 tirbuto"
         price = 1600.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car3():
         desc = "lamborghini Revuelto"
         price = 1600.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car4():
         desc = "ferrari SF90"
         price = 1300.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car5():
         desc = "ferrari 812"
         price = 1300.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car6():
         desc = "Lamborghini Urus"
         price = 900.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
def add_car7():
         desc = "lBMW X1"
         price = 900.00
         invoice_item = [ desc, price]
         tree.insert('',0, values=invoice_item)
         enter_data(desc,price)
         invoice_list.append(invoice_item)
    
 

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    512.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car7(),
    relief="flat"
)
button_1.place(
    x=1185.0,
    y=634.0,
    width=187.0,
    height=38.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1266.0,
    509.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car6(),
    relief="flat"
)
button_2.place(
    x=800.0,
    y=634.0,
    width=187.0,
    height=38.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    894.0,
    509.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car5(),
    relief="flat"
)
button_3.place(
    x=428.0,
    y=634.0,
    width=187.0,
    height=38.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    522.0,
    509.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car4(),
    relief="flat"
)
button_4.place(
    x=79.0,
    y=634.0,
    width=187.0,
    height=38.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    168.0,
    509.0,
    image=image_image_5
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car3(),
    relief="flat"
)
button_5.place(
    x=1185.0,
    y=285.0,
    width=187.0,
    height=38.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1271.0,
    162.0,
    image=image_image_6
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car2(),
    relief="flat"
)
button_6.place(
    x=797.0,
    y=285.0,
    width=187.0,
    height=38.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    903.0,
    164.0,
    image=image_image_7
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car1(),
    relief="flat"
)
button_7.place(
    x=422.0,
    y=285.0,
    width=187.0,
    height=38.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    527.0,
    164.0,
    image=image_image_8
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_car(),
    relief="flat"
)
button_8.place(
    x=115.0,
    y=285.0,
    width=187.0,
    height=38.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    193.0,
    164.0,
    image=image_image_9
)
LOGIN = Frame( window)

# Create a photoimage object of the image in the path
# 1440x950
LOGIN.place(x=0,y=0,width=1440,height=950)
LOGIN.configure(background="white")
LOGIN_IM = Image.open(r"C:\Users\Mohammed Hafeez\Downloads\Image11.png")
test_LOGIN = ImageTk.PhotoImage(LOGIN_IM)
LOGOIN = Label(LOGIN,background="white",image=test_LOGIN).place(
    x=156,
    y=295,
    
)


LOGIN_IM_frame = Image.open(r"C:\Users\Mohammed Hafeez\Downloads\Image33.png")
test_LOGIN_frame = ImageTk.PhotoImage(LOGIN_IM_frame)
LOGOIN = Label(LOGIN,background="white",image=test_LOGIN_frame).place(
    x=730,
    y=218,
    
)

login = Image.open(r"C:\Users\Mohammed Hafeez\Downloads\Login.png")
test_login = ImageTk.PhotoImage(login)
LOGOIN = Label(LOGIN,background="white",image=test_login).place(
    x=885,
    y=241,
    
)

entry_user = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text="USERNAME",
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               
                               width=315,
                               height=49,
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_user.place(x=765,y=336)

entry_pass = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text="Password",
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               width=315,
                               height=51,
                               show="*",
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_pass.place(x=765,y=434)

button_login = customtkinter.CTkButton(master=LOGIN,
                                 #text="LOGIN",
                                 width=144.62,
                                 height=42.4,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=20,
                                 text="LOGIN",
                                 command=check)
button_login.place(x=850,y=510)

#LOGO.image = test

w = Frame( window)
# Create a photoimage object of the image in the path
w.place(x=0,y=0,width=1280,height=832)
image1 = Image.open(r"C:\Users\Mohammed Hafeez\Downloads\MacBook Air - aa1.png")
test = ImageTk.PhotoImage(image1)
LOGO = Label(w,image=test).pack()
#LOGO.image = test

window.after(2000,lambda:w.destroy())



window.resizable(False, False)
window.mainloop()
