from tkinter import *

def make_right_menu(root):
    global rightmenu
    rightmenu = Menu(root,tearoff=0)
    rightmenu.add_command(label='Cut',accelerator='Ctrl+X')
    rightmenu.add_command(label='Copy',accelerator='Ctrl+C')
    rightmenu.add_command(label='Paste',accelerator='Ctrl+V')
    rightmenu.add_separator()
    rightmenu.add_command(label='Select All',accelerator='Ctrl+A')

def select_all(event=None):
    t1.tag_add(SEL,'1.0',END)
    t1.mark_set(INSERT,'1.0')
    t1.see(INSERT)
    return 'break'
def show_rightmenu(event):
    widget = event.widget
    rightmenu.entryconfigure('Cut',command=lambda:widget.event_generate('<<Cut>>'))
    rightmenu.entryconfigure('Copy',command=lambda:widget.event_generate('<<Copy>>'))
    rightmenu.entryconfigure('Paste',command=lambda:widget.event_generate('<<Paste>>'))
    if type(widget) == Entry:
         rightmenu.entryconfigure('Select All',command=lambda:widget.select_range(0,END))
    elif type(widget) == Text:
        rightmenu.entryconfigure('Select All',command=select_all)
    rightmenu.tk.call('tk_popup',rightmenu,event.x_root,event.y_root)

    
root = Tk()
make_right_menu(root)
root.bind_class('Text',"<Button-3><ButtonRelease-3>",show_rightmenu)
root.bind_class('Entry',"<Button-3><ButtonRelease-3>",show_rightmenu)

t1 = Text(root)
t1.pack()
e1 = Entry(root)
e1.pack()
root.mainloop()
