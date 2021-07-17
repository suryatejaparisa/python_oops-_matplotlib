import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 5000
avg = []
for _ in range(2,n):
    r = np.random.randint(1,7,_) #generates sample space of event throwing the unbiased die
    avg.append(np.average(r))
def clt(current):
    plt.cla()
    if current == 5000: 
        a.event_source.stop() #stops when animation in last frame

    plt.hist(avg[0:current]) #plots histogram
    plt.gca().set_title('standard normal distribution')
    plt.gca().set_xlabel('Average of die rolls')
    plt.gca().set_ylabel('Frequency')

fig = plt.figure()
anim = animation.FuncAnimation(fig, clt, interval=1)
anim.save('./clt.gif', writer='imagemagick', fps=10)#generates gif using Funcanimation
