import pandas as pd, numpy, statistics
from sklearn import datasets
import matplotlib.pyplot as plt
boston=datasets.load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['Target'] = boston.target
y = df['Target']
for i in boston.feature_names:
    x = df[i]
    print(i)
    plt.scatter(x,y)
    df1 = pd.DataFrame(df[i],df['Target'])
    #print("median\t",numpy.median(df[i]))
    print("median\t",statistics.median (df[i].tolist()))
    print(df1.describe())
    plt.show()
print('INDUS vs NOX')
plt.scatter(df['INDUS'],df['NOX'])

plt.show()