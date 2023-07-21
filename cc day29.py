# cook your dish here
'''program to print 
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''
n=5
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	for j in range(i,n):
		print(" ",end=" ")
	for j in range(i,n):
		print(" ",end=" ")
	for j in range(i,0,-1):
			print(j,end=" ")
	print()
'''
program to print 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=5
z=1
for i in range(n+1):
	for j in range(1,i+1):
		print(z,end=" ")
		z+=1
	print()