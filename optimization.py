import pulp
import tkinter as tk
from tkinter import ttk
from tkinter import Frame
import sys 
import os

root= tk.Tk()
root.title('Simplex Optimization')

#simplex optimization function

def simplex():
    simentry1=int(entry1.get())
    simentry2=int(entry2.get())
    simentry3=int(entry3.get())

    simbentry1=int(bentry1.get())
    simbentry2=int(bentry2.get())
    simbentry3=int(bentry3.get())
    simbentry4=bentry4.get()
    simbentry5=int(bentry5.get())

    simcentry1=int(centry1.get())
    simcentry2=int(centry2.get())
    simcentry3=int(centry3.get())
    simcentry4=centry4.get()
    simcentry5=int(centry5.get())

    simdentry1=int(dentry1.get())
    simdentry2=int(dentry2.get())
    simdentry3=int(dentry3.get())
    simdentry4=dentry4.get()
    simdentry5=int(dentry5.get())

    

    leore = "<="
    gore = ">="
    equal = "="
    firstsym = bentry4.get()
    secondsym = centry4.get()
    thirdsym = dentry4.get()
    # sys.setrecursionlimit(5000)

    #define variables

    x1=pulp.LpVariable('x1',lowBound=0)
    x2=pulp.LpVariable('x2',lowBound=0)
    x3=pulp.LpVariable('x3',lowBound=0)

    #define objective function

    max_profit=pulp.LpProblem('maximize',pulp.LpMaximize)
    max_profit+=simentry1*x1+simentry2*x2+simentry3*x3

    #constraints
    
    if firstsym==equal:
        max_profit+= simbentry1*x1+simbentry2*x2+simbentry3*x3==simbentry5
    elif firstsym==gore:
        max_profit+= simbentry1*x1+simbentry2*x2+simbentry3*x3>=simbentry5
    elif firstsym==leore:
        max_profit+= simbentry1*x1+simbentry2*x2+simbentry3*x3<=simbentry5
    
    if secondsym==equal:
        max_profit+= simcentry1*x1+simcentry2*x2+simcentry3*x3==simcentry5
    elif secondsym==gore:
        max_profit+= simcentry1*x1+simcentry2*x2+simcentry3*x3>=simcentry5
    elif secondsym==leore:
        max_profit+= simcentry1*x1+simcentry2*x2+simcentry3*x3<=simcentry5

    if thirdsym==equal:
        max_profit+= simdentry1*x1+simdentry2*x2+simdentry3*x3==simdentry5
    elif thirdsym==gore:
        max_profit+= simdentry1*x1+simdentry2*x2+simdentry3*x3>=simdentry5
    elif thirdsym==leore:
        max_profit+= simdentry1*x1+simdentry2*x2+simdentry3*x3<=simdentry5

        
    #solve

    max_profit.solve()
    x1var='x1= '+str(x1.varValue)
    x2var='x2= '+str(x2.varValue)
    x3var='x3= '+str(x3.varValue)
    maxtext='Maximim Profit is'
    maxprofit=pulp.value(max_profit.objective)

    Olabel1 = tk.Label(root, text=x1var,fg='black',bg='white')
    Olabel1.config(font=('helvetica', 17))
    canvas1.create_window(225+190, 305+225, window=Olabel1)

    Olabel2 = tk.Label(root, text=x2var,fg='black',bg='white')
    Olabel2.config(font=('helvetica', 17))
    canvas1.create_window(225+190, 305+250, window=Olabel2)
    
    Olabel3 = tk.Label(root, text=x3var,fg='black',bg='white')
    Olabel3.config(font=('helvetica', 17))
    canvas1.create_window(225+190, 305+300, window=Olabel3)

    Olabel4 = tk.Label(root, text=maxtext, fg='black',bg='white')
    Olabel4.config(font=('helvetica', 17))
    canvas1.create_window(225+190, 305+350, window=Olabel4)

    Olabel5 = tk.Label(root, text=maxprofit,fg='black',bg='white')
    Olabel5.config(font=('helvetica', 17))
    canvas1.create_window(225+190, 305+400, window=Olabel5)

    
    


canvas1 = tk.Canvas(root, width = 800, height = 900,  relief = 'raised', bg='#D7ECD9')
canvas1.pack()
#Heading
label1 = tk.Label(root, text='Simplex Optimization',fg='white',bg='#218B82')
label1.config(font=('helvetica', 20))
canvas1.create_window(400, 30, window=label1)
#Credit
label2 = tk.Label(root, text='Submitted By: Shephalika Dhakal ',fg='#218B82',bg='#98D4BB')
label2.config(font=('helvetica', 14))
canvas1.create_window(200, 70, window=label2)

