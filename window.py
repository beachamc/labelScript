import labels
from Tkinter import *

class Application(Frame):
	def generateLabel(self):
		labels.Generate()
		self.quit()
	def createWidgets(self):
		self.label = Label(self)
		self.label["text"] = "Click the button below when you are ready to generate the labels."

		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["command"] = self.quit

		self.QUIT.grid()

		self.generate = Button(self)
		self.generate["text"] = "Generate",
		self.generate["command"] = self.generateLabel

		self.generate.grid()

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
root.title("Label Maker")
app = Application(master=root)
app.mainloop()
root.destroy()