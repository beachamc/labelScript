class Product:
	def __init__(self):
		self.sku = False
		self.deviceType = False
		self.color = False
		self.carrier = False
		self.size = False
		self.specs = False
		self.name = False
		self.numLabels = False

	def getSku(self):
		return self.sku

	def getDeviceType(self):
		return self.deviceType

	def getColor(self):
		return self.color

	def getCarrier(self):
		return self.carrier

	def getSize(self):
		return self.size

	def getSpecs(self):
		return self.specs

	def getName(self):
		return self.name

	def getNumLabels(self):
		return self.numLabels

	def getSummary(self):
		return str(self.sku) + " | " + str(self.deviceType)  + " | " + str(self.color)  + " | " + str(self.carrier)  + " | " + str(self.size)  + " | " + str(self.specs) + " | " + str(self.name) + " | " + str(self.numLabels)

	def setSku(self,newSku):
		self.sku = newSku

	def setDeviceType(self,newDeviceType):
		self.deviceType = newDeviceType

	def setColor(self,newColor):
		self.color = newColor

	def setCarrier(self,newCarrier):
		self.carrier = newCarrier

	def setSize(self,newSize):
		self.size = newSize

	def setSpecs(self,newSpecs):
		self.specs = newSpecs

	def setName(self, newName):
		self.name = newName

	def setNumLabels(self, newNumLabels):
		self.numLabels = newNumLabels


