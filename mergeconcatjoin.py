import pandas as pd

path='online_retail.csv'
df=pd.read_csv(path)
#print(type(rd))
print("1:*************************\n",df.head(10))#muestra las primeras 5 filas o las filas que le indiquemos

#nueva tabla en base a valores indice columnas y una funcion de sumatoria
pivot001=pd.pivot_table(df,values='Quantity', index='Country', columns='StockCode',aggfunc='sum')
print("table pivote:*************************\n", pivot001)

#nueva tabla en base a valores indice varias columnas y una funcion de media
pivot002=pd.pivot_table(df,values='Quantity', index='Country', columns=['StockCode','UnitPrice'],aggfunc='mean')
print("table pivote002:*************************\n", pivot002)

df2 = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': [1, 2, 3],
    'C': [4, 5, 6]
})
print("df2:*************************\n",df2)

#apilado o moviendo indices 
dfs=df2.stack()
print("stack:*************************\n",dfs)

#apilado o moviendo indices 
dfsatras=dfs.unstack()
print("unstack:*************************\n",dfsatras)