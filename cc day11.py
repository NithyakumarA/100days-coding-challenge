# cook your dish here
'''Problem
You know that 
1 kg of pulp can be used to makes
1000 pages and 
1 notebook consists of 
100 pages.
Suppose a notebook factory receives 
N kg of pulp, how many notebooks can be made from that?
Input Format
First line will contain 
T, the number of test cases. Then the test cases follow.
Each test case contains a single integer 
N - the weight of the pulp the factory has (in kgs).
Output Format
For each test case, output the number of notebooks that can be made using
N kgs of pulp.'''
l=int(input())
for i in range(l):
	c=int(input())
	e=(c*1000)//100
	print(e)