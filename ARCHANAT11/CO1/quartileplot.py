#quartileplot
import matplotlib.pyplot as plt
import numpy as np
data =np.random.normal(30,1,500)
plt.boxplot(data)
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()
