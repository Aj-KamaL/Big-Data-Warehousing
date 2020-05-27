import numpy
import csv
import os
import pandas
from tkinter import *
import mysql.connector
from mysql.connector import Error
import datetime



connection = mysql.connector.connect(host='localhost',user='root',password='rootpass')
cursor1 = connection.cursor()
now = datetime.datetime.now()
datee=str(now.strftime("%d-%m-%Y"))
userid=str(now.strftime("%S%M%d"))
# cursor1.execute("create database dw")
cursor1.execute("use DWProj")
# cursor1.execute("source /Users/rajat_mac/Downloads/DW_Minor_Project/createtables.sql;")

def hot_br_val():
	win= Toplevel(root)
	win.title("User Input: Hotel Brand-Value Preferences")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)    

	label3= Label(win, text= "Date: ", bg= "red", fg= "white")
	label3.grid(row= 3, column=1,sticky=W+E)
	label4= Label(win, text= datee, bg= "green", fg= "white")
	label4.grid(row= 3, column=2, sticky=W+E)

	label5= Label(win, text= "Star Rating: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Quality of Service: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Reviews Rating: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	entry3=Entry(win)
	entry3.grid(row= 6, column=2,sticky=W+E)
	def submit():
		try:
			starrating= int(entry1.get())
			qos= int(entry2.get())
			reviewsrating= float(entry3.get())
			cursor1.execute("INSERT INTO HotelBrandValue(userid, datee, starrating, qualityofservice, reviewsrating) VALUES (" + userid + "," + "NOW()," + str(starrating) + "," + str(qos) + "," + str(reviewsrating) + ");")
			connection.commit()
			# print("INSERT INTO HotelBrandValue(userid, datee, starrating, qualityofservice, reviewsrating) VALUES (" + userid + "," + "NOW()," + str(starrating) + "," + str(qos) + "," + str(reviewsrating) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 8, column= 1, columnspan= 2)



def acc():
	win= Toplevel(root)
	win.title("User Input: Expected Accessibility")

	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)

	label3= Label(win, text= "Date: ", bg= "red", fg= "white")
	label3.grid(row= 3, column=1,sticky=W+E)
	label4= Label(win, text= datee, bg= "green", fg= "white")
	label4.grid(row= 3, column=2, sticky=W+E)	   

	label5= Label(win, text= "Location(Latitude Longitude): ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Weather Conditions(MinTemp MaxTemp): ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Occupancy: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	variable3 = StringVar()
	variable3.set("Vacant")#check this
	entry3= OptionMenu(win, variable3, "Vacant", "Full")
	entry3.grid(row= 6, column=2,sticky=W+E)
	def submit():
		try:
			occupied= FALSE
			location= str(entry1.get())
			weather= str(entry2.get())
			if(variable3.get()== "Vacant"):
				occupied= TRUE#means occupancy available
			cursor1.execute("INSERT INTO Accessibility(userid, datee, locationn, occupancy, weatherconditions) VALUES (" + userid + "," + "NOW(),\"" + location + "\"," + str(int(occupied)) + ",\"" + weather + "\");")
			connection.commit()
			# print("INSERT INTO Accessibility(userid, datee, locationn, occupancy, weatherconditions) VALUES (" + userid + "," + "NOW(),\"" + location + "\"," + str(int(occupied)) + ",\"" + weather + "\");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 8, column= 1, columnspan= 2)



def pref():
	win= Toplevel(root)
	win.title("User Input: Expected Preferences")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)

	label3= Label(win, text= "Date: ", bg= "red", fg= "white")
	label3.grid(row= 3, column=1,sticky=W+E)
	label4= Label(win, text= datee, bg= "green", fg= "white")
	label4.grid(row= 3, column=2, sticky=W+E)	   

	label5= Label(win, text= "Reservation Cost: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Transport Cost: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label8= Label(win, text= "Dining Options: ", bg= "red", fg= "white")
	label8.grid(row= 6, column=1,sticky=W+E)
	variable4= StringVar()
	variable4.set("Breakfast Lunch Dinner")
	entry4= Listbox(win, listvariable= variable4, selectmode= MULTIPLE, width= 20, height= 10)
	entry4.grid(row= 6, column=2,sticky=W+E)

	label9= Label(win, text= "Leisure Activities: ", bg= "red", fg= "white")
	label9.grid(row= 7, column=1,sticky=W+E)  
	entry5=Entry(win)
	entry5.grid(row= 7, column=2,sticky=W+E)

	label10= Label(win, text= "Period of Stay(days): ", bg= "red", fg= "white")
	label10.grid(row= 8, column=1,sticky=W+E)  
	entry6=Entry(win)
	entry6.grid(row= 8, column=2,sticky=W+E)

	label11= Label(win, text= "Mode of Payment: ", bg= "red", fg= "white")
	label11.grid(row= 9, column=1,sticky=W+E)  
	entry7=Entry(win)
	entry7.grid(row= 9, column=2,sticky=W+E)

	label12= Label(win, text= "Discount(%): ", bg= "red", fg= "white")
	label12.grid(row= 10, column=1,sticky=W+E)  
	entry8=Entry(win)
	entry8.grid(row= 10, column=2,sticky=W+E)
	def submit():
		try:
			diningselected= [entry4.get(idx) for idx in entry4.curselection()]
			dining= 0
			if("Breakfast" in diningselected):
				dining+= 1
			if("Lunch" in diningselected):
				dining+= 2
			if("Dinner" in diningselected):
				dining+= 4
			discount= float(entry8.get())
			stay= int(entry6.get())
			payment= str(entry7.get())
			transport= float(entry2.get())
			reserve= float(entry1.get())
			leisure= str(entry5.get())
			cursor1.execute("INSERT INTO Preferences(userid, datee, diningoptions, periodofstay, discount, transportcost, leisureactivities, modeofpayment, reservationcost) VALUES (" + userid + "," + "NOW()," + str(dining) + "," + str(stay) + "," + str(discount) + "," + str(transport) + ",\"" + leisure + "\",\"" + payment + "\"," + str(reserve) + ");")
			connection.commit()
			# print("INSERT INTO Preferences(userid, datee, diningoptions, periodofstay, discount, transportcost, leisureactivities, modeofpayment, reservationcost) VALUES (" + userid + "," + "NOW()," + str(dining) + "," + str(stay) + "," + str(discount) + "," + str(transport) + ",\"" + leisure + "\",\"" + payment + "\"," + str(reserve) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 12, column= 1, columnspan= 2)



def hot_fac():
	win= Toplevel(root)
	win.title("User Input: Expected Hotel Facilities")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)
	   

	label5= Label(win, text= "Swimming Pool: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Breakfast Included: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Parking: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	entry3=Entry(win)
	entry3.grid(row= 6, column=2,sticky=W+E)

	label8= Label(win, text= "Order-In: ", bg= "red", fg= "white")
	label8.grid(row= 7, column=1,sticky=W+E)  
	entry4=Entry(win)
	entry4.grid(row= 7, column=2,sticky=W+E)

	label9= Label(win, text= "Dining: ", bg= "red", fg= "white")
	label9.grid(row= 8, column=1,sticky=W+E)  
	entry5=Entry(win)
	entry5.grid(row= 8, column=2,sticky=W+E)
	def submit():
		try:
			pool= FALSE
			breakfast= FALSE
			parking= FALSE
			orderin= FALSE
			dining= FALSE
			if(str(entry1.get())[0].lower()== 'y'):
				pool= TRUE
			if(str(entry2.get())[0].lower()== 'y'):
				breakfast= TRUE
			if(str(entry3.get())[0].lower()== 'y'):
				parking= TRUE
			if(str(entry4.get())[0].lower()== 'y'):
				orderin= TRUE
			if(str(entry5.get())[0].lower()== 'y'):
				dining= TRUE
			cursor1.execute("INSERT INTO HotelFacilities(userid, datee, parking, swimmingpool, breakfastincluded, diningincluded, orderin) VALUES (" + userid + "," + "NOW()," + str(int(parking)) + "," + str(int(pool)) + "," + str(int(breakfast)) + "," + str(int(dining)) + "," + str(int(orderin)) + ");")
			connection.commit()
			# print("INSERT INTO HotelFacilities(userid, datee, parking, swimmingpool, breakfastincluded, diningincluded, orderin) VALUES (" + userid + "," + "NOW()," + str(int(parking)) + "," + str(int(pool)) + "," + str(int(breakfast)) + "," + str(int(dining)) + "," + str(int(orderin)) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()			
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 10, column= 1, columnspan= 2)



