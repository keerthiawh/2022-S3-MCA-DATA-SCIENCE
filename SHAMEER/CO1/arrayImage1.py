#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from PIL import Image
from scipy import ndimage
from matplotlib import pyplot as plt
a=Image.open('mkh.jpg')
plt.imshow(a)
b=np.array(a)
x=ndimage.rotate(b,180)
d=Image.fromarray(x)
plt.imshow(d)


# In[10]:


y=ndimage.zoom(b,(.25,.25,1))
w=Image.fromarray(y)
plt.imshow(w)


# In[3]:


import numpy as np
from PIL import Image
from scipy import ndimage
from matplotlib import pyplot as plt
a=Image.open('mkh.jpg')
plt.imshow(a)


# In[ ]:




