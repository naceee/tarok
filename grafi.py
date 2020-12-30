from sta import *
import matplotlib.pyplot as plt
import csv

#vsebuje ničto igro
imena = ['blaz', 'gasper', 'jernej', 'klancar', 'nace', 'peter']
tocke = {'blaz': [0], 'gasper': [0], 'jernej': [0], 'klancar': [0], 'nace': [0], 'peter': [0]}
skupaj = {'blaz': [], 'gasper': [], 'jernej': [], 'klancar': [], 'nace': [], 'peter': []}
skupaj_odigrano = {'blaz': [], 'gasper': [], 'jernej': [], 'klancar': [], 'nace': [], 'peter': []}
igre = {'blaz': [], 'gasper': [], 'jernej': [], 'klancar': [], 'nace': [], 'peter': []}
igre_skupaj = {'blaz': [], 'gasper': [], 'jernej': [], 'klancar': [], 'nace': [], 'peter': []}
igre_skupaj_odigrano = {'blaz': [], 'gasper': [], 'jernej': [], 'klancar': [], 'nace': [], 'peter': []}
barve = {'blaz': 'b', 'gasper': 'forestgreen', 'jernej': 'rebeccapurple', 'klancar': 'k', 'nace': 'r', 'peter': 'gold'}
mesto_igralca = {'blaz': [0 for _ in range(4)], 'gasper': [0 for _ in range(4)], 'jernej': [0 for _ in range(4)], 'klancar': [0 for _ in range(4)], 'nace': [0 for _ in range(4)], 'peter': [0 for _ in range(4)]}

vse_igre = [0]
vse_igre_skupaj = []

# števila iger v eni partiji
with open('igre.txt', 'r') as f:
	reader = csv.reader(f, delimiter='	')
	for line in reader:
		vse_igre.append(float(line[0]))

#števila iger v partijah (kumulativno)
for i in range(len(vse_igre)):
	vse_igre_skupaj.append(sum(vse_igre[:i+1]))

#število točk v eni partiji
for i in tocke:
	with open(i+'.txt', 'r') as f:
		reader = csv.reader(f, delimiter='	')
		for line in reader:
			try:
				tocke[i].append(float(line[0]))
			except:
				tocke[i].append(0)

#število točk v partijah (kumulativno)
for i in tocke:
	for j in range(len(tocke[i])):
		skupaj[i].append(sum(tocke[i][:j+1]))

#število iger v posamezni partiji
for i in tocke:
	for j in range(len(tocke[i])):
		if tocke[i][j] != 0:
			igre[i].append(vse_igre[j])
		else:
			igre[i].append(0)

#število toč skozi partije (kumulativno)
for i in tocke:
	for j in range(len(tocke[i])):
		igre_skupaj[i].append(sum(igre[i][:j+1]))

#število točk skozi odigrane partije
for i in tocke:
	skupaj_odigrano[i].append(skupaj[i][0])
	for j in range(1, len(skupaj[i])):
		if skupaj[i][j] != skupaj[i][j-1]:
			skupaj_odigrano[i].append(skupaj[i][j])

#število iger skozi odigrane partije
for i in tocke:
	igre_skupaj_odigrano[i].append(igre_skupaj[i][0])
	for j in range(1, len(igre_skupaj[i])):
		if igre_skupaj[i][j] != igre_skupaj[i][j-1]:
			igre_skupaj_odigrano[i].append(igre_skupaj[i][j])

#poračunamo mesta, zaradi ničte igre se vsem odbije 1. mesto
nic = -100000
for i in range(1, len(tocke['blaz'])):
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

