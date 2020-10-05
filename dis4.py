import sys
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import random
from ApFinder import *
from ClientFinder2 import *
from HiddenApDiscover2 import *
from deauth import *

english = ['Wireless Security', 'Hello', 'Exit', 'Reset', 'Change Language', '', 'Scanner AP', 'Clients Scan', 'Monitor ON/OFF', 'Scan Hidden AP', 'DDoS Attack', 'Open']
romana = ['Securitate Wireless', 'Salut', 'Iesire', 'Resetare', 'Schimbare limba', '', 'Scanare AP', 'Scanare Clienti', 'Monitorizare ON/OFF', 'Scanare AP Ascuns', 'Atac DDoS', 'Deschide']

interface = 'wlan0'
noPackets = '10000'

#deauth
target = '00:00:00:00:00:00'
gateway = '00:00:00:00:00:00'
iface = 'wlan0'
verbose = '-v'

def choose_language():
	global window2

	window2 = Tk()

	window2.title(english[1])
 
	window2.geometry('350x200')

	window2.configure(background='#23252E')

	window2.mainloop()

def vp_start_gui(lang,changeLang):
	global window
	
	window = Tk()

	window.title(lang[0])
 
	window.geometry('1024x720')

	window.configure(background='#23252E')

	def close_window(): 
		window.destroy()
	 
	def clicked():
		print ("AAAA")

	def openfile():
		filename = askopenfilename()
		print(filename)

	# Insert a menu bar on the main window
	menubar = Menu(window)
	window.config(menu=menubar)

	# Create a menu button labeled "File" that brings up a menu
	filemenu = Menu(menubar)
	helpmenu = Menu(menubar)
	menubar.add_cascade(label='File', menu=filemenu)
	menubar.add_cascade(label='Help', menu=helpmenu)

	# Create entries in the "File" menu
	# simulated command functions that we want to invoke from our menus
	def doPrint(): 
		print ('print')
	def doSave(): 
		print ('doSave')
	def monChange():
		print("aaaamonChange")
	def doScan():
		runScan()
	def clientFinder():
		ClientFinder(interface,noPackets)
	def hiddenApDiscover():
		HiddenApDiscover(interface, noPackets)
	def deauth():
		runDeauth(target, gateway, iface, verbose)
	filemenu.add_command(label='Print', command=doPrint)
	filemenu.add_command(label='Save', command=doSave)
	filemenu.add_separator()
	filemenu.add_command(label='Quit', command=sys.exit)
	

	scanBtn = Button(text=lang[6], bg='#0489D3', foreground='white', font=("Times", 15, "bold"), command=doScan)
	 
	scanBtn.place(relx=0.225, rely=0.25, anchor=CENTER)	


	clientFindBtn = Button(text=lang[7], bg='#0489D3', foreground='white', font=("Times", 15, "bold"), command=clientFinder)
	 
	clientFindBtn.place(relx=0.725, rely=0.25, anchor=CENTER)


	monBtn = Button(text=lang[8], bg='#0489D3', foreground='white', font=("Times", 15, "bold"), command=monChange)
	 
	monBtn.place(relx=0.5, rely=0.425, anchor=CENTER)


	scanApBtn = Button(text=lang[9], bg='#0489D3', foreground='white', font=("Times", 15, "bold"), command=hiddenApDiscover)
	#lbl.grid(column=0, row=0, columnspan=3, sticky='we')
	scanApBtn.place(relx=0.225, rely=0.6, anchor=CENTER)


	ddosBtn = Button(text=lang[10], bg='#0489D3', foreground='white', font=("Times", 15, "bold"), command=deauth)
	#lbl.grid(column=0, row=0, columnspan=3, sticky='we')
	ddosBtn.place(relx=0.725, rely=0.6, anchor=CENTER)


	# #fileOpen
	# openFile = Button(text=lang[11], highlightbackground='blue', foreground='black', font=("Times", 15, "bold"), highlightthickness=10, command=openfile)
	 
	# openFile.place(relx=0.3, rely=0.25, anchor=CENTER)	


	exitBtn = Button(text=lang[2], bg='#0489D3', foreground='white', font=("Times", 30, "bold"), command=close_window)
	 
	exitBtn.place(relx=0.5, rely=0.85, anchor=CENTER)


	if changeLang == 0:
		chLangBtn = Button(text=lang[4], bg='#0489D3', foreground='white', command= lambda: change_language(romana,1))
	elif changeLang == 1:
		chLangBtn = Button(text=lang[4], bg='#0489D3', foreground='white', command= lambda: change_language(english,0))

	chLangBtn.place(relx=0.9, rely=0.05, anchor=CENTER)



	window.mainloop()


if __name__ == '__main__':
	def refresh():
		window.destroy()
		vp_start_gui(english,0)
	def change_language(lang,changeLang):
		window.destroy()
		vp_start_gui(lang,changeLang)	
	vp_start_gui(english,0)
	#choose_language()








