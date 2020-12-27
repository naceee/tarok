fileigre = open("igre.txt", "r")

fileigralci = []
igre = []
tocke =  []

igralci = ["peter", "nace", "blaz", "gasper", "jernej", "klancar"]
for i in range(len(igralci)):
	tocke.append([])
	fileigralci.append(open(igralci[i] + ".txt", "r"))

  
while True: 
	line = fileigre.readline()
	#print(line)
	if not line:
		break
	else:
		igre.append(int(line))
		for i in range(len(igralci)):
			#print(igralci[i])
			t = fileigralci[i].readline()
			if t != "\n":
				tocke[i].append(int(t))
			else:
				tocke[i].append(0)	



print("stevilo iger")
print(igre)
for i in range(len(igralci)):
	print(igralci[i])
	print(tocke[i])
