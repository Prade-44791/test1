import pandas as pd
from matplotlib import pyplot as pa
import seaborn as s

tm=pd.read_csv("C:/Users/prade/Desktop/PYTHON FILES/AUTOMPG.csv")
#histogram
pa.hist(tm['mpg'], color='green', label='mpg')
pa.xlabel('mpg')
pa.ylabel('Frequency')
pa.title('Frequency distribution')
pa.show()

#scatter
c=['red','blue']
pa.scatter(tm['weight'], tm['mpg'],label="Weight and mpg",color='black')
pa.xlabel('weight')
pa.ylabel("Size of the car")
pa.title("Scatter plot of given data")
pa.show()

#bar graph
ca=tm['am'].value_counts()
pa.bar(ca.index,ca.values,color='r',width=1)
pa.xticks([0,1],['0-Automatic','1-Manual'])
pa.xlabel("Tranmisson Type")
pa.ylabel("No of Cars")
pa.title("Frequency distribution of transmission type of cars")
pa.show()

#box graph
pa.boxplot(tm['mpg'])
pa.xlabel("MPG")
pa.ylabel("Values")
pa.title("BOX plot of MPG Vlues")
pa.show()



