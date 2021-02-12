import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grafi import *

fig, ax = plt.subplots()

nic = -100000

y_max = 0
for k in imena:
	if y_max < len(skupaj_odigrano[k]):
		y_max = len(skupaj_odigrano[k])

def animate(i):
	if i == 0:
		for k in mesto_igralca:
			mesto_igralca[k] = [-1]+[0 for _ in range(3)]
	ax.cla()
	rez_igre = []
	mesta = []
	for j in imena:
		if tocke[j][i] != 0:
			rez_igre.append(tocke[j][i])
		else:
			rez_igre.append(nic)
		mesta.append(0)
	mest = 4
	while mest > 0:
		m = max(rez_igre)
		count = 0
		for k in range(len(rez_igre)):
			if rez_igre[k] == m:
				rez_igre[k] = nic
				mesta[k] = mest
				count += 1
		mest -= count
	for j in range(4):
		for k in range(len(mesta)):
			if mesta[k] == 4-j:
				mesto_igralca[imena[k]][j] += 1

	hist2_1 = []
	hist2_2 = []
	hist2_3 = []
	hist2_4 = []

	for i in tocke:
		hist2_1.append(mesto_igralca[i][0])
		hist2_2.append(mesto_igralca[i][1])
		hist2_3.append(mesto_igralca[i][2])
		hist2_4.append(mesto_igralca[i][3])

	ind = np.arange(len(hist2_1))  # the x locations for the groups
	width = 0.2  # the width of the bars

	ax.bar(ind - 3*width/2, hist2_1, width, color = 'gold', label = '1. mesto')
	ax.bar(ind - width/2, hist2_2, width, color = 'silver', label = '2. mesto')
	ax.bar(ind + width/2, hist2_3, width, color = 'peru', label = '3. mesto')
	ax.bar(ind + 3*width/2, hist2_4, width, color = 'k', label = '4. mesto')
	ax.set_xticklabels(['']+imena)
	ax.set_title('mesta')
	ax.legend(loc = 'upper center', bbox_to_anchor=(0.578, 1))



ani = animation.FuncAnimation(fig, animate, frames = len(tocke['blaz']), repeat = True, repeat_delay = 1400, interval = 400)
ani.save('im_mesta_en_stolpec.gif')
plt.show()