

inp=open('A-large-practice.in','r')
linp=inp.readlines()
linp=[el.rstrip('\n') for el in linp]

linp.remove(linp[0])
num=len(linp)
#print('test'+str(linp))

def countsheep(n,dig):
	a=[int(d) for d in str(n)]
	for x in a:
		if not x in dig:
			dig.append(x)

for i in range(num):
	digits=[]
	count=1
	#print("TEST :"+linp[i])
	if (int(linp[i]) != 0):
		while len(digits)<10:
			countsheep(count*int(linp[i]),digits)
			count += 1
		print("Case #"+str(i+1)+": "+str(int(linp[i])*(count-1)))
	else:
		print("Case #"+str(i+1)+": INSOMNIA")	
	 
