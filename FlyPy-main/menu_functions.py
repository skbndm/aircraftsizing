# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:55:51 2021

@author: Matko
"""
import tkinter as tk

def option_load():
    filename1 = tk.filedialog.askopenfilename(
        title='select a file title',
        filetypes=(
            ("Text files","*.txt"),
            ("All files","*.*")))
    with open(filename1,'r') as f:
        load_list = []
        for lin in f:
            lin2 = lin.strip("\n")
            load_list.append(lin2)
        f.close()
    if load_list[0] == "savefile for FlyPy":
        return load_list,filename1 # this is list!
    else:
        load_list = 'Save file not a valid type or corrupt.'
        return load_list # this is string! Error must react on string!

def option_save(savelist,filename1):
    thefile = open(filename1,"w+")
    for item in savelist:
        thefile.write( str(item) + "\n" )
    thefile.close()
    return

def option_saveas(savelist):
    global C
    filename1 = tk.filedialog.asksaveasfilename(
        # initialdir="~",
        title="Save file",
        defaultextension=".txt",
        filetypes=(
            ("Text files","*.txt"),
            ("All files","*.*")))
    thefile = open(filename1,"w+")
    for item in savelist:
        thefile.write( str(item) + "\n" )
    thefile.close()
    return filename1

#-----------------------------------#

def option_about():
    text1 = "Hi, thanks for using this aircraft sizing tool (I haven't come up with a name yet). It's a hobby project and still heavily in development.\n\nIf you have constructive comments and/or advices, please leave a comment on my github page.\n\nMat"
    tk.messagebox.showinfo(title="About", message=text1)
    return


#ovo ide nakon entry level width
def donothing():
    return