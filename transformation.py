from functions import *
import numpy as NP

class Transformation:
	def __init__(self):
		self.space=spatial_default()
		self.color=color_default()
		self.depth=depth_default()
	#	self.traslation=traslation_default()

	
	def setSpace(self,otherspace):
		self.space=otherspace
		return self

	def setColor(self,othercolor):
		self.color=othercolor
		return self

	def setDepth(self,otherdepth):
		self.depth=otherdepth
		return self

#	def setTraslation(self,othertraslation):
#		self.traslation=othertraslation
#		return self


#	def getTraslation(self):
#		return self.traslation

	def getDepth(self):
		return self.depth

	def getSpace(self):
		return self.space

	def getDirx(self):
		return NP.dot(self.getSpace(),NP.array([1,0,0,0]) )[:3]

	def getDiry(self):
		return NP.dot(self.getSpace(),NP.array([0,1,0,0]) )[:3]

	def getDirz(self):
		return NP.dot(self.getSpace(),NP.array([0,0,1,0]) )[:3]

	def getPosition(self):
		return NP.dot(self.getSpace(),NP.array([0,0,0,1]) )[:3]

	def getColor(self):
		return self.color

	def getSize(self):
		return NP.array([NP.linalg.norm(self.getDirx()),NP.linalg.norm(self.getDiry()),NP.linalg.norm(self.getDirz())])

	def transform(self,other):
		nuevaTransformacion = Transformation()
	#	nuevaTransformacion.setSpace(NP.dot(other.getSpace(), self.getSpace())+other.getTraslation())
		nuevaTransformacion.setSpace(NP.dot(other.getSpace(), self.getSpace()))
		nuevaTransformacion.setColor(NP.multiply(other.getColor(), self.getColor()))
		nuevaTransformacion.setDepth(min(self.getDepth(), other.getDepth()))
	#	nuevaTransformacion.setTraslation(traslation_default())
		return nuevaTransformacion

	# debugging
	def mostrar(self):
		print "Space:"
		print self.getSpace()
		print "Color:"
		print self.getColor()
		print "Depth:"
		print self.getDepth()



