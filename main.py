import customtkinter as CTk
import tkinter
from tkinter import filedialog as fd
import sqlite3

labelPadx = 13
labelPady = 7
entryPadx = 15
entryPady = 5
DbFilename = "logins.db"

def submitData():
	con = sqlite3.connect(DbFilename)
	cur = con.cursor()
	cur.execute("INSERT INTO logins VALUES (?, ?, ?)", (websiteEntry.get(), usernameEntry.get(), passwordEntry.get()))
	con.commit()
	con.close()

def viewLogins():
	dialog = CTk.CTkInputDialog(text="Enter Master Password: ", title="Master Password")
	file = open("masterpass.txt")
	masterPass = file.readline()
	if masterPass == dialog.get_input():
		print("CORRECT")

def DBFile():
	global DbFilename
	DbFilename = fd.askopenfilename()

def command_1():
	window.grid_forget()
	sideFrame.grid_forget()
	window.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
	root.geometry("510x500")

def command_2():
	window.grid_forget()
	sideFrame.grid_forget()
	sideFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
	root.geometry("587x500")

def DBsearch():
	value = optionMenu.get()
	userInput = searchEntry.get()
	con = sqlite3.connect(DbFilename)
	cur = con.cursor()
	if value == "Website":
		cur.execute(f'SELECT * FROM "logins" WHERE website = ?',(userInput,))
	elif value == "Username":
		cur.execute(f'SELECT * FROM "logins" WHERE username = ?',(userInput,))
	result = cur.fetchall()
	# print(result)
	con.commit()
	con.close()

	for item in result:
		foundWebsite = item[0]
		foundUsername = item[1]
		foundPassword = item[2]

		lines = CTk.CTkLabel(master = searchResultFrame,
										  text= "-------------------------",
										  text_color="#d1cfcf",
										  font=('Monoscope', 19))
		lines.pack()

		foundWebsite_Label = CTk.CTkLabel(master = searchResultFrame,
										  text=f"Website: {foundWebsite}",
										  text_color="#d1cfcf",
										  font=('Monoscope', 19))
		foundWebsite_Label.pack()

		foundUsername_Label = CTk.CTkLabel(master = searchResultFrame,
										   text=f"Username: {foundUsername}",
										   text_color="#d1cfcf",
										   font=('Monoscope', 19))
		foundUsername_Label.pack()

		foundPassword_Label = CTk.CTkLabel(master = searchResultFrame,
										   text=f"Password: {foundPassword}",
										   text_color="#d1cfcf",
										   font=('Monoscope', 19))
		foundPassword_Label.pack()

def ClearSearchResult():
	for widget in searchResultFrame.winfo_children():
		widget.destroy()

def about():
	aboutWin = CTk.CTk()
	aboutWin.title("About")
	aboutWin.geometry("500x90")
	aboutWin.configure(fg_color="#3b3b3b")
	label1 = CTk.CTkLabel(aboutWin,
						  text="Created by: oxonomy",
						  text_color="#d1cfcf",
						  font=('Monoscope', 19))
	label2 = CTk.CTkLabel(aboutWin,
						  text="Github: github.com/0xonomy",
						  text_color="#d1cfcf",
						  font=('Monoscope', 19))
	label3 = CTk.CTkLabel(aboutWin,
						  text="You can do whatever you want whith this, idc",
						  text_color="#d1cfcf",
						  font=('Monoscope', 20))
	label1.pack()
	label2.pack()
	label3.pack()
	aboutWin.mainloop()

root = CTk.CTk()
root.title("Password Manager 0.0.1")
# root.geometry("510x500")
root.geometry("587x500")
root.configure(fg_color="#3b3b3b")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)

sideBar = CTk.CTkFrame(root, fg_color="#545454", height=480)
sideBar.grid(row=0, column=0, pady=10, sticky="nsew")

window = CTk.CTkFrame(root, fg_color="#545454", height=480)
# window.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

sideFrame = CTk.CTkFrame(root, fg_color="#545454", height=480)
sideFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

sideBut1 = CTk.CTkButton(sideBar, text="New Login", command=command_1)
sideBut2 = CTk.CTkButton(sideBar, text="Search Login", command=command_2)
sideBut1.grid(row=0, column=0, padx=10, pady=5)
sideBut2.grid(row=1, column=0, padx=10, pady=5)

DbFile = CTk.CTkButton(sideBar, text="DB File", command=DBFile)
DbFile.grid(row=2, column=0, pady=(330, 10))

aboutButton = CTk.CTkButton(sideBar, text="About", command=about)
aboutButton.grid(row=3, column=0)

websiteLabel = CTk.CTkLabel(window,
							text="Enter Website:",
							text_color="#d1cfcf",
							font=('Monoscope', 19))
usernameLabel = CTk.CTkLabel(window,
							text="Enter username:",
							text_color="#d1cfcf",
							font=('Monoscope', 19))
passwordLabel = CTk.CTkLabel(window,
							text="Enter password:",
							text_color="#d1cfcf",
							font=('Monoscope', 19))

#Entries for data
websiteEntry = CTk.CTkEntry(window, 
							placeholder_text="Website",
							font=('Monoscope', 19), 
							width=300, 
							height= 40)
usernameEntry = CTk.CTkEntry(window, 
							placeholder_text="Username", 
							font=('Monoscope', 19), 
							width=300, 
							height= 40)
passwordEntry = CTk.CTkEntry(window, 
							placeholder_text="Password", 
							font=('Monoscope', 19), 
							width=300, 
							height= 40)

submitButton = CTk.CTkButton(window, text="Submit Data", command=submitData)

websiteLabel.pack(anchor=tkinter.NW,
				  padx=labelPadx,
				  pady=labelPady)
websiteEntry.pack(anchor=tkinter.NW,
				  padx=entryPadx,
				  pady=entryPady)
usernameLabel.pack(anchor=tkinter.NW,
				  padx=labelPadx,
				  pady=labelPady)
usernameEntry.pack(anchor=tkinter.NW,
				  padx=entryPadx,
				  pady=entryPady)
passwordLabel.pack(anchor=tkinter.NW,
				  padx=labelPadx,
				  pady=labelPady)
passwordEntry.pack(anchor=tkinter.NW,
				  padx=entryPadx,
				  pady=entryPady)
submitButton.pack(anchor=tkinter.NW,
				  padx=entryPadx,
				  pady=20)

sideTopFrame = CTk.CTkFrame(sideFrame,
						    fg_color="#545454",
						    height=200)
sideTopFrame.grid(row=0, column=0, sticky="nsew")

viewLoginsButton = CTk.CTkButton(sideTopFrame,
								 text="View Logins",
								 command=viewLogins)
searchByLabel = CTk.CTkLabel(sideTopFrame,
							text="Search by: ",
							text_color="#d1cfcf",
							font=('Monoscope', 19))
optionMenu = CTk.CTkOptionMenu(sideTopFrame,
							   values=['Username', 'Website'],
							   width=130)
optionMenu.set('Username')
searchEntry = CTk.CTkEntry(sideTopFrame,
						  placeholder_text="Search:",
						  font=('Monoscope', 19),
						  width=230,
						  height=40)
searchButton = CTk.CTkButton(sideTopFrame,
							 text='Search',
							 width=120,
							 command=DBsearch)
searchResultFrame = CTk.CTkFrame(sideFrame,
								fg_color="#303030",
								height=330,
								width=400)
clearResultButton = CTk.CTkButton(sideFrame,
								  text='Clear',
								  width=400,
								  command=ClearSearchResult)
clearResultButton.grid(row=4, pady=(15, 0))

searchByLabel.grid(row=0,
				   column=0,
				   padx=labelPadx,
				   pady=labelPady)
optionMenu.grid(row=0,
				column=1,
				padx=5)
searchEntry.grid(row=1,
				column=0,
				padx=10)
searchButton.grid(row=1,
				column=1,
				padx=5)
searchResultFrame.grid(padx=5,
					   pady=10,
					   sticky="nsew")

window.mainloop()