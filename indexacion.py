import numpy as np

a=np.array([10,20,30,40,30])
print(a[0])
print(a[1])
print(a[-1])
print(a[1:4],"\n \n")

bool_index=a==30 # bool_index=a>30, bool_index=a<30, bool_index=a<=30   devuelve el valor booleano de la comparacion
print(bool_index)
print(type(bool_index))

index=[0,3,4]
print(a[index])

b=np.random.randint(1,20,[4,4])
print("matris \n",b)
print("muestra la posicion del selecionado",b[2,2])#muestra la posicion
print("001= \n",b[0:2,0:2]) # corte de la matris mas pequeña de 2x2 de la posicion 0 a la 1
print("002= \n",b[1:3,1:3])
print("003= \n",b[2:4,2:4])
print("004= \n",b[0:3,0:3]) # corte de la matris mas pequeña de 3x3 de la posicion 0 a la 2

print("nuevos datos \n")

# Obtener las matrices de índices
print("el tamano de la matris es:",b.shape) # devuelva el tamaño de la matris

indices = np.indices((4,4))
#muestra los indices en 2 matrices una con la posicion de las filas y otra con la posision de las columnas del tamaño indicado en este caso 4x4
print("2:",indices) 

pr=np.array([100,200,300])
des=np.array([0.9])
des_pr=pr*des
print("broadcasting", des_pr,"\n")

pr2=np.random.randint(10,99,[2,2])
des2=np.array([10,20]) # el broadcasting solo puede funcionar si las columnas coinciden con las columnas o el vector pequeño es de un solo dato
des_pr2=pr2-des2
print("precios: \n ", pr2)
print("broadcasting2:\n ", des_pr2)