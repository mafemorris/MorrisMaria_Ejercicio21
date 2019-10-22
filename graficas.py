from numpy import *
from matplotlib.pylab import *

t=linspace(0,2*pi,100)
seno = lambda t: sin(t)

plot(seno(t))
savefig('sin.png')