def room_fac():
	win= Toplevel(root)
	win.title("User Input: Expected Room Facilities")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)
	   

	label5= Label(win, text= "Single Room: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Double Room: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Deluxe Suites: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	entry3=Entry(win)
	entry3.grid(row= 6, column=2,sticky=W+E)

	label8= Label(win, text= "Attached Bathrooms: ", bg= "red", fg= "white")
	label8.grid(row= 7, column=1,sticky=W+E)  
	entry4=Entry(win)
	entry4.grid(row= 7, column=2,sticky=W+E)

	label9= Label(win, text= "Hostel Room: ", bg= "red", fg= "white")
	label9.grid(row= 8, column=1,sticky=W+E)  
	entry5=Entry(win)
	entry5.grid(row= 8, column=2,sticky=W+E)
	def submit():
		try:
			single= FALSE
			double= FALSE
			triple= FALSE
			attached= FALSE
			hostel= FALSE
			if(str(entry1.get())[0].lower()== 'y'):
				single= TRUE
			if(str(entry2.get())[0].lower()== 'y'):
				double= TRUE
			if(str(entry3.get())[0].lower()== 'y'):
				deluxe= TRUE
			if(str(entry4.get())[0].lower()== 'y'):
				attached= TRUE
			if(str(entry5.get())[0].lower()== 'y'):
				hostel= TRUE
			cursor1.execute("INSERT INTO RoomFacilities(userid, datee, singleroom, deluxesuite, doubleroom, attachedbathrooms, hostelroom) VALUES (" + userid + "," + "NOW()," + str(int(single)) + "," + str(int(deluxe)) + "," + str(int(double)) + "," + str(int(attached)) + "," + str(int(hostel)) + ");")
			connection.commit()
			# print("INSERT INTO RoomFacilities(userid, datee, singleroom, deluxesuite, doubleroom, attachedbathrooms, hostelroom) VALUES (" + userid + "," + "NOW()," + str(int(single)) + "," + str(int(deluxe)) + "," + str(int(double)) + "," + str(int(attached)) + "," + str(int(hostel)) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 10, column= 1, columnspan= 2)



def hot_pol():
	win= Toplevel(root)
	win.title("User Input: Expected Hotel Policies")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)
	   

	label5= Label(win, text= "Pets Allowed: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "CheckIN/OUT: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E) 
	variable2= StringVar()
	variable2.set("Flexible") 
	entry2= OptionMenu(win, variable2, "Flexible", "Strict", "Either")
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Healthcare Options: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	entry3=Entry(win)
	entry3.grid(row= 6, column=2,sticky=W+E)

	label8= Label(win, text= "Cancellation Charges: ", bg= "red", fg= "white")
	label8.grid(row= 7, column=1,sticky=W+E)  
	entry4=Entry(win)
	entry4.grid(row= 7, column=2,sticky=W+E)

	label9= Label(win, text= "Medical Charges: ", bg= "red", fg= "white")
	label9.grid(row= 8, column=1,sticky=W+E)  
	entry5=Entry(win)
	entry5.grid(row= 8, column=2,sticky=W+E)
	def submit():
		try:
			pets= FALSE
			healthcare= FALSE
			if(str(entry1.get())[0].lower()== 'y'):
				pets= TRUE
			if(str(entry3.get())[0].lower()== 'y'):
				healthcare= TRUE
			checkinout= str(variable2.get())
			cancellation= float(entry4.get())
			medical= float(entry5.get()) 
			cursor1.execute("INSERT INTO HotelPolicies(userid, datee, cancellationcharges, healthcareoptions, petsallowed, checkinout, medicalcharges) VALUES (" + userid + "," + "NOW()," + str(cancellation) + "," + str(int(healthcare)) + "," + str(int(pets)) + ",\"" + checkinout + "\"," + str(medical) + ");")
			connection.commit()
			# print ("INSERT INTO HotelPolicies(userid, datee, cancellationcharges, healthcareoptions, petsallowed, checkinout, medicalcharges) VALUES (" + userid + "," + "NOW()," + str(cancellation) + "," + str(int(healthcare)) + "," + str(int(pets)) + ",\"" + checkinout + "\"," + str(medical) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 10, column= 1, columnspan= 2)



