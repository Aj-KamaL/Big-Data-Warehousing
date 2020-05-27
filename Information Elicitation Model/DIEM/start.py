import numpy
import csv
import os
import pandas
from tkinter import *
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',user='root',password='rootpass')
sql_select_Queryd = "create database IF NOT EXISTS Decision"
sql_select_Querya = "create database IF NOT EXISTS Act"
sql_select_Queryb = "create database IF NOT EXISTS Obj"
sql_select_Queryc = "create database IF NOT EXISTS Unc"
cursor1 = connection.cursor()
cursor1.execute(sql_select_Queryd)
cursor1.execute(sql_select_Querya)
cursor1.execute(sql_select_Queryb)
cursor1.execute(sql_select_Queryc)

def dec():
	win= Toplevel(root)
	win.title("Add New Decision")
	label1= Label(win, text= "Enter your decision:", bg= "red", fg= "white")
	label1.grid(row= 2, sticky= E)
	entry1= Entry(win)
	entry1.grid(row= 2, column= 1)
	writethis= ["Decision", "1"]
	def dec_submit():
		writethis[1]= entry1.get()
		if(writethis[1]== ""):
			win.destroy()
			return "Come on Bro!"
		print (writethis)
		sql_select_Query1 = "use Decision"
		cursor1 = connection.cursor()
		cursor1.execute(sql_select_Query1)
		sql_select_Query2 = "create table "+str(writethis[1])+"(decid varchar(100),dectyp varchar(100))"
		print(sql_select_Query2)
		cursor2 = connection.cursor()
		cursor2.execute(sql_select_Query2)
		with open('./make.csv', 'a') as f:
			writer= csv.writer(f)
			writer.writerow(writethis)
		win.destroy()
	button1= Button(win, text= "Submit", command= dec_submit)
	button1.grid(row= 5, columnspan= 2)


