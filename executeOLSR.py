import os, matplotlib.pyplot as plt, time




distanceList = [5, 25, 75, 100]
listNode = []
listRTTNode = []

for node in range(2, 6):
	rateLoss = []
	rttMedia = []
	listDistance = []
	for distance in distanceList: 
		f = os.popen("./waf --pyrun 'src/flow-monitor/examples/wifi-olsr-flowmon.py --NumNodesSide=%s --DISTANCE=%s'"%(node, distance))
	time.sleep(5)		
"""
		test = f.read().split("% packet loss") 
		rateLoss.append(float(test[0].split("received, ")[1])/100)
		#print(test[1].split("rtt min/avg/max/mdev = "))
		if(len(test[1].split("rtt min/avg/max/mdev = ")) > 1):
			rtt = test[1].split("rtt min/avg/max/mdev = ")[1]
			rttMedia.append(float(rtt.split("/")[1]))
			listDistance.append(distance)
	listRTTNode.append(rttMedia)
	listNode.append(node)

	print(rttMedia)

plt.plot(listDistance, listRTTNode[0], 'r--', label='2 nós')
plt.plot(listDistance, listRTTNode[3], 'g-', label='5 nós')
plt.plot(listDistance, listRTTNode[8], 'y-', label='10 nós')
plt.plot(listDistance, listRTTNode[13], 'r-', label='15 nós')
plt.plot(listDistance, listRTTNode[-1], 'b-', label='20 nós')
plt.legend(loc="upper left")
plt.xlabel("distância (m)")
plt.ylabel("RTT (ms)")
plt.savefig("AODV_RTT.png")
"""