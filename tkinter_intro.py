#Creating a GUI app with Python using: https://realpython.com/python-gui-tkinter/

import tkinter as tk

#Create a window
window = tk.Tk()

#Create a label widget
greeting = tk.Label(text="Hello, Tkinter")
"""
Widget Class	Description
Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Entry	        A text entry widget that allows only a single line of text
Text	        A text entry widget that allows multiline text entry
Frame	        A rectangular region used to group related widgets or provide padding between widgets
"""

#Displays the label widget in the window by using .pack()
greeting.pack()

#Command to continuously run program (includes checking for button presses)
window.mainloop()
