import numpy as np

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
X = np.linalg.solve(a, b)
print("Solución del sistema AX = B:\n", X)