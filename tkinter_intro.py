#Creating a GUI app with Python using: https://realpython.com/python-gui-tkinter/

import tkinter as tk

#Create a window
window = tk.Tk()

"""
Widget Class	Description
Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Entry	        A text entry widget that allows only a single line of text
Text	        A text entry widget that allows multiline text entry
Frame	        A rectangular region used to group related widgets or provide padding between widgets
"""

#Create a label widget - can only view from, not edit to
greeting = tk.Label(
    text="Name",
    foreground="white", #fg is shorthand for foreground
    background="blue", #bg is shorthand for background
    width=10, #weight and height are measured in text units = height and width of a single '0'
    height=10
)

#Creating a button is the same thing as creating a label, only you also code what happens when you click
#foreground and background colors are not displaying as they should...
'''
button = tk.Button(
    text="Click me!",
    foreground="yellow",
    background="blue",
    width=25,
    height=5
)'''

#Entry widgets - retrieve with .get(), delete with .delete(), and insert with .insert()
entry = tk.Entry()

#Displays the label widget in the window by using .pack()
greeting.pack()
#button.pack()
entry.pack()

#Command to continuously run program (includes checking for button presses)
window.mainloop()
