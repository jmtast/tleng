import numpy as num
from math import *

# Funciones para los estados iniciales (default) de los elementos
def spatial_default():
	return num.identity(4)

def color_default():
	return num.array([1,1,1])

def depth_default():
	return 100

def translation_default():
	return num.zeros((4,4))

# Funcion para pasar de Grados a Radianes
def degree2radian(deg):
	return (deg/180)*pi

# Funcion para pasar de Radianes a Grados
def radian2degree(rad):
	return (rad*180)/pi


# Funciones para rotaciones en x, y, z
def rot_x(x):
	res = num.identity(4)
	x = float(x)
	res[1][1] =  cos(degree2radian(x))
	res[1][2] =  sin(degree2radian(x))
	res[2][1] = -sin(degree2radian(x))
	res[2][2] =  cos(degree2radian(x))
	return res

def rot_y(y):
	res = num.identity(4)
	y = float(y)
	res[0][0] =  cos(degree2radian(y))
	res[0][2] =  sin(degree2radian(y))
	res[2][0] = -sin(degree2radian(y))
	res[2][2] =  cos(degree2radian(y))
	return res

def rot_z(z):
	res = num.identity(4)
	z = float(z)
	res[0][0] =  cos(degree2radian(z))
	res[0][1] =  sin(degree2radian(z))
	res[1][0] = -sin(degree2radian(z))
	res[1][1] =  cos(degree2radian(z))
	return res

# Funciones para modificar los canales del color
def col_r(r):
	return num.array([r,1,1])

def col_r(g):
	return num.array([1,g,1])

def col_r(b):
	return num.array([1,1,b])

# Funciones para modificar la translacion
def trans_x(x):
	res = num.zeros((4,4))
	res[0][3] = x
	return res

def trans_y(y):
	res = num.zeros((4,4))
	res[1][3] = y
	return res

def trans_z(z):
	res = num.zeros((4,4))
	res[2][3] = z
	return res

# Funciones para escalar
def scale_x(x):
	res = num.identity(4)
	res[0][0] = x
	return res

def scale_y(y):
	res = num.identity(4)
	res[1][1] = y
	return res

def scale_z(z):
	res = num.identity(4)
	res[2][2] = z
	return res

def scale_all_axis(n):
	res = num.identity(4)
	res[0][0] = n
	res[1][1] = n
	res[2][2] = n
	return res
