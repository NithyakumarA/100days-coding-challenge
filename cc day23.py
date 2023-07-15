# cook your dish here
# 2nd max value in list 
n=int(input())
if(n>=1 and n<=6):
	for i in range(n):
		a=list(map(int,input().split()))
		b=a.remove(max(a))
		c=max(a)
		print(c)