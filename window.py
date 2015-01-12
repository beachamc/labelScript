import labels
from Tkinter import *

class Application(Frame):
	def generateLabel(self):
		labels.Generate()
		print('Continue')
		self.quit()
	def createWidgets(self):

		self.label = Label(self, text="Update the .csv file and save it. Once you've done that hit Generate to create the labels.", wraplength=180)
		self.label.grid(row=0, columnspan=2)

		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["command"] = self.quit

		self.QUIT.grid(row=1, column=1, sticky=S)

		self.generate = Button(self)
		self.generate["text"] = "Generate",
		self.generate["command"] = self.generateLabel

		self.generate.grid(row=1, column=0, sticky=S)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack(padx=10, pady=10)
		self.createWidgets()

root = Tk()
root.title("Label Maker")
app = Application(master=root)
app.mainloop()
root.destroy()