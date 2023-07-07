t=int(input())
for z in range(t):
	a=input()
	b=a.split()
	l=[]
	for i in range(len(b)):
	   	c=int(b[i])
	   	l.append(c)
	p=1
	for j in l:
	   	p=j*p
	print(p)