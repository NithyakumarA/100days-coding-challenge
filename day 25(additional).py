#program to print stars(*) in form
'''eg:
5
*
* *
* * *
* * * *
* * * * *
* * * * *
	'''
	
class Solution:
    def printSquare(self, N):
        a=1
        for i in range (N):
            for j in range(a):
                print("*",end=" ")
            print( )
            a=a+1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)