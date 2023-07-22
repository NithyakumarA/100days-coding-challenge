'''program to print
A
A B
A B C
A B C D
A B C D E
'''
n=5
for i in range(n):
		a=65
		for j in range(i+1):
			print(chr(a),end=" ")
			a=a+1
		print()