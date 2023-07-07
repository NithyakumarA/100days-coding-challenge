# cook your dish here
'''Problem
Chef wants to gift 
C chocolates to Botswal on his birthday. However, he has only 
X chocolates with him.
The cost of 
1 chocolate is 
Y rupees.
Find the minimum money in rupees Chef needs to spend so that he can gift 
C chocolates to Botswal.
Input Format
First line will contain 
T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, three integers
C,X, and 
Y.
Output Format:
For each test case, output in a single line answer, the minimum money in rupees Chef needs to spend.'''
l=int(input())
for i in range(l):
	c,x,y=  list(map(int, input().split()))
	d=c-x
	e=d*y
	print(e)