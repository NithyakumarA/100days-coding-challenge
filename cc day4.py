# cook your dish here
'''
problem statement:
Chef has a bucket having a capacity of 
K liters. It is already filled with 
X liters of water.
find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.
input format:
The first line will contain 
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers K and 
X - as mentioned in the problem.
Output Format:
For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.'''
t=int(input())
for i in range(t):
	a=input()
	b=a.split()
	l=[]
	for i in range(len(b)):
		c=int(b[i])
		l.append(c)
	j=0
	d=l[j]-l[j+1]
	print(d)