'''program to print
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n=5
for i in range(n-1):
	for j in range(i+1):
		print("*",end=" ")
	print()
for k in range(n):
	for l in range(k,n):
		print("*",end=" ")
	print()
'''program to print
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''
#User function Template for python3

n=int(input())

for i in range(1,n+1):
	if i%2==0:
		for j in range(1,i+1):
			if(j%2==0):
				print("1",end=" ")
			else:
				print("0",end=" ")
		print()
	else:
		for j in range(1,i+1):
			if(j%2!=0):
				print("1",end=" ")
			else:
				print("0",end=" ")
		print()