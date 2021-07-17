import numpy as np
import matplotlib.pyplot as plt
t = 0
X = np.linspace(0+t, 2*np.pi+t, 256)
S = np.sin(X)
plt.plot(X, S)
plt.xticks([ 0+t, np.pi/4+t, np.pi/2+t, 3*np.pi/4+t, np.pi+t, 5*np.pi/4+t, 3*np.pi/2+t, 7*np.pi/4+t, 2*np.pi+t ],[r'$0.0\pi$', r'$0.25\pi$', r'$0.5\pi$', r'$0.75\pi$', r'$1.0\pi$', r'$1.25\pi$', r'$1.5\pi$', r'$1.75\pi$', r'$2.0\pi$' ])
plt.ylim(-2,2)
t = np.pi/2
X = np.linspace(0, 2*np.pi, 256)
Y = np.linspace(0+t, 2*np.pi+t, 256)
S = np.sin(Y)
plt.plot(X, S)
plt.title('Interactive sinusoidal functions')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$sin(\theta+\phi)$')
plt.grid(True, linestyle='--',  which='both')
plt.axhline(y=0, color='k')
plt.axhline(y=1, color='g')
plt.text( np.pi+t, 1.1, 'Maximum value')
plt.axhline(y=-1, color='r')
plt.text( np.pi/4+t, -1.2, 'Minimum value')
plt.show()
