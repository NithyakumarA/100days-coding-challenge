# cook your dish here
''' 

Problem
Chef started watching a movie that runs for a total of 
X minutes.

Chef has decided to watch the first 
Y minutes of the movie at twice the usual speed as he was warned by his friends that the movie gets interesting only after the first 
Y minutes.
How long will Chef spend watching the movie in total?
Note: It is guaranteed that 
Y is even.
Input Format:
The first line contains two space separated integers,
X,Y - as per the problem statement.
Output Format:
Print in a single line, an integer denoting the total number of minutes that Chef spends in watching the movie.
'''
x,y=list(map(int,input().split()))
if(x>=0 and x<=1000 and y>=0 and y<=1000):
			if(x>y and y%2==0):
				c=y//2
				d=x-c
				print(d)