import pandas as pd

path='online_retail.csv'
df=pd.read_csv(path)
#print(type(rd))
#print("1:*************************\n",df.head(10))#muestra las primeras 5 filas o las filas que le indiquemos

df2 = pd.DataFrame({
    'key': ['a', 'b', 'c'],
    'value1': [1, 2, 3],
})
df3 = pd.DataFrame({
    'key': ['b', 'c', 'd'],
    'value2': [4, 5, 6],
})

print("df2:*************************\n",df2)
print("df3:*************************\n",df3)

inerjoin=pd.merge(df2,df3,on='key',how='inner')
print("inner join:*************************\n",inerjoin)

outerjoin=pd.merge(df2,df3,on='key',how='outer')
print(" outer join:*************************\n",outerjoin)

leftjoin=pd.merge(df2,df3,on='key',how='left')
print("left join:*************************\n",leftjoin)

rightjoin=pd.merge(df2,df3,on='key',how='right')
print("right join:*************************\n",rightjoin)


df5 = pd.DataFrame({
    'A': ['a0', 'a1', 'a2'],
    'B': ['b0', 'b1', 'b2'],
})

df6 = pd.DataFrame({
    'A': ['a3', 'a4', 'a5'],
    'B': ['b3', 'b4', 'b5'],
})
print("df5:*************************\n",df5)
print("df6:*************************\n",df6)


concatenervertical=pd.concat([df5,df6])
print("concatenacion vertical:*************************\n",concatenervertical)

concatenhorizontal=pd.concat([df5,df6], axis=1) #axis= 1 es por eje x axis 0 es eje Y o por defecto apilacion vertical
print("concatenacion horizonal:*************************\n",concatenhorizontal)

#cambiando el valor de los indices
df7 = pd.DataFrame({
    'A': ['a0', 'a1', 'a2'],
    'B': ['b0', 'b1', 'b2'],
}, index=['k0','k1','k2'])

df8 = pd.DataFrame({
    'C': ['c3', 'c4', 'c5'],
    'D': ['d3', 'd4', 'd5'],
}, index=['k0','k2','k3'])

print("df7:*************************\n",df7)
print("df8:*************************\n",df8)

joined001=df7.join(df8, how='inner')
print("join con otro index:*************************\n",joined001)