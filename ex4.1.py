import matplotlib.pyplot as plt
import math as math
import numpy as np

def x(t, KF, C, wd, wn):
    return (KF*(1-math.e**(-C*wn*t)*(np.cos(wd*t)+C*(wn/wd)*np.sin(wd*t))))

t = np.arange(0.,3.,0.0001)
plt.plot(t, x(t,0.2667,0.2675,5.7994,6.0187), color='black')
plt.plot(t, 0.1388*math.e**(-1.61*t)*np.sin(5.7994*t))
plt.plot((0,3), (-0.04, -0.04), color='red')
plt.legend(("x(t)","x'(t)",'threshold'))
print(0.1388*math.e**(-1.61*0.78)*np.sin(5.7994*0.78))
plt.show()
