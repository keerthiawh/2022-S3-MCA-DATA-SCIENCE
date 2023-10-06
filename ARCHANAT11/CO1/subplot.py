import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2 * np.pi,100)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x,y_sin,label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('sin function')
plt.legend()
plt.grid()
plt.subplot(1,2,2)
plt.plot(x,y_cos,label='cos(x)',color='green')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('cos function')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
