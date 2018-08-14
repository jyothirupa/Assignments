
# coding: utf-8

# In[60]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score


# In[61]:


iris = pd.read_csv('C:\\Users\\user\\.spyder-py3\\iris.csv')
iris.head()


# In[62]:


## map each iris species to a number with a dictionary and list comprehension.
iris_class = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
iris['species_num'] = [iris_class[i] for i in iris.Species]


# In[63]:


iris.head()


# In[64]:


## Create an 'X' matrix by dropping the irrelevant columns.
X = iris.drop(['Species', 'species_num'], axis=1)
y = iris.species_num


# In[65]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


# In[66]:


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)


# In[67]:


pred_y = knn.predict(X_test)
r2_score(y_test, pred_y)

