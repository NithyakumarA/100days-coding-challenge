# cook your dish here
'''
Problem:
Chef has infinite coins in denominations of rupees 
5 and rupees 
10.
Find the minimum number of coins Chef needs, to pay exactly 
X rupees. If it is impossible to pay 
X rupees in denominations of rupees 
5 and 
10 only, print
−1.
Input Format:
First line will contain 
T, number of test cases. Then the test cases follow.
Each test case contains of a single integer 
X.
Output Format:
For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly 
X rupees. If it is impossible to pay 
X rupees in denominations of rupees 
5 and 
10 only, print 
−1.
Constraints:
1≤T≤1000
1≤X≤1000
'''
t=int(input())
if(t>=1 and t<=1000):
	for t in range(t):
		x=int(input())
		if(x%5==0 or x%10==0):
			if(x==5 or x==10):
				print("1")
			else:
				c=x%10
				if(c==0):
					d=x//10
					print(d)
				else:
					e=1+(x//10)
					print(e)
		else:
			print("-1")		