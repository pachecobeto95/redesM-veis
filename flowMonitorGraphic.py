import os, matplotlib.pyplot as plt, time
from xml.dom.minidom import parse, parseString
import math

distanceList = [10, 20, 30, 70, 100]
listNodeDelay = []
listNoderatioLostPacket = []

for node in range(2, 6):
	fileDelay = []
	fileratioLostPacket = []
	for distance in distanceList:
		dom1 = parse("OLSRGAUSSMARKOV%s_%s"%(node,distance))
		flow = dom1.getElementsByTagName('Flow')
		ratioLostPacket = []
		delayMedia = []
		for elem in flow:
			txPackets = elem.attributes['flowId'].value
			attributesDict = dict(elem.attributes.items())
			if('txPackets' in attributesDict.keys()):
				txPackets = float(attributesDict['txPackets'])
				lostPackets = float(attributesDict['lostPackets'])
				if(txPackets != 0):
					ratioLostPacket.append(lostPackets/txPackets)
				
				delayNb = float(attributesDict['delaySum'].split("+")[1].split("ns")[0])
				if(delayNb is not None):
					test = txPackets - lostPackets
					delayTemp = delayNb/test
					delayMedia.append(delayTemp)

		fileratioLostPacket.append(sum(ratioLostPacket)/len(ratioLostPacket))
		fileDelay.append(sum(delayMedia)/len(delayMedia))

	listNoderatioLostPacket.append(fileratioLostPacket)
	listNodeDelay.append(fileDelay)

plt.plot(distanceList, listNoderatioLostPacket[0], 'r--', label=u'2 nós')
plt.plot(distanceList, listNoderatioLostPacket[1], 'g-', label=u'3 nós')
plt.plot(distanceList, listNoderatioLostPacket[2], 'y-', label=u'4 nós')
plt.plot(distanceList, listNoderatioLostPacket[3], 'b-', label=u'5 nós')
plt.legend(loc="upper left")
plt.xlabel(u"distância (m)")
plt.ylabel(u"Taxa de Perda de Pacotes")
plt.savefig("OlsrGAUSSRatioLostPacket.png")
plt.show()
time.sleep(2)

print(len(listNodeDelay))
plt.plot(distanceList, listNodeDelay[0], 'r--', label='2 nós')
plt.plot(distanceList, listNodeDelay[1], 'g-', label='3 nós')
plt.plot(distanceList, listNodeDelay[2], 'y-', label='4 nós')
plt.plot(distanceList, listNodeDelay[3], 'b-', label='5 nós')
plt.legend(loc="upper left")
plt.xlabel("Distância (m)")
plt.ylabel("Atraso (ns)")
plt.savefig("OlsrGAUSSDelay.png")
plt.show()
time.sleep(2)
