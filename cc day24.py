# cook your dish here
# subscription required or not 
t=int(input())
if(t>=1 and t<=100):
	for t in range(t):
		x=int(input())
		if(x>=1 and x<=100):
			if(x<=30):
				print("No")
			else:
				print("yes")