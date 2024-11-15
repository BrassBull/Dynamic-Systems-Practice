import matplotlib.pyplot as plt
import math as math
import numpy as np

def y(t, ka, tau):
    return (ka*(1-math.e**(-t/tau)))
t = np.arange(0.,50.,0.2)
tau = 5000*0.01375/(50+1/0.025)
ka = (50*180+60/0.025)/(50+1/0.025)
plt.plot(t, 60*math.e**(-t/tau) + ka*(1-math.e**(-t/tau)), color='black')

plt.show()