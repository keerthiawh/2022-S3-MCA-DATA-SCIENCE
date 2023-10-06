#sincosdiagram
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y, linestyle='dotted',color='red')
x=np.arange(0,4*np.pi,0.1)
z=np.cos(x)
plt.plot(x,z, linestyle='solid',color='green')
plt.title('data')
plt.xlabel("pi value")
plt.ylabel("sinx, cosx")
plt.legend(['sin(x)','cos(x)'])
plt.show()
     
