import pandas as pd

path='online_retail.csv'
df=pd.read_csv(path)
#print(type(rd))
print("1:*************************\n",df.head(10))#muestra las primeras 5 filas o las filas que le indiquemos

#GROUPBY
#
#conteo de valores unicos por columna ver resultado
conteopai=df.Country.value_counts()
print("conteo pais:*************************\n", conteopai.head(10))

#
#sumatoria de las cantidades por pais metodo sum de la columna quantity de la agrupacion por pais
conteogrupos=df.groupby('Country').Quantity.sum()
print("sumatoria de grupos por pais:*************************\n", conteogrupos)

#
sp=df.groupby('Country').UnitPrice.sum()
print("sp:*************************\n", sp)

# 38 paises
sp1=df.groupby('Country').UnitPrice.sum().count()
print("sp1:*************************\n", sp1)

#
sp2=df.groupby('Country').InvoiceNo.count()
print("sp2:*************************\n", sp2)

#operacion estadistica 
conteoestadistica=df.groupby('Country').UnitPrice.agg(['mean','sum'])
print("media y suma:*************************\n", conteoestadistica)

#agrupamos 2 columnas por pais y por stock depues sacamos la sumatoria de sus cantidades
sp4=df.groupby(['Country','StockCode']).Quantity.sum()
print("sp4:*************************\n", sp4)

#aplicando fucnion
def totalrev(group):
    return (group['Quantity']*group['UnitPrice']).sum()

rev=df.groupby('Country').apply(totalrev)
print(":*************************\n", rev)