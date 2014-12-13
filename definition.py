from transformation import *
import visual as visual
from random import randint

# Clase abstracta que define comportamientos genericos (las subclases que funcionen de manera
#	distinta para algun metodo, lo redefinen)
class Definition:
	def __init__(self):
		self.rules_list = list()

	def AND(self,rule):
		newand = AndDefinition()
		newand.AND(self)
		newand.AND(rule)
		return newand

	def OR(self,rule):
		newor = OrDefinition()
		newor.OR(self)
		newor.OR(rule)
		return newor

	def POW(self,n):
		return PowDefinition(self,n)

	def CORCHETE(self):
		return CorcheteDefinition(self)

	def LESSGREATER(self):
		return LessGreaterDefinition(self)

	def transform(self, transf):
		self.transformation = self.transformation.transform(transf)

	def showPot(self, n, transformation):
		for i in range(0,n):
			self.show(transformation)


## Subclasses

## OR (|)
class OrDefinition(Definition):
	def __init__(self):
		self.rules_list = list()
		self.transformation = Transformation()
		self.timesCalled = 0

	def OR(self,rule):
		self.rules_list.append(rule)
		return self

	def show(self, recTransformation):
		toshow = randint(1,len(self.rules_list))-1
		newTransformation = self.transformation.transform(recTransformation)
		self.rules_list[toshow].show(newTransformation)


## AND (&)
class AndDefinition(Definition):
	def __init__(self):
		self.rules_list = list()
		self.transformation = Transformation()
		self.timesCalled = 0

	def AND(self,rule):
		self.rules_list.append(rule)
		return self

	def show(self,recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		for rule in self.rules_list:
			rule.show(newTransformation)

## POW (^N)
class PowDefinition(Definition):
	def __init__(self,rule,n):
		self.pot = n
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		self.rules_list[0].showPot(self.pot,newTransformation)

# CORCHETE ([E])
class CorcheteDefinition(Definition):
	def __init__(self,rule):
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()
		self.timesCalled = 0

	def show(self, recTransformation):
		newTransformation = self.transformation.transform(recTransformation)
		self.rules_list[0].show(newTransformation)

	def showPot(self, n, recTransformation):
		acumulativeTransformation = Transformation()
		for i in range(0,n):
			acumulativeTransformation = acumulativeTransformation.transform(self.transformation)
			finalTransformation = acumulativeTransformation.transform(recTransformation)
			self.rules_list[0].show(finalTransformation)

# < E >
class LessGreaterDefinition(Definition):
	def __init__(self,rule):
		self.rules_list = list()
		self.rules_list.append(rule)
		self.transformation = Transformation()

	def show(self, recTransformation):
		maybe_show = (randint(1,2) % 2) == 0
		newTransformation = self.transformation.transform(recTransformation)
		if (maybe_show):
			self.rules_list[0].show(newTransformation)

# regla
class RuleDefinition(Definition):
	def __init__(self, rule):
		self.rule = rule
		self.transformation = Transformation()

	def show(self, recTransformation):
		# Actualizo la cantidad de veces que es llamada la regla
		# Aumento en 1 la profundidad de la regla self.rule
		rule2timesCalled_Dict[self.rule] = rule2timesCalled_Dict[self.rule]+1

		newTransformation = self.transformation.transform(recTransformation)
		if (rule2timesCalled_Dict[self.rule] == newTransformation.getDepth()):
			if ((str(self.rule)+'_final') in rule2definition_Dict):
				rule2definition_Dict[(str(self.rule)+'_final')].show(newTransformation)
			else:
				rule2definition_Dict[self.rule].show(newTransformation)
		elif (rule2timesCalled_Dict[self.rule] < newTransformation.getDepth()):
			rule2definition_Dict[self.rule].show(newTransformation)

		# Disminuyo en 1 la profundidad de la regla self.rule (ya termine de hacer un show de toda esta rama)
		rule2timesCalled_Dict[self.rule] = rule2timesCalled_Dict[self.rule]-1


class Void(Definition):
	def __init__(self):
		self.transformation = Transformation()

	def show(self, recTransformation):
		pass
		

class Ball(Definition):
	def __init__(self):
		self.transformation = Transformation()

	def show(self, recTransformation):
		finalTransformation = self.transformation.transform(recTransformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
		visual.ellipsoid(pos=position, size=size, axis=dirx, up=diry, color=color)

class Box(Definition):
	def __init__(self):
		self.transformation = Transformation()

	def show(self, recTransformation):
		finalTransformation = self.transformation.transform(recTransformation)
		position = finalTransformation.getPosition()
		dirx = finalTransformation.getDirx()
		diry = finalTransformation.getDiry()
		color = finalTransformation.getColor()
		size = finalTransformation.getSize()
		visual.box(pos=position, size=size, axis=dirx, up=diry, color=color)

def VOID():
	return Void()

def BALL():
	return Ball()

def BOX():
	return Box()

def RULE(rule):
	return RuleDefinition(rule)


def setearNuevaEntry(rule_name, definition):
	global rule2definition_Dict
	rule2definition_Dict[rule_name] = definition
	rule2timesCalled_Dict[rule_name] = 0

def isUserDefinedRule(rule):
	try:
		return all( char.isalpha() for char in str(rule))
	except Exception, e:
		return False

###
rule2definition_Dict = dict()
rule2timesCalled_Dict = dict()