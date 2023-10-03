#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np


# In[29]:


import pandas as pd


# In[30]:


from sklearn.datasets import make_blobs


# In[31]:


import matplotlib.pyplot as plt


# In[37]:


# Number of data points
n_samples = 100


# In[38]:


# Number of features (2D data for easy visualization)
n_features = 2 


# In[39]:


# Number of blobs or clusters
n_clusters = 3


# In[53]:


# Create blobs
X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters,cluster_std =5,shuffle =True, random_state=2,)


# In[54]:


# Visualize the blobs
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Generated Blobs')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


# In[ ]:




