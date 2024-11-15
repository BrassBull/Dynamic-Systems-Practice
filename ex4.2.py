import matplotlib.pyplot as plt
import math as math
import numpy as np

def c2(t, Kc, tau1, tau2):
    return (Kc*(1+(tau2*math.e**(-t/tau2) - tau1*math.e**(-t/tau1))/(tau1-tau2)))
def c1(t, Kc, tau1, tau2):
    return(1.5*Kc*(-math.e**(-t/tau2)+math.e**(-t/tau1))/(tau1-tau2) + c2(t, Kc, tau1, tau2))
t = np.arange(0.,25.,0.001)
plt.plot(t, c2(t,0.25,0.8787,5.1213), color='black')
plt.plot(t, c1(t,0.25,0.8787,5.1213), color='blue')
plt.plot((0,25), (0.25, 0.25), color='red')
plt.legend(("c2(t)",'c1(t)','threshold'))
plt.show()
plt.close()
plt.plot(t, (c1(t,0.25,0.8787,5.1213)-c2(t,0.25,0.8787,5.1213))*2/3, color='black')
plt.plot(t, (c1(t,0.25,0.8787,5.1213)-c2(t,0.25,0.8787,5.1213))*2/3 + 1.5*0.25*(math.e**(-t/5.1213)/5.1213+math.e**(-t/0.8787)/0.8787)/(0.8787-5.1213), color='blue')
plt.show()
plt.close()