def din_fac():
	win= Toplevel(root)
	win.title("User Input: Expected Dining Facilities")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)
	   

	label5= Label(win, text= "Breakfast: ", bg= "red", fg= "white")
	label5.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)

	label6= Label(win, text= "Lunch: ", bg= "red", fg= "white")
	label6.grid(row= 5, column=1,sticky=W+E)  
	entry2=Entry(win)
	entry2.grid(row= 5, column=2,sticky=W+E)

	label7= Label(win, text= "Dinner: ", bg= "red", fg= "white")
	label7.grid(row= 6, column=1,sticky=W+E)  
	entry3=Entry(win)
	entry3.grid(row= 6, column=2,sticky=W+E)

	label8= Label(win, text= "Bar: ", bg= "red", fg= "white")
	label8.grid(row= 7, column=1,sticky=W+E)  
	entry4=Entry(win)
	entry4.grid(row= 7, column=2,sticky=W+E)
	def submit():
		try:
			breakfast= FALSE
			lunch= FALSE
			dining= FALSE
			bar= FALSE
			if(str(entry1.get())[0].lower()== 'y'):
				breakfast= TRUE
			if(str(entry2.get())[0].lower()== 'y'):
				lunch= TRUE
			if(str(entry3.get())[0].lower()== 'y'):
				dining= TRUE
			if(str(entry4.get())[0].lower()== 'y'):
				bar= TRUE
			cursor1.execute("INSERT INTO DiningFacilities(userid, datee, bar, lunch, breakfast, dinner) VALUES (" + userid + "," + "NOW()," + str(int(bar)) + "," + str(int(lunch)) + "," + str(int(breakfast)) + "," + str(int(dining)) + ");")
			connection.commit()
			# print("INSERT INTO DiningFacilities(userid, datee, bar, lunch, breakfast, dinner) VALUES (" + userid + "," + "NOW()," + str(int(bar)) + "," + str(int(lunch)) + "," + str(int(breakfast)) + "," + str(int(dining)) + ");")
			win.destroy()
		except Exception as e:
			print (e)
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Ok, I am done!", fg= 'green', command= submit)
	button.grid(row= 9, column= 1, columnspan= 2)



