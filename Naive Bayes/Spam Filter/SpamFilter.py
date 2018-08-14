
# coding: utf-8

# In[252]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score


# In[253]:


# read the data and replace null values with a null string
df1 = pd.read_csv("C:\\Users\\user\\Downloads\\Spam-mail-filtering-master\\Spam-mail-filtering-master\\spamham.csv")
df = df1.where((pd.notnull(df1)), '')


# In[254]:



dfa = pd.read_csv("C:\\Users\\user\\Downloads\\Spam-mail-filtering-master\\Spam-mail-filtering-master\\a.csv")
#print(dfa)
'''input_email = dfa['Message']
input_email = input_email.where((pd.notnull(input_email)), '')
'''
input_email=[input("Enter Input:")]
#print(input_email)


# In[255]:


# Categorize Spam as 0 and Not spam as 1 
df.loc[df["Category"] == 'ham', "Category",] = 1
df.loc[df["Category"] == 'spam', "Category",] = 0
# split data as label and text . System should be capable of predicting the label based on the  text
df_x = df['Message']
df_y = df['Category']
# split the table - 80 percent for training and 20 percent for test size
x_train = df1['Message']
y_train = df1['Category']



# In[256]:


# feature extraction, coversion to lower case and removal of stop words using TFIDF VECTORIZER
tfvec = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
x_trainFeat = tfvec.fit_transform(x_train)

x_testFeat = tfvec.transform(input_email)

#x_testFeat = tfvec.transform(input_email)
#print("~~~~~~~~~~~~~~~~\n\n\n",type(x_test[0]))


#print(x_test)


# In[257]:


# GNB is used to model
y_trainGnb = y_train.astype('int')
classifierModel2 = MultinomialNB()
classifierModel2.fit(x_trainFeat, y_trainGnb)
predResult2 = classifierModel2.predict(x_testFeat)

print("Predicted value:","Spam" if predResult2 == [0] else "Ham")




# In[258]:


# Calc accuracy,converting to int - solves - cant handle mix of unknown and binary

