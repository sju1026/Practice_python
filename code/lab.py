# lab 11 - 1
import matplotlib.pyplot as plt

x = [x for x in range(-10, 10)] 
y = [2*t for t in x]            
plt.plot(x, y, marker='o')      

plt.axis([-20, 20, -20, 20])
plt.show()

# lab 11 - 2
import math 
import matplotlib.pyplot as plt 
 
x = [] 
y = [] 
 
for angle in range(360): 
    x.append(angle) 
    y.append(math.sin(math.radians(angle))) 
 
plt.plot(x, y) 
plt.title("SINE WAVE") 
plt.show()

# lab 11 - 3
import numpy as np 
import matplotlib.pyplot as plt 
 
mu1, sigma1 = 10, 2
mu2, sigma2 = -6, 3

standard_Gauss = np.random.randn(10000)
Gauss1 = mu1 + sigma1 * np.random.randn(10000)
Gauss2 = mu2 + sigma2 * np.random.randn(10000) 

plt.figure(figsize=(10,6)) 
plt.hist(standard_Gauss, bins=50, alpha=0.4) 
plt.hist(Gauss1, bins=50, alpha=0.4)
plt.hist(Gauss2, bins=50, alpha=0.4)

plt.show()

# lab 11 - 4
import matplotlib.pyplot as plt 
import numpy as np 
 
np.random.seed(19680801) 
data = np.random.randn(2, 100) 
 
fig, axs = plt.subplots(2, 2, figsize=(5, 5)) 

axs[0, 0].hist(data[0]) 
axs[1, 0].scatter(data[0], data[1]) 
axs[0, 1].plot(data[0], data[1]) 
axs[1, 1].hist2d(data[0], data[1]) 
 
plt.show()