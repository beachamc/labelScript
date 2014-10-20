## Created by Cameron Beacham
import os, sys, time
from Product import Product

def Generate():

	## open and split the csv file
	infile = open("products.csv", 'r')
	contents = infile.read()
	infile.close()
	products = csvParser(contents)
	outfile = open('labels.html', 'w')
	
	infile = open('header.html', 'r')
	html = infile.read()
	outfile.write(html)
	infile.close()

	for i in range(len(products)):
		deviceType = products[i].getDeviceType()
		if(deviceType == "IPHONE"):
			for j in range(products[i].getNumLabels()):
				outfile.write('\n\t'+iPhoneLabel(products[i]))
		elif(deviceType == "IPAD"):
			for j in range(products[i].getNumLabels()):
				outfile.write('\n\t'+iPadLabel(products[i]))
		elif(deviceType == "CPU"):
			for j in range(products[i].getNumLabels()):
				outfile.write('\n\t'+CPULabel(products[i]))
		else:
			pass
			## will be expanded to custom labels in the future

	infile = open('footer.html', 'r')
	html = infile.read()
	outfile.write(html)
	infile.close()



## takes in a string read from a csv file
## returns a list of objects of type Product
def csvParser(myString):
	products = myString.split('\r')
	for i in range(len(products)):
		products[i] = products[i].split(',')
	products.pop(0)
	for i in range(len(products)):
		try:
			int(products[i][7])
		except:
			continue
		else:
			temp = Product()
			if(products[i][0] != "n/a"):
				temp.setSku(products[i][0].upper())
			if(products[i][1] != "n/a"):
				temp.setDeviceType(products[i][1].upper())
			if(products[i][2] != "n/a"):
				temp.setColor(products[i][2].upper())
			if(products[i][3] != "n/a"):
				temp.setCarrier(products[i][3].upper())
			if(products[i][4] != "n/a"):
				temp.setSize(products[i][4].upper())
			if(products[i][5] != "n/a"):
				temp.setSpecs(products[i][5].upper())
			if(products[i][6] != "n/a"):
				temp.setName(products[i][6])
			if(products[i][7] != "n/a"):
				temp.setNumLabels(int(products[i][7]))
			products[i] = temp
	return products

def iPhoneLabel(product):
	output = '<div class="iPhoneLabels '+str(product.getColor())+'">\n<div class="carrier">'+str(product.getCarrier())+'</div>\n<div class="partNum">'+str(product.getSku())+'</div>\n<div class="details">\n<div class="size">'+str(product.getSize())+'</div>\n<div class="color">'+str(product.getColor())+'</div>\n</div>\n</div>'
	return output

def iPadLabel(product):
	output = '<div class="iPadLabels '+str(product.getColor())+'">\n<div class="leftBox">\n<div class="carrier">'+str(product.getCarrier())+'</div>\n</div>\n<div class="rightBox">\n<div class="partNum">'+str(product.getSku())+'</div>\n<div class="details">\n<div class="name">'+str(product.getName())+'</div>\n<div class="size">'+str(product.getSize())+'</div>\n</div>\n</div>\n</div>'
	return output

def CPULabel(product):
	output = '<div class="computerLabels">\n<div class="leftBox">\n<div class="computer">'+str(product.getName())+'</div>\n</div>\n<div class="rightBox">\n<div class="partNum">'+str(product.getSku())+'</div>\n<div class="specs">'+str(product.getSpecs())+'</div>\n</div>\n</div>'
	return output

if __name__ == '__main__':
	Generate()
 