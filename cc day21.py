# cook your dish here
''' 
In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary.
If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.
NOTE: Gross Salary = Basic Salary + HRA + DA
Input:
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer salary.
Output:
For each test case, output the gross salary of the employee in a new line. Your answer will be considered correct if the absolute error is less than 10-2.
Constraints:
1 ≤ T ≤ 1000
1 ≤ salary ≤ 100000
'''
t=int(input())
if(t>=1 and t<=1000):
	for t in range(t):
		x=int(input())
		if(x>=1 and x<=100000):
			if(x<1500):
				HRA=(10/100)*x
				DA=(90/100)*x
				Gross=x+HRA+DA
				print(Gross)
			if(x>=1500):
				HRA=500
				DA=(98/100)*x
				Gross=x+HRA+DA
				print(Gross)