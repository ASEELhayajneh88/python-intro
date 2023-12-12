import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import messagebox
from PIL import ImageTk,Image

root= tk.Tk()
root.geometry('800x600+0+0')
root.title('Roaster and Coffee')
photo = PhotoImage(fille="C:\Users\computer\Downloads\tk.png")


def delete_pagees():
    for frame in main_frame.winfo_children():
        frame.destroy()

    

def indicate(lb, page):
    lb.config(bg='brown')
    delete_pagees()
    page()
    
    
def home_page():
    home_frame= tk.Frame(main_frame)

    lb= tk.Label(home_frame, text='ROASTER & AL-ASEEL COFFEE\n\n\n Roasted And Al-Aseel Coffee.Unique, \nHere You Will Find Everything That Is Delicious And Suits Your High Taste.\n' , font=('Bold,50'),)    
    lb.pack()
    
    home_frame.pack(pady=20)
    

def menu_page():
    menu_frame= tk.Frame(main_frame)

    # Table creation
    tree = ttk.Treeview(menu_frame, height=20,columns=("item", "price"), show="headings")
    tree.heading("item", text="Item")
    tree.heading("price", text="Price")

    # Example data
    coffee_items = [
        ("Arabian Coffee", "5jd"),
        ("Turkish Coffee",   "4.5jd"),
        ("Nescafee",   "8jd"),
        ("Espresso",   "3.5jd"),
        ("Iced Coffee",   "3.5jd"),
        ("Hot Chocolate", "2.5jd"),
        ("Tea", "2jd"),
        
    ]

    # Add items to table
    for item in coffee_items:
        tree.insert("", "end", values=item)

    # Scrollbar for table
    scroll_bar = ttk.Scrollbar(menu_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll_bar.set)

    # Display table and scrollbar
    tree.pack(side="left", fill="both", expand=True)
    scroll_bar.pack(side="right", fill="y")
    #buy item from table
    menu_frame.pack(pady=20)

    
      
    
    
def contact_page():
       
    
    # contact frame
    contact_frame= tk.Frame(main_frame)

    # labels and entry for name, phone, email, and address
    tk.Label(contact_frame, text='Name:',font=50).pack()
    name_var = tk.StringVar()
    tk.Entry(contact_frame, textvariable=name_var,width=80).pack()

    tk.Label(contact_frame, text='Phone:',font=50).pack()
    phone_var = tk.StringVar()
    tk.Entry(contact_frame, textvariable=phone_var,width=80).pack()

    tk.Label(contact_frame, text='Email:',font=50).pack()
    email_var = tk.StringVar()
    tk.Entry(contact_frame, textvariable=email_var,width=80).pack()

    tk.Label(contact_frame, text='Address:',font=50).pack()
    address_var = tk.StringVar()
    tk.Entry(contact_frame, textvariable=address_var,width=80).pack()
    # submit button
    submit_button = tk.Button(contact_frame, text='Submit',font=50,command=lambda: submit_contact(name_var,phone_var,email_var,address_var))
    submit_button.pack()
    submit_button.configure(command=lambda: submit_contact(name_var,phone_var, email_var, address_var))
    # display contact frame
    contact_frame.pack(pady=20)
    def submit_contact(name_var, phone_var, email_var,
                       address_var):
        # get values from entry
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()
        messagebox.showinfo('Contact Added', 'Contact added to contacts list')
    contact_frame.pack(pady=20)

    
      
  
def about_page():
    about_frame= tk.Frame(main_frame)
    #add grid
    layout= tk.Frame(about_frame)
    layout.pack()
    # add labels
    tk.Label(layout, text='About US',font=50).pack()
    tk.Label(layout, text='What Makes Us Special.',font=50).pack()
    tk.Label(layout, text='Roasted And Aseel Coffee Will Take You To A Great Taste. \nYou Will Taste Coffee And Chocolate With Its Origins, Constantly Developing In Our Business\n, Proud To Provide High Quality Coffee And Many Products That Suit Your High Taste.\n\n',font=50).pack()
    tk.Label(layout, text='Our Services',font=90).pack()
    tk.Label(layout, text='Innovating products and developing production without compromising on the quality\n of the usual taste that we committed to providing from the beginning, while leaving a positive contribution to our society and continuing to continue.\n With every cup of coffee, we present to you the glass’s distinctive commercial and technological\n journey with experiences and expertise.',font=50).pack()
  
    about_frame.pack(pady=20)






    # lb= tk.Label(about_frame,
    # text='What Makes Us Special?\n\n\n\nRoasted And Aseel Coffee Will Take You To A Great Taste. \nYou Will Taste Coffee And Chocolate With Its Origins, Constantly Developing In Our Business\n, Proud To Provide High Quality Coffee And Many Products That Suit Your High Taste.', font=('Bold,50'))
    # lb.pack()
    
    # about_frame.pack(pady=20)
    
# def order_page():

            





   


options_frame= tk.Frame(root, bg='#c3c3c3')

home_btn= tk.Button(options_frame, text='Home',font=('Bold',15),fg='brown', bg='#c3c3c3',bd=0,command=lambda:indicate(home_indicate,home_page))

home_btn.place(x=10,y=50)
home_indicate= tk.Label(options_frame, text='', bg='brown' )
home_indicate.place(x=3,y=50, width=5, height=40)





menu_btn= tk.Button(options_frame, text='Menu',font=('Bold',15),fg='brown',bg='#c3c3c3',bd=0,command=lambda:indicate(menu_indicate,menu_page),)
menu_btn.place(x=10,y=100)
menu_indicate=tk.Label(options_frame,text='',bg='brown')
menu_indicate.place(x=3,y=100, width=5, height=40)

contact_btn= tk.Button(options_frame, text='Contact',font=('Bold',15),fg='brown',bg='#c3c3c3',bd=0,command=lambda:indicate(contact_indicate,contact_page))
contact_btn.place(x=10,y=150)
contact_indicate=tk.Label(options_frame,text='',bg='brown')
contact_indicate.place(x=3,y=150, width=5, height=40)

about_btn= tk.Button(options_frame, text='About',font=('Bold',15),fg='brown',bg='#c3c3c3',bd=0,command=lambda:indicate(about_indicate,about_page),)
about_btn.place(x=10,y=200)
about_indicate=tk.Label(options_frame,text='',bg='brown')
about_indicate.place(x=3,y=200, width=5, height=40)

# order_btn= tk.Button(options_frame, text='Order',font=('Bold',15),fg='brown',bg='#c3c3c3',bd=0,command=lambda:indicate(about_indicate,order_page),)
# order_btn.place(x=10,y=250)
# order_indicate=tk.Label(options_frame,text='',bg='brown')
# order_indicate.place(x=3,y=250, width=5, height=40)







options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=700)

main_frame= tk.Frame(root,highlightbackground='black',highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1500, height=700)


root.mainloop()
