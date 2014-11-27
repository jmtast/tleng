from transformation import *
import visual as visual

class Definition:
	def __init__(self,id):
		self.id = id
		self.rules_list = list()
		pass

	def AND(self,rule):
		global nextId
		global rule2definition_Dict
		nextId = nextId+1
		newand = AndDefinition(nextId)
		newand.AND(self.id)
		newand.AND(rule)
		rule2definition_Dict[nextId] = newand
		return nextId

	def OR(self,rule):
		global nextId
		global rule2definition_Dict
		nextId = nextId+1
		newor = OrDefinition(nextId)
		newor.OR(self.id)
		newor.OR(rule)
		rule2definition_Dict[nextId] = newor
		return nextId

	def POT(self,rule,n):
		global nextId
		global rule2definition_Dict
		nextId = nextId+1
		rule2definition_Dict[nextId] = PotDefinition(rule,n,nextId)
		return nextId

	def CORCHETE(self,rule):
		global nextId
		global rule2definition_Dict
		nextId = nextId+1
		rule2definition_Dict[nextId] = CorcheteDefinition(rule,nextId)
		return nextId

#	def show(self, profundidad):
#		pass
#
#	def showPot(profundidad,n):
#		for 1 in range(1,n):
#			self.show(profundidad)
#		pass


## Subclasses

## OR (|)
class OrDefinition(Definition):
	def __init__(self,id):
		self.id=id
		self.rules_list = list()
		self.transformation = Transformation()

	def OR(self,rule):
		self.rules_list.append(rule)
		return nextId

	def show(self, profundidad, transformation):
		toshow = randint(1,len(self.rules_list))-1
		rule2definition_Dict[self.rules_list[toshow]].show(profundidad, self.transform.transform(transf) )
	#	print "OR("
	#	for rule in self.rules_list:
	#		rule2definition_Dict[rule].show(profundidad,self.transformation.transform(transformation))
	#	print ")"
## AND (&)
class AndDefinition(Definition):
	def __init__(self,id):
		self.id=id
		self.rules_list = list()
		self.transformation = Transformation()

	def AND(self,rule):
		self.rules_list.append(rule)
		return nextId

	def show(self, profundidad,transformation):
		print "AND("
	#	print self.rules_list
		for rule in self.rules_list:
			rule2definition_Dict[rule].show(profundidad,self.transformation.transform(transformation))
		print ")"

## POT (^N)
class PotDefinition(Definition):
	def __init__(self,rule,n,id):
		self.pot = n
		self.id=id
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
	#	rules_list[0].showPot(profundidad,self.pot)
		print "POT("
		rule2definition_Dict[self.rules_list[0]].show(profundidad,self.transformation.transform(transformation))
		print self.n
		print ")"

# CORCHETE ([E])
class CorcheteDefinition(Definition):
	def __init__(self,rule,id):
		self.id=id
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
		print "["
		rule2definition_Dict[self.rules_list[0]].show(profundidad,self.transformation.transform(transformation))
		print "]"

	def showPot(self, profundidad, n, transformation):
#		for 1 in range(1,n):
		pass


class TransformatedDefinition(Definition):
	def __init__(self,rule,id):
		self.rules_list = list()
		self.id=id
		self.rules_list.append(rule)
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
		pass

	def showPot(self, profundidad,n):
		pass

class Void(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
		pass


class Ball(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
		finalTransformation = self.transformation.transform(transformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
		print color
		visual.ellipsoid(pos=position, size=size, axis=dirx, up=diry, color=color)

class Box(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()

	def show(self, profundidad, transformation):
		finalTransformation = self.transformation.transform(transformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
		print color
		visual.box(pos=position, size=size, axis=dirx, up=diry, color=color)

def VOID():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Void(nuevaEntry))
	return nuevaEntry
#	return 0

def BALL():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Ball(nuevaEntry))
	return nuevaEntry
#	return 1

def BOX():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Box(nuevaEntry))
	return nuevaEntry
#	return 2




def getNextId():
	global nextId
	nextId = nextId+1
	return nextId

def setearNuevaEntry(id, definition):
	global rule2definition_Dict
	rule2definition_Dict[id] = definition


nextId = 0
rule2definition_Dict = dict()

#rule2definition_Dict[0] = PrimitiveDefinition('_',0)
#rule2definition_Dict[1] = PrimitiveDefinition('ball',1)
#rule2definition_Dict[2] = PrimitiveDefinition('box',2)