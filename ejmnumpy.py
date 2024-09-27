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





array=np.array([[1,2,3],[4,5,6]])
print(array.ndim)# dimensiones
print(array.shape)# tamaño de la matris
print(array.dtype)# tipo

z=np.array(3, dtype=np.uint8)
print("z=",z)

#print(z.)

sum=np.sum(array)# sumatoria
print(sum)

mean=np.mean(array) #media
print(mean)

std=np.std(array) # desviacion estandar
print(std)

z=np.array(3, dtype=np.uint8)
print("z=",z)

double_array=np.array([1,2,3], dtype='d')
print("convertido a doubles:",double_array)

z=z.astype(np.float64)
print("float64:",z)

sum=np.sum(array)
print(sum)






a=np.random.randint(1,10,[2,2])
print("a= \n",a)

b=np.random.randint(1,10,[2,2])
print("b= \n",b)

c=np.dot(a,b)
print("el producto es = \n",c)

deter=np.linalg.det(a)
print("determinantes es= \n", deter)

inv=np.linalg.inv(a)
print("inversa es= \n", inv)

valores_propios, vectores_propios = np.linalg.eig(a)
print("Valores propios de A:\n", valores_propios)
print("Vectores propios de A:\n", vectores_propios)

bb = np.array([1, 2])
X = np.linalg.solve(a, bb)
print("Solución del sistema AX = B:\n", X)