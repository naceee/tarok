import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grafi import *

fig, ax = plt.subplots()


y_max = 0
for i in imena:
	if skupaj[i][-1] > y_max:
		y_max = skupaj_odigrano[i][-1]

def animate(n):
	ax.cla()

	hist1 = []
	imena = []
	barve_stolpcev = []
	vrstni_red = []
	for _ in range(len(tocke)):
		max_v = -100000
		max_m = ''
		for i in tocke:
			if i not in vrstni_red:
				if len(skupaj[i]) > n:
					if skupaj[i][n] > max_v:
						max_v = skupaj[i][n]
						max_m = i
				else:
					if skupaj[i][-1] > max_v:
						max_v = skupaj[i][-1]
						max_m = i
		vrstni_red.append(max_m)
	print(vrstni_red)

	for i in vrstni_red:
		if len(skupaj[i]) > n:
			hist1.append(skupaj[i][n])
		else:
			hist1.append(skupaj[i][-1])
		barve_stolpcev.append(barve[i])
	ax.bar(vrstni_red, hist1, color = barve_stolpcev)
	ax.set_title('število iger:'+str(round(vse_igre_skupaj[n])))
	ax.set_ylabel('točke')
	ax.set_ylim([0, y_max+1000])



ani = animation.FuncAnimation(fig, animate, frames = len(vse_igre_skupaj), repeat = True, repeat_delay = 1400,interval = 400)
ani.save('im_vecna_napredno.gif')
plt.show()