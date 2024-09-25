import numpy as np
import pandas as pd

# Leer archivos de excel, actualizar el openpyxl pip install openpyxl
'''df=pd.read_excel('pu.xlsx', sheet_name='Hoja1')
print(type(df))
print(df)'''

path='online_retail.csv'
rd=pd.read_csv(path)
print(type(rd))
print(rd.head(2))#muestra las primeras 5 filas o las filas que le indiquemos

aa=np.random.randint(1,20,[3,3])
print("a:\n",aa)
dfa=pd.DataFrame(aa, columns=['A','B','C'])# nombra las cabeceras o columnas de los datos
print("df:\n",dfa)

lista=[[1,'jhon',22],[2,'jose',24]]
dfdd=pd.DataFrame(lista, columns=['ID','Nombre','Edad'])
print("df:\n",dfdd)

dic=[{'ID':1,
        'nombre':'juan',
        'edad':22},
        {'ID':2,
        'nombre':'pepe',
        'edad':30},]
dfdic=pd.DataFrame(dic)
print("df:\n",dfdic)

dic2={'ID':[1,2,3],'nombre':['pedro','javier','lote'],'edad':[25,60,35]}
dfdic2=pd.DataFrame(dic2)
print("df:\n",dfdic2)

#SERIALIZAR
dic3={'ID':pd.Series([1,2,3,4,5,6]),
      'nombre':pd.Series(['pedro','javier','lote','mote','lito','berno']),
      'edad':pd.Series([25,60,35,18,52,22])
      }
dfdic3=pd.DataFrame(dic3)
print("df:\n",dfdic3)
