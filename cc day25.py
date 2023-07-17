#program to print stars(*) in nxn matrix form
'''eg:
5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
	'''
	
class Solution:

    def printSquare(self, N):

        for i in range (N):
            for j in range(N):
                print("*",end=" ")
            print( )
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)