label3 = tk.Label(root, text='Submitted To: Durga Prasad Dhakal',fg='#218B82',bg='#98D4BB')
label3.config(font=('helvetica', 14))
canvas1.create_window(550, 70, window=label3)


#creating entry lable and entry for Max(Z)
label4 = tk.Label(root, text='Max(Z) = ',fg='black')
label4.config(font=('helvetica', 15))
canvas1.create_window(120, 160, window=label4)
#1
entry1 = tk.Entry (root) 
canvas1.create_window(180, 160, window=entry1,height=40,width=40)
label5 = tk.Label(root, text='X1 +',fg='black')
label5.config(font=('helvetica', 15))
canvas1.create_window(225, 165, window=label5)
#2
entry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160, window=entry2,height=40,width=40)
label6 = tk.Label(root, text='X2 +',fg='black')
label6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165, window=label6)
#3
entry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160, window=entry3,height=40,width=40)
label7 = tk.Label(root, text='X3',fg='black')
label7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165, window=label7)

#creating entry lable and entry for 1st equation
#1
bentry1 = tk.Entry (root) 
canvas1.create_window(180, 160+50, window=bentry1,height=40,width=40)
blabel5 = tk.Label(root, text='X1 +',fg='black')
blabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+50, window=blabel5)
#2
bentry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+50, window=bentry2,height=40,width=40)
blabel6 = tk.Label(root, text='X2 +',fg='black')
blabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+50, window=blabel6)
#3
bentry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+50, window=bentry3,height=40,width=40)
blabel7 = tk.Label(root, text='X3',fg='black')
blabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+50, window=blabel7)
#symbol
bentry4 = ttk.Combobox(root,values=['<=','>=','='])
bentry4.current(0)
canvas1.create_window(180+90+170, 160+50, window=bentry4,height=40,width=40)
#constant
bentry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50, window=bentry5,height=40,width=40)


#creating entry lable and entry for 2nd equation
#1
centry1 = tk.Entry (root) 
canvas1.create_window(180, 160+50+50, window=centry1,height=40,width=40)
clabel5 = tk.Label(root, text='X1 +',fg='black')
clabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+50+50, window=clabel5)
#2
centry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+50+50, window=centry2,height=40,width=40)
clabel6 = tk.Label(root, text='X2 +',fg='black')
clabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+50+50, window=clabel6)
#3
centry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+50+50, window=centry3,height=40,width=40)
clabel7 = tk.Label(root, text='X3',fg='black')
clabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+50+50, window=clabel7)
#symbol
centry4 = ttk.Combobox(root,values=['<=','>=','='])
centry4.current(0)
canvas1.create_window(180+90+170, 160+50+50, window=centry4,height=40,width=40)
#constant
centry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50+50, window=centry5,height=40,width=40)

#creating entry lable and entry for 3rd equation
#1
dentry1 = tk.Entry (root) 
canvas1.create_window(180, 160+150, window=dentry1,height=40,width=40)
dlabel5 = tk.Label(root, text='X1 +',fg='black')
dlabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+150, window=dlabel5)
#2
dentry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+150, window=dentry2,height=40,width=40)
dlabel6 = tk.Label(root, text='X2 +',fg='black')
dlabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+150, window=dlabel6)
#3
dentry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+150, window=dentry3,height=40,width=40)
dlabel7 = tk.Label(root, text='X3',fg='black')
dlabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+150, window=dlabel7)
#symbol
geore = '>='
leore = '<='
equal = '='
dentry4 = ttk.Combobox(root,values=[equal,leore,geore])
dentry4.current(1)
canvas1.create_window(180+90+170, 160+150, window=dentry4,height=40,width=40)
#constant
dentry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+150, window=dentry5,height=40,width=40)

#last portion
dlabel7 = tk.Label(root, text='X1,X2,X3 >= 0',fg='black')
dlabel7.config(font=('helvetica', 15))
canvas1.create_window(225, 165+200, window=dlabel7)
canvas1.create_rectangle(5, 450, 800, 800,fill='#D7ECD9')
#def restart_program():
#    """Restarts the current program.
#    Note: this function does not return. Any cleanup action (like
#    saving data) must be done before calling this function."""
#    python = sys.executable
#    os.execl(python, python, * sys.argv)



#Optimize button
button1 = tk.Button(text='Optimize',  bg='#98D4BB', fg='#218B82', font=('helvetica', 15, 'bold'),relief = 'solid',command=simplex)
canvas1.create_window(250, 365+50, window=button1,height=50,width=100)

#Reset button
#button2 = tk.Button(text='Reset',  bg='red', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid',command=restart_program)
#canvas1.create_window(480, 365+50, window=button2,height=50,width=100)



root.mainloop()
