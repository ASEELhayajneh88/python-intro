#  tikinter GUI

# import tkinter as tk


# class Application(tk.Frame):

#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Helllllo World\n(click me !!!!!)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="right")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
# from PIL import ImageTk, Image

# from PIL import ImageTk, Image
# from tkinter import *

# #Import the required Libraries
# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter frame
# win= Tk()

# #Set the geometry of Tkinter frame
# win.geometry("750x250")

# def display_text():
#    global entry
#    string= entry.get()
#    print('User Input: ', string)
#    label.configure(text=string)

# #Initialize a Label to display the User Input
# label=Label(win, text="", font=("Courier 22 bold"))
# label.pack()
# img=ImageTk.PhotoImage(Image.open("./tk.png"))

# #Create an Entry widget to accept User Input
# entry= Entry(win, width= 40)
# entry.focus_set()
# entry.pack()

# #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)


# win.mainloop()



# import tkinter as tk
# from tkinter import ttk


# LARGEFONT =("Verdana", 35)

# class tkinterApp(tk.Tk):
	
# 	# __init__ function for class tkinterApp 
# 	def __init__(self, *args, **kwargs): 
		
# 		# __init__ function for class Tk
# 		tk.Tk.__init__(self, *args, **kwargs)
		
# 		# creating a container
# 		container = tk.Frame(self) 
# 		container.pack(side = "top", fill = "both", expand = True) 

# 		container.grid_rowconfigure(0, weight = 1)
# 		container.grid_columnconfigure(0, weight = 1)

# 		# initializing frames to an empty array
# 		self.frames = {} 

# 		# iterating through a tuple consisting
# 		# of the different page layouts
# 		for F in (StartPage, Page1, Page2,page3):

# 			frame = F(container, self)

# 			# initializing frame of that object from
# 			# startpage, page1, page2 respectively with 
# 			# for loop
# 			self.frames[F] = frame 

# 			frame.grid(row = 0, column = 0, sticky ="nsew")

# 		self.show_frame(StartPage)

# 	# to display the current frame passed as
# 	# parameter
# 	def show_frame(self, cont):
# 		frame = self.frames[cont]
# 		frame.tkraise()

# # first window frame startpage

# class StartPage(tk.Frame):
# 	def __init__(self, parent, controller): 
# 		tk.Frame.__init__(self, parent)
		
# 		# label of frame Layout 2
# 		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
# 		# putting the grid in its place by using
# 		# grid
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

# 		button1 = ttk.Button(self, text ="Page 1",
# 		command = lambda : controller.show_frame(Page1))
	
# 		# putting the button in its place by
# 		# using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		## button to show frame 2 with text layout2
# 		button2 = ttk.Button(self, text ="Page 2",
# 		command = lambda : controller.show_frame(Page2))
	
# 		# putting the button in its place by
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# # second window frame page1 
# class Page1(tk.Frame):
	
# 	def __init__(self, parent, controller):
		
# 		tk.Frame.__init__(self, parent)
# 		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button1 = ttk.Button(self, text ="StartPage",
# 							command = lambda : controller.show_frame(StartPage))
	
# 		# putting the button in its place 
# 		# by using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button2 = ttk.Button(self, text ="Page 2",
# 							command = lambda : controller.show_frame(Page2))
	   
# 		# putting the button in its place by 
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
     


# # third window frame page2
# class Page2(tk.Frame): 
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self, parent)
# 		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button1 = ttk.Button(self, text ="Page 1",
# 							command = lambda : controller.show_frame(Page1))
	
# 		# putting the button in its place by 
# 		# using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		# button to show frame 3 with text
# 		# layout3
# 		button2 = ttk.Button(self, text ="Startpage",
# 							command = lambda : controller.show_frame(StartPage))
	
# 		# putting the button in its place by
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
#         button3 = ttk.Button(self, text ="Page 2",command = lambda : controller.show_frame(Page2))
	   
# 		# putting the button in its place by 
# 		# using grid
#         button3.grid(row = 3, column = 1, padx = 10, pady = 10)

# class Page3(tk.Frame): 
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self, parent)
# 		label = ttk.Label(self, text ="Page 3", font = LARGEFONT)
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button1 = ttk.Button(self, text ="Page 1",
# 							command = lambda : controller.show_frame(Page1))
	
# 		# putting the button in its place by 
# 		# using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		# button to show frame 3 with text
# 		# layout3
	

# # Driver Code
# app = tkinterApp()
# app.mainloop()
import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
