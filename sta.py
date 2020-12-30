import numpy as np
from math import sqrt


def ave(x):
	#izračuna povprečje
	re = 0
	for i in x:
		re += i
	if len(x) == 0:
		return 0
	return re/len(x)

def linfit(x, y):
	#avtomatizira linearno fitanje, uporabiš le pri plot na druge mestu (plt.plot(x, linfit(x, y)(x)))
	fit = np.polyfit(x, y, 1, full = True)
	print('naklon premice in zač. vr.:', fit[0][0], fit[0][1])
	sq = sqrt(fit[1][0]/(len(x)-2))
	pov = ave(x)
	sx = 0
	for i in x:
		sx += (pov - i) ** 2
	sx = sqrt(sx)
	if sx != 0:
		sq /= sx
		print('abs. napaka naklona:', sq)
		print('rel. napaka naklona', sq/fit[0][0])
	else:
		print('povprečje x ravno 0!')
	fit = np.polyfit(x, y, 1)
	return np.poly1d(fit)

def lapp(x, y, t, n):
	#aprksimira poljubno krivuljo s premicami s poljubno točkami (n) in vrne vrednost v poljubni točki
	#deluje za sezname ki niso urejeni po velikosti (precej počas vrjetno)
	appv = []
	for _ in range(n):
		dis = 10**10
		disv = -1
		for i in range(len(x)):
			if i in appv:
				continue
			a = abs(x[i] - t)
			if a < dis :
				dis = a
				disv = i
		appv.append(disv)
	appp = [[],[]]
	for i in appv:
		appp[0].append(x[i])
		appp[1].append(y[i])
	fit = np.polyfit(appp[0], appp[1], 1)
	return np.poly1d(fit)(t)
