import os, matplotlib.pyplot as plt, time



distanceList = [10, 30, 40, 50, 70]
listNode = []
listRTTNode = []
x = [5, 5, 5, 5, 5]
y = [1.5, 1.5, 30.56, 68.5, 68.5]
z = [2, 4.5, 27.5, 69.5, 69.5]
w = [0.7, 30.67, 73.5, 284.2, 328.5]

plt.plot(distanceList, x, 'r--', label='2 nós')
plt.plot(distanceList, y, 'g-', label='5 nós')
plt.plot(distanceList, z, 'y-', label='10 nós')
plt.plot(distanceList, w, 'r-', label='15 nós')
plt.legend(loc="upper left")
plt.xlabel("distância (m)")
plt.ylabel("RTT (ms)")
plt.show()
plt.savefig("AODV_GAUSS.png")