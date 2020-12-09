fileigre = open("igre.txt", "r")
fileigralci = []
fileigralci.append(open("peter.txt", "r"))
fileigralci.append(open("nace.txt", "r"))
fileigralci.append(open("blaz.txt", "r"))
fileigralci.append(open("gasper.txt", "r"))
fileigralci.append(open("jernej.txt", "r"))
fileigralci.append(open("klancar.txt", "r"))

igre = []
igralci = ["peter", "nace", "blaz", "gasper", "jernej", "klancar"]
tocke =  []
for i in range(len(igralci)):
	tocke.append([])

print(tocke)
  
while True: 
	line = fileigre.readline()
	print("---->", line)
	if not line:
		break
	else:
		igre.append(int(line))
		for i in range(len(igralci)):
			t = fileigralci[i].readline()
			print(t)
			if t != "\n":
				tocke[i].append(int(t))
			else:
				tocke[i].append(0)				


for i in range(len(igralci)):
	print(igralci[i])
	print(tocke[i])

