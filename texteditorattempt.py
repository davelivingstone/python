'''The idea came from Derek Banas' youtube tutorial for creating a file menu.
I just wrote it again for practice and learning and then I started 
adding stuff to it. I wanted to extend it and create an actual 
simple text editor. I changed quit() to destroy() in the quit_app 
function, since quit() didn't work. I also added the title and 
geometry to root, plus changed Command to Control, for Linux and 
Windows systems. Then, I added a customized Text widget for writing text, 
menu items for saving it as a text file and opening that text file, 
and then bound the keyboard commands for them. I still have a lot to
do, such as saving to a file name of your choosing and opening a distinct
file, but it's a start.'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app(event=None):
	root.destroy()

def show_about(event=None):
	messagebox.showinfo('About', 'I wrote most of this on July 29th, 2019')

def save_text(event=None):
	with open('text.txt', 'w') as f:
		f.write(text_area.get(0.0, END))

def open_file(event=None):
	with open('text.txt', 'r') as f:
		stringified = ''.join(f.readlines())
		text_area.insert(END, stringified)


root = Tk()
root.title('Text Editor')
root.geometry('640x500')

the_menu = Menu(root)

# File menu
file_menu = Menu(the_menu, tearoff=0)
file_menu.add_command(label='Open', accelerator='Ctrl-o', command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl-s', command=save_text)

file_menu.add_separator()

file_menu.add_command(label='Quit', accelerator='Ctrl-q', command=quit_app)
the_menu.add_cascade(label='File', menu=file_menu)

# Font menu
text_font = StringVar()
text_font.set('Times')

def change_font(event=None):
	print('Font picked: ', text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label='Times', variable=text_font, command=change_font)
font_menu.add_radiobutton(label='Courier', variable=text_font, command=change_font)
font_menu.add_radiobutton(label='Arial', variable=text_font, command=change_font)

# View menu
view_menu = Menu(the_menu, tearoff=0)

line_numbers = IntVar()
line_numbers.set(1)

view_menu.add_checkbutton(label='Line numbers', variable=line_numbers)
view_menu.add_cascade(label='Fonts', menu=font_menu)
the_menu.add_cascade(label='View', menu=view_menu)

# Help menu
help_menu = Menu(the_menu, tearoff=0)
help_menu.add_command(label='About', accelerator='Ctrl-m', command=show_about)

the_menu.add_cascade(label='Help', menu=help_menu)

root.bind('<Control-m>', show_about)
root.bind('<Control-q>', quit_app)
root.bind('<Control-s>', save_text)
root.bind('<Control-o>', open_file)

root.config(menu=the_menu)

text_area = Text(root, width=640, height=500, bg='lightgreen', fg='black', wrap='word', font=('Times', 12))
text_area.pack()

root.mainloop()