def usr_sat():
	win= Toplevel(root)
	win.title("User Input: User Satisfiability")
	label1= Label(win, text= "User ID: ", bg= "red", fg= "white")
	label1.grid(row= 2, column=1,sticky=W+E)
	label2= Label(win, text= userid, bg= "green", fg= "white")
	label2.grid(row= 2, column=2,sticky=W+E)
	label3= Label(win, text= "User Rating(1-5): ", bg= "red", fg= "white")
	label3.grid(row= 4, column=1,sticky=W+E)  
	entry1=Entry(win)
	entry1.grid(row= 4, column=2,sticky=W+E)
	def submit():
		try:
			rating= float(entry1.get())
			cursor1.execute("INSERT INTO UserSatisfiability(userid, datee, userrating) VALUES (" + userid + "," + "NOW()," + str(rating) + ");")
			connection.commit()
			# print("INSERT INTO UserSatisfiability(userid, datee, userrating) VALUES (" + userid + "," + "NOW()," + str(rating) + ");")
			win.destroy()
		except Exception as e:
			print ("Bad Input. Try Again!!!")
			win.destroy()
	button= Button(win, text= "Submit Rating!", fg= 'green', command= submit)
	button.grid(row= 6, column= 1, columnspan= 2)



nwusr=0
def submitt():
	global nwusr
	if(name.get()=="" or age.get()=="" or gen.get()==""):
		win= Toplevel(root)
		win.title("Error")
		label= Label(win, text= "Insufficient Information Provided. Try Again!", fg= "black", bg= "yellow")
		label.grid(row= 0,sticky=W+E)
	else:
		if nwusr==0:
			try:
				print("New User Created")
				nwusr=1
				cursor1.execute("INSERT INTO UserDetails(userid,username,userage,usergender) VALUES (" + userid + ",\"" + str(name.get())+"\"," + str(int(age.get())) +",\""+ str(gen.get()) + "\");")
				connection.commit()
				# print("INSERT INTO UserDetails(userid,username,userage,usergender) VALUES (" + userid + ",\"" + str(name.get())+"\"," + str(int(age.get())) +","+ str(gen.get()) + ");")
			except Exception as e:
				print (e)
				try:
					print ("User Already Exist. Credentials Updated")
					cursor1.execute("Update UserDetails Set username =\""+ str(name.get()) +"\", userage ="+ str(age.get())+", usergender=\""+ str(gen.get())+ "\" where userid =" + userid +";")
					connection.commit()
					# print("Update UserDetails Set name =\""+ str(name.get()) +"\", age ="+ str(age.get())+", gender=\""+ str(gen.get())+ "\" where userid =" + userid +");")
				except Exception as e:
					print ("Bad Input. Try Again!!!")
					root.destroy()
		else:
			try:
				print ("User Already Exist. Credentials Updated")
				cursor1.execute("Update UserDetails Set username =\""+ str(name.get()) +"\", userage ="+ str(age.get())+", usergender=\""+ str(gen.get())+ "\" where userid =" + userid +";")
				connection.commit()
				# print("Update UserDetails Set name ="+ str(name.get()) +", age ="+ str(age.get())+", gender="+ str(gen.get())+ " where userid =" + userid +");")
			except Exception as e:
				print(e)
				print ("Bad Input. Try Again!!!")
				root.destroy()
			
			
		win= Toplevel(root)
		win.title("User Inputs and Preferences")

		label= Label(win, text= "Choose a Hotel for Leisure", fg= "black", bg= "yellow")
		label.grid(row= 0, column= 1,sticky=W+E)

		labelid= Label(win, text= "User Id: "+userid, fg= "white", bg= "blue")
		labelid.grid(row= 0, column= 2,sticky=W+E)

		adddec= Button(win, text= 'Hotel Brand-Value', fg= 'green', command= hot_br_val)
		adddec.grid(row= 2, column= 1,sticky=W+E)

		addunc= Button(win, text= 'Accessibility', fg= 'green', command= acc)
		addunc.grid(row= 3, column= 1,sticky=W+E)

		addact= Button(win, text= 'Preferences', fg= 'green', command= pref)
		addact.grid(row= 4, column= 1,sticky=W+E)

		addobj= Button(win, text= 'Hotel Facilities', fg= 'green', command= hot_fac)
		addobj.grid(row= 5, column= 1,sticky=W+E)

		showdec= Button(win, text= 'Room Facilities', fg= 'green', command= room_fac)
		showdec.grid(row= 2, column= 2,sticky=W+E)

		showunc= Button(win, text= 'Hotel Policies', fg= 'green', command= hot_pol)
		showunc.grid(row= 3, column= 2,sticky=W+E)

		showact= Button(win, text= 'Dining Facilities', fg= 'green', command= din_fac)
		showact.grid(row= 4, column= 2,sticky=W+E)

		showobj= Button(win, text= 'Show Hotels', fg= 'green', command= usr_sat)
		showobj.grid(row= 5, column= 2,sticky=W+E)
		def edit():
			win.destroy() 
		
		def closee():
			connection.close()
			root.destroy() 
		editbt= Button(win, text= 'Edit Credentials', fg= 'white',bg="black", command= edit)
		editbt.grid(row= 6, column= 1,sticky=W+E)
		editbt1= Button(win, text= 'Close', fg= 'white',bg="black", command= closee)
		editbt1.grid(row= 6, column= 2,sticky=W+E)




