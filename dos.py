import numpy as np

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