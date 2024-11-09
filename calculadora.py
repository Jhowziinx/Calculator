from tkinter import *
from tkinter import ttk

#colors

color1 = "#1c1a1a"  #background
color2 = "#ffffff"  #white
color3 = "#38576b"  #blue
color4 = "#ECEFF1"  #cinzenta
color5 = "#15b352"  #green

window = Tk()
window.title("Calculadora")
window.geometry("238x310")
window.config(bg = color1)

#frames

screen_frame = Frame(window, width = 235, height = 50, bg = color1)
screen_frame.grid(row = 0, column = 0)

screen_body = Frame(window, width = 235, height = 268, bg= color1)
screen_body.grid(row = 1, column = 0)

#all values

values_all = ""

# functions

def values_enter(event):
    global values_all
    values_all = values_all + str(event)
    text_value.set(values_all)

def calculate():
    global values_all 
    result = eval(values_all)
    text_value.set(str(result))
    values_all = (str(result))

def clean_screen():
    global values_all
    values_all = ''
    text_value.set('')

#making_label
    
text_value = StringVar()
app_label = Label(screen_frame, textvariable = text_value, width = 16, height = 2, padx = 7, relief= FLAT, anchor = 'e', justify = RIGHT, font = ("Ivy 18"), bg = color1, fg = color2)
app_label.place(x = 0, y = 0)

#buttons

b_1 = Button(screen_body, command = clean_screen, text = "C", width = 11, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE, )
b_1.place(x = 0, y = 0)
b_2 = Button(screen_body, command = lambda: values_enter("%"), text = "%", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_2.place(x = 118, y = 0)
b_3 = Button(screen_body, command = lambda: values_enter("/"),text = "/", width = 5, height = 2, bg = color5, fg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_3.place(x = 177, y = 0)

b_4 = Button(screen_body, command = lambda: values_enter("7"),text = "7", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_4.place(x = 0, y = 52)
b_5 = Button(screen_body, command = lambda: values_enter("8"),text = "8", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_5.place(x = 59, y = 52)
b_6 = Button(screen_body, command = lambda: values_enter("9"),text = "9", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_6.place(x = 118, y = 52)
b_7 = Button(screen_body, command = lambda: values_enter("*"),text = "X", width = 5, height = 2, bg = color5, fg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_7.place(x = 177, y = 52)

b_8 = Button(screen_body, command = lambda: values_enter("4"),text = "4", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_8.place(x = 0, y = 104)
b_9 = Button(screen_body, command = lambda: values_enter("5"),text = "5", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_9.place(x = 59, y = 104)
b_10 = Button(screen_body,command = lambda: values_enter("6"),text = "6", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_10.place(x = 118, y = 104)
b_11 = Button(screen_body,command = lambda: values_enter("-"),text = "-", width = 5, height = 2, bg = color5, fg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_11.place(x = 177, y = 104)

b_12 = Button(screen_body,command = lambda: values_enter("1"),text = "1", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_12.place(x = 0, y = 156)
b_13 = Button(screen_body,command = lambda: values_enter("2"),text = "2", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_13.place(x = 59, y = 156)
b_14 = Button(screen_body,command = lambda: values_enter("3"),text = "3", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_14.place(x = 118, y = 156)
b_15 = Button(screen_body,command = lambda: values_enter("+"),text = "+", width = 5, height = 2, bg = color5, fg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_15.place(x = 177, y = 156)

b_16 = Button(screen_body,command = lambda: values_enter("0"),text = "0", width = 11, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_16.place(x = 0, y = 208)
b_17 = Button(screen_body,command = lambda: values_enter("."),text = ".", width = 5, height = 2, bg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_17.place(x = 118, y = 208)
b_18 = Button(screen_body, command = calculate,text = "=", width = 5, height = 2, bg = color5, fg = color2, font = ('Ivy 13 bold'), relief = RAISED, overrelief=RIDGE)
b_18.place(x = 177, y = 208)


window.mainloop()