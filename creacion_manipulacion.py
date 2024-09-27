import pandas as pd

path='online_retail.csv'
df=pd.read_csv(path)
#print(type(rd))
print("1:*************************\n",df.head(10))#muestra las primeras 5 filas o las filas que le indiquemos

#crear una columna
df['TotalPrice']=df['Quantity']*df['UnitPrice']
print("2:*************************\n",df.head(10))#muestra las primeras 10 filas o las filas que le indiquemos

#nueva columna por condicionales
df['ValorAlto']=df['TotalPrice']>16
print("Valor Alto:*************************\n", df.ValorAlto.head(10))

print("separacion:*************************\n")

print("informacion1:*************************\n",df.info())

#convertir columnas
df.InvoiceDate=pd.to_datetime(df.InvoiceDate)
print("informacion2:*************************\n",df.info())

#no es necesario por que object es similar a string
df.Description=df.Description.astype('str')
print("informacion3:*************************\n",df.info())# por eso sigue botando object

#crear columna aplicando lambdas
df['Descuento']=df['TotalPrice'].apply(lambda x: x*.09)
print("Descuento:*************************\n", df.head(10))

#crear columna aplicando funciones usando appply
def categorias(price):
    if price>50:
        return 'alto'
    elif price<20:
        return 'bajo'
    else:
        return 'medio'

df['Categorias']=df['TotalPrice'].apply(categorias)
print("Categorias:*************************\n", df.head(10))

#filtrar datos ventas en reino unido y/ otro ejm France
ventasuk=df[df['Country']=='United Kingdom']
print("ventas reino unido:*************************\n", ventasuk)

#filtrar datos en una variable almacenamos solo las que cumplan la condicion
#en este caso todas las ventas mayores a 40 de la columna quantity
ventasaltaspais=df[df.Quantity > 40]
print("ventas mayor a N:*************************\n", ventasaltaspais)

#conbinacion de condiciones
ventasaltasuk=df[(df.Country =='United Kingdom') & (df.Quantity > 40)]
print("ventas reino unido:*************************\n", ventasaltasuk)

#filtracion por año
ventas2011=df[df.InvoiceDate.dt.year==2010]
print("ventas 2011:*************************\n", ventas2011)

#filtracion por año y por mes
ventasdiciembre2010=df[(df.InvoiceDate.dt.year==2010)&(df.InvoiceDate.dt.month==12)]
print("ventas diciembre 2010:*************************\n", ventasdiciembre2010)
