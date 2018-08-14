
# coding: utf-8

# In[267]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics, datasets, linear_model


# In[268]:


data = datasets.load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)
len(df)


# In[269]:


y = pd.DataFrame(data.target, columns=['MEDV'])

X = df[['RM', 'PTRATIO', 'LSTAT']]
#y = target['MEDV']


# In[270]:


X.head()


# In[271]:


kf = KFold(n_splits = 3, shuffle = True, random_state = 2)
result = next(kf.split(X), None)


# In[272]:


len(result) ##result[0] contains the training data and result[1] contains the test data


# In[273]:


train_X, train_y = X.iloc[result[0]], y.iloc[result[0]]
test_X, test_y =  X.iloc[result[1]], y.iloc[result[1]]


# In[274]:


len(train_X)


# In[275]:


len(test_y)


# In[276]:


train_X.head()


# In[277]:


test_X.head()


# In[278]:


train_y.head()


# In[279]:


test_y.head()


# In[280]:


lm = linear_model.LinearRegression()

model = lm.fit(X_train, y_train)


# In[281]:


predictions = cross_val_predict(model, test_X, test_y, cv=3)

predictions[0:5]


# In[282]:


plt.scatter(test_y[0:5], predictions[0:5])
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()


# In[283]:


plt.scatter(test_y, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()