def unc():
    win= Toplevel(root)
    win.title("Add New Uncertainty")
    label1= Label(win, text= "Name of Uncertainty Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Uncertainty Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)
    entry1= Entry(win)
    entry2= Entry(win)
    entry1.grid(row= 2, column= 1)
    entry2.grid(row= 3, column= 1)
    writethis= ["Uncertainty", "1", "2"]
    
    def unc_submit():
        writethis[1]= entry1.get()
        writethis[2]= entry2.get()
        if(writethis[1]== "" or writethis[2]== ""):
            win.destroy()
            return "Come on Bro!"
        print (writethis)
        tempb=""
        sql_select_Query1 = "use Unc"
        cursor1 = connection.cursor()
        cursor1.execute(sql_select_Query1)

        sql_select_Query2 = "create table "+str(writethis[1])+"("
        for j in writethis[2].split(','):
        	tempb=tempb+str(j)+" varchar(100),"
        tempb=tempb[:-1]
        sql_select_Query2 = sql_select_Query2+tempb+")"
        print(sql_select_Query2)
        cursor2 = connection.cursor()
        cursor2.execute(sql_select_Query2)
        with open('./make.csv', 'a') as f:
            writer= csv.writer(f)
            writer.writerow(writethis)
        win.destroy()
    button1= Button(win, text= "Submit", command= unc_submit)
#     button1.bind("<Button-1>", unc_submit)
    button1.grid(row= 5, columnspan= 2)





def act():
    win= Toplevel(root)
    win.title("Add New Action")
    label1= Label(win, text= "Name of Action Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Action Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)
    entry1= Entry(win)
    entry2= Entry(win)
    entry1.grid(row= 2, column= 1)
    entry2.grid(row= 3, column= 1)
    writethis= ["Action", "1", "2"]
    def act_submit():
        writethis[1]= entry1.get()
        writethis[2]= entry2.get()
        if(writethis[1]== "" or writethis[2]== ""):
            win.destroy()
            return "Come on Bro!"
        print (writethis)
        tempb=""
        sql_select_Query1 = "use Act"
        cursor1 = connection.cursor()
        cursor1.execute(sql_select_Query1)

        sql_select_Query2 = "create table "+str(writethis[1])+"("
        for j in writethis[2].split(','):
        	tempb+=j+" varchar(100),"
        tempb=tempb[:-1]
        sql_select_Query2 = sql_select_Query2+tempb+")"
        print(sql_select_Query2)
        cursor2 = connection.cursor()
        cursor2.execute(sql_select_Query2)
        with open('./make.csv', 'a') as f:
            writer= csv.writer(f)
            writer.writerow(writethis)
        win.destroy()    
    button1= Button(win, text= "Submit", command= act_submit)
    button1.grid(row= 5, columnspan= 2)




def obj():
    win= Toplevel(root)
    win.title("Add New Objective")
    label1= Label(win, text= "Name of Objective Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Objective Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)
    entry1= Entry(win)
    entry2= Entry(win)
    entry1.grid(row= 2, column= 1)
    entry2.grid(row= 3, column= 1)
    writethis= ["Objective", "1", "2"]
    def obj_submit():
        writethis[1]= entry1.get()
        writethis[2]= entry2.get()
        if(writethis[1]== "" or writethis[2]== ""):
            win.destroy()
            return "Come on Bro!"
        print (writethis)
        tempb=""
        sql_select_Query1 = "use Obj"
        cursor1 = connection.cursor()
        cursor1.execute(sql_select_Query1)

        sql_select_Query2 = "create table "+str(writethis[1])+"("
        for j in writethis[2].split(','):
        	tempb+=j+" varchar(100),"
        tempb=tempb[:-1]
        sql_select_Query2 = sql_select_Query2+tempb+")"
        print(sql_select_Query2)
        cursor2 = connection.cursor()
        cursor2.execute(sql_select_Query2)
        with open('./make.csv', 'a') as f:
            writer= csv.writer(f)
            writer.writerow(writethis)
        win.destroy()
    button1= Button(win, text= "Submit", command= obj_submit)
    button1.grid(row= 5, columnspan= 2)


def sdec():
    win= Toplevel(root)
    win.title("Show All Decisions")
    label1= Label(win, text= "Name of Decision Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Decision Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)



    sql_select_Query1 = "use Decision"
    cursor1 = connection.cursor()
    cursor1.execute(sql_select_Query1)
    
    sql_select_Query2 = "show tables"
    cursor2 = connection.cursor()
    cursor2.execute(sql_select_Query2)
    records2 = cursor2.fetchall()
    print(records2)

    tempa=""
    tempb=""
    for i in records2:
    	print(i[0])
    	tempa+=str(i[0])+'\n'
    	sql_select_Query3 = "DESCRIBE " + str(i[0])
    	print(sql_select_Query3)
    	cursor3 = connection.cursor()
    	cursor3.execute(sql_select_Query3)
    	records3 = cursor3.fetchall()
    	print(records3)
    	for j in records3:
    		tempb+=str(j[0])+" ,"
    	tempb=tempb[:-1]
    	tempb +='\n'
    print(tempa)
    print(tempb)
    label3= Label(win, text= tempa, fg= "white",bg= "green")
    label4= Label(win, text= tempb, fg= "white",bg= "green")
    label3.grid(row= 2, column= 1)
    label4.grid(row= 3, column= 1)
    def dec_close():
        win.destroy()
    button1= Button(win, text= "Close", command= dec_close)
    button1.grid(row= 5, columnspan= 2)


def sobj():
    win= Toplevel(root)
    win.title("Show All Objectives")
    label1= Label(win, text= "Name of Objective Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Objective Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)



    sql_select_Query1 = "use Obj"
    cursor1 = connection.cursor()
    cursor1.execute(sql_select_Query1)
    
    sql_select_Query2 = "show tables"
    cursor2 = connection.cursor()
    cursor2.execute(sql_select_Query2)
    records2 = cursor2.fetchall()
    print(records2)

    tempa=""
    tempb=""
    for i in records2:
    	print(i[0])
    	tempa+=str(i[0])+'\n'
    	sql_select_Query3 = "DESCRIBE " + str(i[0])
    	print(sql_select_Query3)
    	cursor3 = connection.cursor()
    	cursor3.execute(sql_select_Query3)
    	records3 = cursor3.fetchall()
    	print(records3)
    	for j in records3:
    		tempb+=str(j[0])+" ,"
    	tempb=tempb[:-1]
    	tempb +='\n'
    print(tempa)
    print(tempb)
    label3= Label(win, text= tempa, fg= "white",bg= "green")
    label4= Label(win, text= tempb, fg= "white",bg= "green")
    label3.grid(row= 2, column= 1)
    label4.grid(row= 3, column= 1)
    def obj_close():
        win.destroy()
    button1= Button(win, text= "Close", command= obj_close)
    button1.grid(row= 5, columnspan= 2)

def sunc():
    win= Toplevel(root)
    win.title("Show Uncertainities")
    label1= Label(win, text= "Name of Uncertainty Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Uncertainty Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)



    sql_select_Query1 = "use Unc"
    cursor1 = connection.cursor()
    cursor1.execute(sql_select_Query1)
    
    sql_select_Query2 = "show tables"
    cursor2 = connection.cursor()
    cursor2.execute(sql_select_Query2)
    records2 = cursor2.fetchall()
    print(records2)

    tempa=""
    tempb=""
    for i in records2:
    	print(i[0])
    	tempa+=str(i[0])+'\n'
    	sql_select_Query3 = "DESCRIBE " + str(i[0])
    	print(sql_select_Query3)
    	cursor3 = connection.cursor()
    	cursor3.execute(sql_select_Query3)
    	records3 = cursor3.fetchall()
    	print(records3)
    	for j in records3:
    		tempb+=str(j[0])+" ,"
    	tempb=tempb[:-1]
    	tempb +='\n'
    print(tempa)
    print(tempb)
    label3= Label(win, text= tempa, fg= "white",bg= "green")
    label4= Label(win, text= tempb, fg= "white",bg= "green")
    label3.grid(row= 2, column= 1)
    label4.grid(row= 3, column= 1)
    def unc_close():
        win.destroy()
    button1= Button(win, text= "Close", command= unc_close)
    button1.grid(row= 5, columnspan= 2)

def sact():
    win= Toplevel(root)
    win.title("Show Actions")
    label1= Label(win, text= "Name of Action Object", bg= "purple", fg= "white")
    label1.grid(row= 2, sticky= E)
    label2= Label(win, text= "Records in Action Object", bg= "purple", fg= "white")
    label2.grid(row= 3, sticky= E)



    sql_select_Query1 = "use Act"
    cursor1 = connection.cursor()
    cursor1.execute(sql_select_Query1)
    
    sql_select_Query2 = "show tables"
    cursor2 = connection.cursor()
    cursor2.execute(sql_select_Query2)
    records2 = cursor2.fetchall()
    print(records2)

    tempa=""
    tempb=""
    for i in records2:
    	print(i[0])
    	tempa+=str(i[0])+'\n'
    	sql_select_Query3 = "DESCRIBE " + str(i[0])
    	print(sql_select_Query3)
    	cursor3 = connection.cursor()
    	cursor3.execute(sql_select_Query3)
    	records3 = cursor3.fetchall()
    	print(records3)
    	for j in records3:
    		tempb+=str(j[0])+" ,"
    	tempb=tempb[:-1]
    	tempb +='\n'
    print(tempa)
    print(tempb)
    label3= Label(win, text= tempa, fg= "white",bg= "green")
    label4= Label(win, text= tempb, fg= "white",bg= "green")
    label3.grid(row= 2, column= 1)
    label4.grid(row= 3, column= 1)
    def act_close():
        win.destroy()
    button1= Button(win, text= "Close", command= act_close)
    button1.grid(row= 5, columnspan= 2)



root= Tk()
root.title("DW MINOR PROJECT")
root.configure(background='black')

label= Label(root, text= "Decision: Choose a Hotel for Leisure", fg= "black", bg= "yellow")
label.grid(row= 0, columnspan= 2)

adddec= Button(root, text= 'Add a Decision', fg= 'green', command= dec)
adddec.grid(row= 2, column= 1)

addunc= Button(root, text= 'Add an Uncertainty', fg= 'green', command= unc)
addunc.grid(row= 3, column= 1)

addact= Button(root, text= 'Add an Action', fg= 'green', command= act)
addact.grid(row= 4, column= 1)

addobj= Button(root, text= 'Add an Objective', fg= 'green', command= obj)
addobj.grid(row= 5, column= 1)

showdec= Button(root, text= 'Show Decision', fg= 'green', command= sdec)
showdec.grid(row= 2, column= 2)

showunc= Button(root, text= 'Show Uncertainities', fg= 'green', command= sunc)
showunc.grid(row= 3, column= 2)

showact= Button(root, text= 'Show Actions', fg= 'green', command= sact)
showact.grid(row= 4, column= 2)

showobj= Button(root, text= 'Show Objectives', fg= 'green', command= sobj)
showobj.grid(row= 5, column= 2)

root.mainloop()