'''
#skupaj tocke
for i in tocke:
	plt.plot(vse_igre_skupaj, skupaj[i], '+-', color = barve[i], label=i)
plt.title('točke skozi vse igre')
plt.xlabel('vse igre')
plt.ylabel('točke')
plt.legend()
plt.show()

#fit od zgoraj
for i in tocke:
	b = round(np.polyfit(vse_igre_skupaj, skupaj[i], 1, full = True)[0][0], 2)
	plt.plot(vse_igre_skupaj, linfit(vse_igre_skupaj, skupaj[i])(vse_igre_skupaj), '-', color = barve[i])
	plt.plot(vse_igre_skupaj, skupaj[i], '+', color = barve[i], label = i+': '+str(b))
plt.title('točke skozi vse igre, linearni fit [št. točk/igra]')
plt.xlabel('vse igre')
plt.ylabel('točke')
plt.legend()
plt.show()

from scipy.interpolate import interp1d

xnew = np.linspace(0, vse_igre_skupaj[-1], num = vse_igre_skupaj[-1], endpoint= True)

#inerpolirano
for i in tocke:
	f2 = interp1d(vse_igre_skupaj, skupaj[i], kind = 'cubic')
	plt.plot(vse_igre_skupaj, skupaj[i], '+', label = i, color = barve[i])
	plt.plot(xnew, f2(xnew), '-', color = barve[i])
plt.title('točke skozi vse igre, kubična interpolacija')
plt.xlabel('vse igre')
plt.ylabel('točke')
plt.legend()
plt.show()

#tocke glede na odigrane igre
for i in tocke:
	print(igre_skupaj_odigrano[i], skupaj_odigrano[i])
	plt.plot(igre_skupaj_odigrano[i], skupaj_odigrano[i], '+-', color = barve[i], label=i)
plt.title('točke skozi odigrane igre')
plt.xlabel('odigrane igre')
plt.ylabel('točke')
plt.legend()
plt.show()

#fit od zgoraj
for i in tocke:
	b = round(np.polyfit(igre_skupaj_odigrano[i], skupaj_odigrano[i], 1, full = True)[0][0], 2)
	plt.plot(igre_skupaj_odigrano[i], linfit(igre_skupaj_odigrano[i], skupaj_odigrano[i])(igre_skupaj_odigrano[i]), '-', color = barve[i])
	plt.plot(igre_skupaj_odigrano[i], skupaj_odigrano[i], ' + ', color = barve[i], label = i+': '+str(b))
plt.title('točke skozi odigrane igre, linearni fit [št. točk/igra]')
plt.xlabel('odigrane igre')
plt.ylabel('točke')
plt.legend()
plt.show()

#interpolirano
for i in tocke:
	f2 = interp1d(igre_skupaj_odigrano[i], skupaj_odigrano[i], kind = 'cubic')
	plt.plot(igre_skupaj_odigrano[i], skupaj_odigrano[i], '+', label = i, color = barve[i])
	xnew = np.linspace(0, igre_skupaj_odigrano[i][-1], igre_skupaj_odigrano[i][-1], endpoint= True)
	plt.plot(xnew, f2(xnew), '-', color = barve[i])
plt.title('točke skozi odigrane igre, kubična interpolacija')
plt.xlabel('vse igre')
plt.ylabel('točke')
plt.legend()
plt.show()

#tocke v stoplcih
hist1 = []
imena = []

for i in tocke:
	hist1.append(skupaj[i][-1])
	imena.append(i)
plt.bar(imena, hist1)
plt.title('večna lestvica')
plt.ylabel('točke')
plt.show()

#mesta (prvo, drugo...) eno nad drugim
hist2_1 = []
hist2_2 = []
hist2_3 = []
hist2_4 = []
bottom_2 = []
bottom_3 = []
bottom_4 = []

for i in tocke:
	hist2_1.append(mesto_igralca[i][0])
	hist2_2.append(mesto_igralca[i][1])
	bottom_2.append(mesto_igralca[i][0])
	hist2_3.append(mesto_igralca[i][2])
	bottom_3.append(mesto_igralca[i][0] + mesto_igralca[i][1])
	hist2_4.append(mesto_igralca[i][3])
	bottom_4.append(mesto_igralca[i][0] + mesto_igralca[i][1] + mesto_igralca[i][2])
plt.bar(imena, hist2_1, color = 'gold', label = '1. mesto')
plt.bar(imena, hist2_2, bottom = bottom_2, color = 'silver', label = '2. mesto')
plt.bar(imena, hist2_3, bottom = bottom_3, color = 'peru', label = '3. mesto')
plt.bar(imena, hist2_4, bottom = bottom_4, color = 'k', label = '4. mesto')
plt.title('mesta')

plt.legend()
plt.show()

#eno ob drugem
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

fig, ax = plt.subplots()
ax.bar(ind - 3*width/2, hist2_1, width, color = 'gold', label = '1. mesto')
ax.bar(ind - width/2, hist2_2, width, color = 'silver', label = '2. mesto')
ax.bar(ind + width/2, hist2_3, width, color = 'peru', label = '3. mesto')
ax.bar(ind + 3*width/2, hist2_4, width, color = 'k', label = '4. mesto')
ax.set_xticklabels(['']+imena)
plt.title('mesta')
plt.legend(loc = 'upper center', bbox_to_anchor=(0.578, 1))
plt.show()

#obtežena mesta
hist2_1 = []
hist2_2 = []
hist2_3 = []
bottom_2 = []
bottom_3 = []

for i in tocke:
	hist2_1.append(mesto_igralca[i][0]*3)
	hist2_2.append(mesto_igralca[i][1]*2)
	bottom_2.append(mesto_igralca[i][0]*3)
	hist2_3.append(mesto_igralca[i][2])
	bottom_3.append(mesto_igralca[i][0]*3 + mesto_igralca[i][1]*2)
plt.bar(imena, hist2_1, color = 'gold', label = '1. x 3')
plt.bar(imena, hist2_2, bottom = bottom_2, color = 'silver', label = '2. x 2')
plt.bar(imena, hist2_3, bottom = bottom_3, color = 'peru', label = '3. x 1')
plt.title('obtežena mesta (neke vrste rating)')
plt.ylabel('rating')
plt.legend(loc = 'upper left')
plt.show()
'''