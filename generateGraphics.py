import matplotlib.pyplot as plt
import time

nodesList = [2,3,4,5]
distanceList = [10,25, 100]

#for distance in distanceList:


mediaNodeList = []

for node in nodesList:
	rateLoss = []
	nrLostPacket = []
	mediaDelay = []
	mediaJitter = []
	for distance in distanceList:
		with open("OLSR_DATA_%s_%s.txt"%(node, distance), 'r') as dataFile:
			line = dataFile.readline()
			rateLoss.append(line.split(" ")[2])
			#print(rateLoss)
			nrLostPacket.append(line.split(" ")[3])
			#print(rateLoss)
			mediaDelay.append(float(line.split(" ")[4]))
	mediaNodeList.append(mediaDelay)

	
#plt.bar(distanceList, mediaDelay)
plt.plot(distanceList, mediaNodeList[0], 'r--', label='2 nós')
plt.plot(distanceList, mediaNodeList[1], 'g-', label='3 nós')
plt.plot(distanceList, mediaNodeList[2], 'y-', label='4 nós')
plt.plot(distanceList, mediaNodeList[3], 'b-', label='5 nós')
plt.legend(loc="upper left")
plt.xlabel("distância (m)")
plt.ylabel("número pacotes perdidos")
plt.savefig("OLSR2_rtt.png")
print("fez um")
time.sleep(2)
