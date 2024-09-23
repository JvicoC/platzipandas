import numpy as np

escalar=np.array(42) #dimenssiones de tipo escalar dimensionalidad 0
print(type(escalar))
print(escalar)

vector=np.array([30,29,35,31,33]) # vectores
print(type(vector))
print(vector)

matris=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matris",matris)

tensor=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print("varias dimensiones",tensor)

array_arange=np.arange(10) #generar a travez de una rango de 10
print("arange",array_arange)

eye_matris=np.eye(6) #llenar matris identidad
print("eye identidad",eye_matris)

diag=np.diag([1,2,3,4,5,6])# creacion de matris diagonal con los datos de 1,2,3,4,5,6
print("diagonal",diag)

random=np.random.random([2,3])# 2 es cabtida de files y 3 cantidad de columnas
print("random",random)