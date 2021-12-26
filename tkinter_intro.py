# Creating a GUI app with Python using: https://realpython.com/python-gui-tkinter/

import tkinter as tk

# Create a window
window = tk.Tk()

"""
Widget Class	Description
Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Entry	        A text entry widget that allows only a single line of text
Text	        A text entry widget that allows multiline text entry
Frame	        A rectangular region used to group related widgets or provide padding between widgets
"""

# Create a label widget - can only view from, not edit to
greeting = tk.Label(
    text="Name",
    foreground="white",  # fg is shorthand for foreground
    background="blue",  # bg is shorthand for background
    width=10,  # weight and height are measured in text units = height and width of a single '0'
    height=10
)

# Creating a button is the same thing as creating a label, only you also code what happens when you click
# foreground and background colors are not displaying as they should...
"""button = tk.Button(
    text="Click me!",
    foreground="yellow",
    background="blue",
    width=25,
    height=5
)"""

# Entry widgets - retrieve with .get(), delete with .delete(), and insert with .insert()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
# can use .get(), .delete(), .insert()

# Text widget
textBox = tk.Text()
# can use .get(), but requires:
# 1) line number of character (starts at line 1)
# and
# 2) position of character on line (starts at 0)
# so "1.0" gets line 1, character 0
# .get("1.0", "1.5") gets line 1, characters 0-4
# can also get all info in textbox using .get("1.0", tk.END) --> includes \n characters
# Writing new lines to the text box requires the new line character (\n) inside the string to be written

# Frame widgets hold other widgets
frame_a = tk.Frame()
# Frames can have different borders (tk.FLAT, .SUNKEN, .RAISED, .GROOVE, .RIDGE)
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

# Create an entry widget and add some text
entry_b = tk.Entry(width=40)
entry_b.pack()
entry_b.insert(0, "What is your name? ")

# Displays widgets in the window/frame by using .pack()
frame_a.pack()
greeting.pack()
# button.pack()
entry.pack()
textBox.pack()


# Command to continuously run program (includes checking for button presses)
window.mainloop()
