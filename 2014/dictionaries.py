from functions import *
from transformation import *
from definition import *

def getPrimitiveAction(primitive):
	primitive2action_dict = dict(
			ball = 'BALL',
			box = 'BOX',
			_ = 'VOID'
		)
	res = globals()[primitive2action_dict[primitive]]()
	return res


def getTransformationAssociated(transf, num):
	res = Transformation()
	depthTransformation = 'd'
	if (isSpaceTransformation(transf)):
		newSpace = getTransf(transf, num)
		res.setSpace(newSpace)
	elif (isColorTransformation(transf)):
		newColor = getTransf(transf, num)
		res.setColor(newColor)
	else : # Es depthTransformation
		res.setDepth(num)

	return res

def isSpaceTransformation(transf):
	return transf in ['s','sx','sy','sz','tx','ty','tz','rx','ry','rz']
	
def isColorTransformation(transf):
	return transf in ['cr','cb','cg']

def getTransf(transf, num):
	return globals()[transf](num)	