def close():
	 root.destroy() 



root= Tk()
root.title("DW MAJOR PROJECT")
root.geometry("+50+150")
root.configure(background='black')

lglbl= Label(root, text= "User SignIn", fg= "white", bg= "orange")
lglbl.grid(row= 0,column=1,sticky=W+E)

label5= Label(root, text= "Name: ", bg= "red", fg= "white")
label5.grid(row= 2, column=1,sticky=W+E)  
name=Entry(root)
name.grid(row= 2, column=2,sticky=W+E)

label6= Label(root, text= "Age: ", bg= "red", fg= "white")
label6.grid(row= 3, column=1,sticky=W+E)  
age=Entry(root)
age.grid(row= 3, column=2,sticky=W+E)

label7= Label(root, text= "Gender: ", bg= "red", fg= "white")
label7.grid(row= 4, column=1,sticky=W+E)  
gen=Entry(root)
gen.grid(row= 4, column=2,sticky=W+E)

subm= Button(root, text= 'Submit', fg= 'green', command= submitt)
subm.grid(row= 5, column= 1,sticky=W+E)

close= Button(root, text= 'Close', fg= 'green', command= close)
close.grid(row= 5, column= 2,sticky=W+E)



# label= Label(root, text= "Choose a Hotel for Leisure", fg= "black", bg= "yellow")
# label.grid(row= 0, column= 1,sticky=W+E)

