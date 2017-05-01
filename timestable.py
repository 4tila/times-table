from matplotlib import pyplot as plt
import numpy as np
polynomial = '5*x'
ran = np.arange(-np.pi, np.pi, 0.01)
x = np.cos(ran)
y = np.sin(ran)
plt.plot(x,y)
divs = 257
r = float(len(ran))/float(divs)
ring = list()
for i in range(divs):
    p = int(round(i*r))
    plt.scatter(x[p], y[p])
    ring.append([x[p], y[p]])
for i in range(divs):
    plt.plot([ring[i][0],ring[eval(polynomial.replace('x', str(i)))%divs][0]],
             [ring[i][1],ring[eval(polynomial.replace('x', str(i)))%divs][1]],
                color='blue')
plt.show()
while True:
    polynomial = raw_input('>:')
    plt.plot(x,y)
    for i in range(divs):
        p=int(round(i*r))
        plt.scatter(x[p], y[p])
    for i in range(divs):
        plt.plot([ring[i][0],ring[eval(polynomial.replace('x', str(i)))%divs][0]],
             [ring[i][1],ring[eval(polynomial.replace('x', str(i)))%divs][1]],
                color='blue')
    plt.show()
