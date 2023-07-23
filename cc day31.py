'''program to print
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *'''
n=5
for i in range(n):
	for j in range(i,n):
		print("*",end=" ")
	for k in range(i*2):
		print(" ",end=" ")
	for l in range(i,n):
		print("*",end=" ")
	print()
for i in range(n):
	for j in range(i+1):
		print("*",end=" ")
	for k in range(i,n-1):
		print(" ",end=" ")
	for l in range(i,n-1):
		print(" ",end=" ")
	for m in range(i+1):
		print("*",end=" ")
	print()

'''program to print:
* * * *
*     *
*     *
* * * *
	'''
	
n=4
for i  in range(n):
	for j in range(n):
		if (i==1 and j%3!=0) or (i==2 and j%3!=0):
			print(" ",end=" ")
		else:
			print('*',end=" ")
	print()