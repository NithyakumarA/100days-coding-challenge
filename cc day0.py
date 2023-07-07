# cook your dish here
'''problem statement:
	1) Write a program to print all sum combinations of three numbers by taking two numbers at a time.

Sample Input:
num1 = 2
num2 = 4
num3 = 6

Sample Output:
6
8
10

Explanation:
2 + 4 = 6
2 + 6 = 8
4 + 6 = 10
source code:
	'''

a=int(input("num1="))
b=int(input("num2="))
c=int(input("num3="))
x=a+b
y=b+c
z=c+a
print(x)
print(y)
print(z)
'''
2) Write a program to find the area of a circle. (Use predefined 'pi' variable)

Sample Input:
r = 6
Sample Output:
113.09
source code:
	'''
pi=3.14
r=int(input())
print(pi*(r**2))
'''
3) Check if a given number is an even number or an odd number. Print Yes if it is an even number, else No.

Sample Input: 
12 
Sample Output: 
Yes'''
a=int(input())
if(a%2==0):
	print('yes')
else:
	print('No')