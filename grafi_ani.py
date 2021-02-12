import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grafi import *

fig, ax = plt.subplots()


y_max = 0
for i in imena:
	if skupaj[i][-1] > y_max:
		y_max = skupaj[i][-1]

def animate(n):
	print(n)
	ax.cla()
	for i in tocke:
		ax.plot(vse_igre_skupaj[:n], skupaj[i][:n], '+-', color = barve[i], label=i)
	ax.set_title('točke skozi vse igre')
	ax.set_xlabel('vse igre')
	ax.set_ylabel('točke')
	ax.set_xlim([-10, vse_igre_skupaj[-1]+10])
	ax.set_ylim([-200, y_max+200])
	ax.legend()


ani = animation.FuncAnimation(fig, animate, frames = len(vse_igre_skupaj), repeat = True, interval = 400)
plt.show()
ani.save('im.gif')


