import pandas as pd
da={'mpg':[10,20,45,31,61,],
    'cylinder':[8,6,3,3,8],
    'displacement':[307,350,111,222,332],
    'horsepower':[130,615,271,999,725],
    'weight':[3504,4500,5231,777,761],
    'accelaration':[2005,751,666,122,781],
    'origin':[1,1,2,1,1],
    'modelyear':[70,80,81,91,61],
    'brand':["tata","mahindra","mg","vw","toyota"]}
df=pd.DataFrame(da)
pp=df.describe()
print("this is statistical details of \n",pp)
pv=df[df["cylinder"]==8]
print(df.groupby('modelyear')['brand'].count())
