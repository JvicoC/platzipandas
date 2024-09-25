import numpy as np
import pandas as pd

path='online_retail.csv'
rd=pd.read_csv(path)
#print(type(rd))
print(rd.head(2))#muestra las primeras 5 filas o las filas que le indiquemos

#sacar en una lista el detalle de columnas
n_columns=rd.columns
print(n_columns)

#sacar el tamaño de las filas y columnas
num_fil, num_col=rd.shape
print("numero de filas   : ",num_fil)
print("numero de columnas: ",num_col)

#sacadno datos de la columna solo con su numero
ds=rd['Quantity']
print("una serie:\n",ds.head(10))
print("una serie en la fila 1:\n",ds[2])

#sacadno datos de la columna por la posicion
ds2=rd.iloc[:, 3]
print("una serie2:\n",ds2.head(10))

#sacadno datos de la columna solo con su numero
ds3=rd.Quantity
print("una serie3:\n",ds3.head(10))

#descripcion estadistica
sy=rd.describe()
print("resumen numeros:\n",sy)

#media
mean_value=ds.mean()
print("la media de la serie quntity es: ",mean_value)

#mediana
median_v=ds.median()
print("la mediana de la serie quntity es: ",median_v)

#msuma
sumatoria=ds.sum()
print("la suma es es: ",sumatoria)

#sdfsdf
conteo=ds.count()
print("el conteo es: ",conteo)
#datos faltantas conultas de atos disponible so nulo

#devuelve true en los lugares vacios
missing=rd.isna()
print("001->: ",missing.head(5))

#realiza un conteo de los lugares vacios
mis_count=rd.isna().sum()
print("002->: ",mis_count)

#eliminar filas con datos faltantes
no_mis_rows=rd.dropna()
print("003->: ",no_mis_rows)

#eliminar columnas con datos faltantes
no_mis_columns=rd.dropna(axis=1)
print("004->: ",no_mis_columns)

#llenar con 0 los valores faltantes
rd_filled=rd.fillna(0)
print("005->: ",rd_filled)

#media del presio unitario para rellenar a los datos faltantes
media_precio=rd.UnitPrice.mean()
print("006media->: ",media_precio)
#llenar los datos faltantes con la media en la columnas del precio unitario
#en este caso devuelve cero por que la columna precio no tiene valores vacios OJO
rd_llenado_con_media=rd.UnitPrice.fillna(media_precio)
print("007->:\n ",rd_llenado_con_media)

lista_datos_aumentados = (rd_llenado_con_media == 4.61)==True
print("lista de datos aumentados:\n",lista_datos_aumentados)

mis_count2=rd.UnitPrice.isna().sum()
print("002->: ",mis_count2)

