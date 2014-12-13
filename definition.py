from transformation import *
import visual as visual
from random import randint

# Clase abstracta que define comportamientos genericos (las subclases que funcionen de manera
#	distinta para algun metodo, lo redefinen)
class Definition:
	def __init__(self,id):
		self.id = id
		self.rules_list = list()
		pass

	def AND(self,rule):
		nuevaEntry = getNextId()
		newand = AndDefinition(nuevaEntry)
		newand.AND(self.id)
		newand.AND(rule)
		setearNuevaEntry(nuevaEntry,newand)
		return nuevaEntry

	def OR(self,rule):
		nuevaEntry = getNextId()
		newor = OrDefinition(nuevaEntry)
		newor.OR(self.id)
		newor.OR(rule)
		setearNuevaEntry(nuevaEntry,newor)
		return nuevaEntry

	def POT(self,n):
		nuevaEntry = getNextId()
		setearNuevaEntry(nuevaEntry,PotDefinition(self.id,n,nuevaEntry) )
		return nuevaEntry

	def CORCHETE(self):
		nuevaEntry = getNextId()
		setearNuevaEntry(nuevaEntry,CorcheteDefinition(self.id,nuevaEntry) )
		return nuevaEntry

	def LESSGREATER(self):
		nuevaEntry = getNextId()
		setearNuevaEntry(nuevaEntry,LessGreaterDefinition(self.id,nuevaEntry) )
		return nuevaEntry

	def transform(self, transf):
		self.transformation = self.transformation.transform(transf)

	def showPot(self, n, transformation):
		for i in range(0,n):
			self.show(transformation)




## Subclasses

## OR (|)
class OrDefinition(Definition):
	def __init__(self,id):
		self.id=id
		self.rules_list = list()
		self.transformation = Transformation()
		self.timesCalled = 0

	def OR(self,rule):
		self.rules_list.append(rule)
		return nextId

	def show(self, recTransformation):
		toshow = randint(1,len(self.rules_list))-1
		newTransformation = self.transformation.transform(recTransformation)
		rule2definition_Dict[self.rules_list[toshow]].show(newTransformation)


## AND (&)
class AndDefinition(Definition):
	def __init__(self,id):
		self.id=id
		self.rules_list = list()
		self.transformation = Transformation()
		self.timesCalled = 0

	def AND(self,rule):
		self.rules_list.append(rule)
		return nextId

	def show(self,recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		for rule in self.rules_list:
			rule2definition_Dict[rule].show(newTransformation)

## POT (^N)
class PotDefinition(Definition):
	def __init__(self,rule,n,id):
		self.pot = n
		self.id=id
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		rule2definition_Dict[self.rules_list[0]].showPot(self.pot,newTransformation)

# CORCHETE ([E])
class CorcheteDefinition(Definition):
	def __init__(self,rule,id):
		self.id=id
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		rule2definition_Dict[self.rules_list[0]].show(newTransformation)

	def showPot(self, n, recTransformation):
		# Estoy en el caso de [A] : T ^ N : recTransformation
		acumulativeTransformation = Transformation()
	#	for i in self.rules_list:
		for i in range(0,n):
		#	acumulativeTransformation = self.transformation.transform(acumulativeTransformation)
			acumulativeTransformation = acumulativeTransformation.transform(self.transformation)
			# En cada paso i, acumulativeTransformation = T^i
			# Ahora calculo recTransformation * T^i
			rule2definition_Dict[self.id].show(acumulativeTransformation.transform(recTransformation))

# < E >
class LessGreaterDefinition(Definition):
	def __init__(self,rule,id):
		self.rules_list = list()
		self.id=id
		self.rules_list.append(rule)
		self.transformation = Transformation()

	def show(self, recTransformation):
		maybe_show = (randint(1,2) % 2) == 0
		newTransformation = self.transformation.transform(recTransformation)
		if (maybe_show):
			rule2definition_Dict[self.rules_list[0]].show(newTransformation)
		else:
			rule2definition_Dict[VOID()].show(Transformation())

# regla
class RuleDefinition(Definition):
	def __init__(self, id, rule):
		self.id=id
		self.rule = rule
		self.rules_list = list()
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		# Actualizo la cantidad de veces que es llamada la regla
		# Aumento en 1 la profundidad de la regla self.rule
		rule2timesCalled_Dict[self.rule] = rule2timesCalled_Dict[self.rule]+1

		newTransformation = self.transformation.transform(recTransformation)
		if (rule2timesCalled_Dict[self.rule] == newTransformation.getDepth()):
			if ((str(self.id)+'_final') in rule2definition_Dict):
				rule2definition_Dict[(str(self.id)+'_final')].show(newTransformation)
			else:
				rule2definition_Dict[self.rule].show(newTransformation)
		elif (rule2timesCalled_Dict[self.rule] < newTransformation.getDepth()):
			rule2definition_Dict[self.rule].show(newTransformation)

		# Disminuyo en 1 la profundidad de la regla self.rule (ya termine de hacer un show de toda esta rama)
		rule2timesCalled_Dict[self.rule] = rule2timesCalled_Dict[self.rule]-1


class Void(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		self.timesCalled = self.timesCalled+1
		visual.box(pos=[0,0,0], size=[0,0,0], axis=[0,0,0], up=[0,0,0], color=[0,0,0])
		

class Ball(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		finalTransformation = self.transformation.transform(recTransformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
	#	print "mostrando ellipse con transformacion"
	#	print finalTransformation.getSpace()
		visual.ellipsoid(pos=position, size=size, axis=dirx, up=diry, color=color)

class Box(Definition):
	def __init__(self,id):
		self.id=id
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		finalTransformation = self.transformation.transform(recTransformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
	#	print "mostrando caja con transformacion"
	#	print finalTransformation.getSpace()
		visual.box(pos=position, size=size, axis=dirx, up=diry, color=color)

def VOID():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Void(nuevaEntry))
	return nuevaEntry

def BALL():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Ball(nuevaEntry))
	return nuevaEntry

def BOX():
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,Box(nuevaEntry))
	return nuevaEntry

def RULE(rule):
	nuevaEntry = getNextId()
	setearNuevaEntry(nuevaEntry,RuleDefinition(nuevaEntry,rule) )
	return nuevaEntry


####
def getNextId():
	global nextId
	nextId = nextId+1
	return nextId

def setearNuevaEntry(id, definition):
	global rule2definition_Dict
	rule2definition_Dict[id] = definition
	if (isUserDefinedRule(id)):
		rule2timesCalled_Dict[id] = 0




def isUserDefinedRule(rule):
	return all(not char.isdigit() for char in str(rule))


###
nextId = 0
rule2definition_Dict = dict()
rule2timesCalled_Dict = dict()