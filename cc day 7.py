'''Problem
There are 
N bikes and 
M cars on the road.
Each bike has 
2 tyres.
Each car has 
4 tyres.
Find the total number of tyres on the road.
Input Format:
The first line will contain 
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers
N,M.
Output Format:
For each test case, output in a single line, the total number of tyres on the road. '''
l=int(input())
for i in range(l):
	n,m=list((map(int, input().split())))
	d=n*2
	e=m*4
	f=d+e
	print(f)