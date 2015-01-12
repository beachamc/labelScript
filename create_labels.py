import os, sys, webbrowser
import subprocess

if __name__ == '__main__':

	directory = os.path.dirname(os.path.realpath(__file__))

	## open the csv file
	
	if (sys.platform == 'darwin'):
		os.system('open ' + os.path.join(directory, "products.csv"))
	elif (sys.platform == 'win32'):
		os.system('start ' + os.path.join(directory, "products.csv"))
	elif (sys.platform.startswith('linux')):
		os.system('xdg-open ' + os.path.join(directory, "products.csv"))

	## launch the gui
	subprocess.call(['python', os.path.join(directory, 'window.py')])

	## open labels.py 
	print('process done, opening browser')
	webbrowser.open('file://' + os.path.join(directory, "labels.html"))