# labelid= Label(root, text= "User Id: "+userid, fg= "white", bg= "blue")
# labelid.grid(row= 0, column= 2,sticky=W+E)

# adddec= Button(root, text= 'Hotel Brand-Value', fg= 'green', command= hot_br_val)
# adddec.grid(row= 2, column= 1,sticky=W+E)

# addunc= Button(root, text= 'Accessibility', fg= 'green', command= acc)
# addunc.grid(row= 3, column= 1,sticky=W+E)

# addact= Button(root, text= 'Preferences', fg= 'green', command= pref)
# addact.grid(row= 4, column= 1,sticky=W+E)

# addobj= Button(root, text= 'Hotel Facilities', fg= 'green', command= hot_fac)
# addobj.grid(row= 5, column= 1,sticky=W+E)

# showdec= Button(root, text= 'Room Facilities', fg= 'green', command= room_fac)
# showdec.grid(row= 2, column= 2,sticky=W+E)

# showunc= Button(root, text= 'Hotel Policies', fg= 'green', command= hot_pol)
# showunc.grid(row= 3, column= 2,sticky=W+E)

# showact= Button(root, text= 'Dining Facilities', fg= 'green', command= din_fac)
# showact.grid(row= 4, column= 2,sticky=W+E)

# showobj= Button(root, text= 'User Satisfiability', fg= 'green', command= usr_sat)
# showobj.grid(row= 5, column= 2,sticky=W+E)

root.mainloop()
