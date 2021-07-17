import numpy as np
import matplotlib.pyplot as plt
import keyboard as kb
class Sines():
    values = []
    def addSine(self, angle):
        self.values.append(angle)
        self.t = angle*0.0174533
        X = np.linspace(-10*np.pi, 2*np.pi, 256)
        Y = np.linspace(0+self.t, 2*np.pi+self.t, 256)
        S = np.sin(Y)
        plt.plot(X, S, label=r'$\phi=$'+str(angle)+r'$^\circ$')
        plt.legend(loc="upper right")
    

    def show(self):
        plt.xticks([ 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi ],[r'$0.0\pi$', r'$0.25\pi$', r'$0.5\pi$', r'$0.75\pi$', r'$1.0\pi$', r'$1.25\pi$', r'$1.5\pi$', r'$1.75\pi$', r'$2.0\pi$' ])
        plt.yticks([-2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0],[r'$-2.0$', r'$-1.5$', r'$-1.0$', r'$-0.5$', r'$0.0$', r'$0.5$', '$1.0$', r'$1.5$', r'$2.0$'])   #plt.ylim(-2,2)
        plt.title('Interactive sinusoidal functions')
        plt.xlabel(r'$\theta$')
        plt.ylabel(r'$sin(\theta+\phi)$')
        plt.grid(True, linestyle='--',  which='both')
        plt.axhline(y=0, color='k')
        plt.axhline(y=1, color='g')
        plt.text( np.pi, 1.1, 'Maximum value')
        plt.axhline(y=-1, color='r')
        plt.text( np.pi, -1.2, 'Minimum value')
        plt.show()

    def shiftRight(self, angle):
        plt.clf()
        for i in range(len(self.values)):
            self.values[i] += -angle
        for _ in self.values:
            self.t = (_)*0.0174533
            X = np.linspace(0, 2*np.pi, 256)
            Y = np.linspace(0+self.t, 2*np.pi+self.t, 256)
            S = np.sin(Y)
            plt.plot(X, S, label=r'$\phi=$'+str(_)+r'$^\circ$')
            plt.legend(loc="upper right")
    
    def shiftLeft(self, angle):
        plt.clf()
        for i in range(len(self.values)):
            self.values[i] += angle
        for _ in self.values:
            self.t = (_)*0.0174533
            X = np.linspace(0, 2*np.pi, 256)
            Y = np.linspace(0+self.t, 2*np.pi+self.t, 256)
            S = np.sin(Y)
            plt.plot(X, S, label=r'$\phi=$'+str(_)+r'$^\circ$')
            plt.legend(loc="upper right")
    
    def interact(self):
        pass

s = Sines()
s.addSine(0)
s.addSine(90)
s.show()
