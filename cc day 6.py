# cook your dish here
'''Problem
Eikooc loves bread. She has
N loaves of bread, all of which expires after exactly M days. She can eat upto K loaves of bread in a day. Can she eat all the loaves of bread before they expire?

Input Format:
The first line contains a single integer 
T - the number of test cases. Then the test cases follow.
Each test case consists of a single line containing three integers N,
M and 
K - the number of loaves of bread Eikooc has, the number of days after which all the breads will expire and the number of loaves of bread Eikooc can eat in a day.
Output Format:
For each test case, output Yes if it will be possible for Eikooc to eat all the loaves of bread before they expire. Otherwise output No.

You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).'''
l=int(input())
for i in range(l):
	n,m,k=list((map(int, input().split())))
	c=n/m
	if(k>=c):
		print("yes")
	else:
		print("No")