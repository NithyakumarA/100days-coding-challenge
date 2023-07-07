# cook your dish here
''' problem statement:
MoEngage helps the Chef send email reminders about rated contests to the participants.
There are a total of 
N participants on Chef’s platform, and 
U of them have told Chef not to send emails to them.
If so, how many participants should MoEngage send the contest emails ?
Input Format:
The first and only line of input will contain a single line containing two space-separated integers 
N (the total number of users) and 
U (the number of users who don't want
to receive contest reminders).
output format:
Output in a single line, the number of users MoEngage has to send an email to.'''
a=input()
b=a.split()
l=[]
for i in range(len(b)):
	c=int(b[i])
	l.append(c)
j=0
d=l[j]-l[j+1]
print(d)