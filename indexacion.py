import numpy as np

#INDEXACION Y SLICING
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

#BROADCASTING operaciones de array de distintos tamaños para estirarlos al mas grande
# solo puede funcionar si las columnas coinciden con las columnas o el vector pequeño es de un solo dato

pr=np.array([100,200,300])
des=np.array([0.9])
des_pr=pr*des
print("broadcasting", des_pr,"\n")

pr2=np.random.randint(10,99,[3,3])
des2=np.array([10,20,5]) 
des_pr2=pr2-des2
print("precios: \n ", pr2)
print("res:2:\n ", des_pr2)

#OPERADORES LOGICOS
c=np.random.randint(0,10,[3,3])
print(": \n",c)
print(np.all(c>3))# pregunta si TODOS lo elementos son mayores a 3
print(np.any(c>3))# pregunta si ALGUN elemento es mayor a 3

#CONCATENACION
aa=np.random.randint(1,20,[3,3])
bb=np.random.randint(1,20,[3,3])
print("a= \n",aa)
print("b= \n",bb)
concatencion=np.concatenate((aa,bb))
print("concatenado:\n", concatencion)

#STACKING es como suma de posiciones por ejemplo a=2x2, b=2x2
# de manera vertical resultaria 4x2
# de manera horizontal resultaria 2x4

sateckend_v=np.vstack((aa,bb))# concatenacion de manera vertical
print("stacking:\n", sateckend_v,"\n tamaño en vertical:",sateckend_v.shape)
print("compracion:\n",concatencion==sateckend_v)

sateckend_h=np.hstack((aa,bb))# concatenacion de manera horizontal
print("stacking:\n", sateckend_h,"\n tamaño en horizaontal:",sateckend_h.shape)

#SPLIT corta una vecto o array en partes iguales
cc=np.random.randint(0,10,[3,3])
split_cc=np.split(cc,3)
print("1->:\n",cc)
print("2->:\n",split_cc,"\n\n")
#aplanar un elemento
print("reshape=",cc.reshape(-1))
print("ravel  =",cc.ravel())
print("flaten =",cc.flatten())

#
survey_responses = np.array(["bueno", "excelente", "malo", 
                             "bueno", "bueno", "malo", 
                             "malo", "bueno", "excelente", 
                             "malo"])

unique_elements, counts_elements = np.unique(survey_responses, return_counts=True)

counts = dict(zip(unique_elements, counts_elements))
print(unique_elements)
print(counts_elements)
print(counts)

# COPIAS y VISTAS
#vistas
dd=np.arange(10)
vista=dd[1:4]
print("DD",dd)
print("vista",vista)
dd[1:3]=[0,0]
print("DD",dd)
print("vista modificada",vista,"\n")
#copia
ee=np.arange(10)
copia=ee[[1,2]]
print("EE",ee)
print("copia",copia)
ee[1:3]=[0,0]
print("EE",ee)
print("copia nose altera",copia)
#copia
ff=np.arange(10)
copy_dd = np.copy(ff[1:4])
print(ff)
print(copy_dd)
ff[1:3]=[0,0]
print(ff)
print(copy_dd)


#TRANSFORMACION DE ARRAYS
gg=np.random.randint(0,10,[3,3])
trasnpuesta=gg.T
print("original:\n",gg)
print("transpuesta:\n",trasnpuesta)
modificartamaño=gg.reshape(3,3)# modifica el tamaño siempre y cuando le dimension final coincida con el numero de elementos
print("modificar tamaño:\n",modificartamaño)
inversa=gg[::-1]# invierte la posicion de los elementos en vectores su inversa y en matrices invierte las filas como vector
print("inversa:\n",inversa)
inversa2=np.linalg.inv(gg)# saca la inversa de una matris 
print("inversa2:\n",inversa2)
flatening= gg.flatten()
print("aplnado:\n",flatening)

ff=np.arange(1,13)
print("original:\n",ff)
modff=ff.reshape(3,4)
print("modificado:\n", modff)

