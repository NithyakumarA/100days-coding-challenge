#program to 
'''eg:
5
5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
	'''
	
class Solution:
    def printSquare(self, N):
        a=1
        for i in range (N):
            for j in range(1,a+1):
                print(j,end=" ") 
            print( )
            a=a+1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)
''' program to print
5
5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
class Solution:
    def printSquare(self, N):
        a=1
        b=1
        for i in range (N):
            for j in range(1,a+1):
                print(b,end=" ") 
            print( )
            a=a+1
            b+=1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)
'''program to print
5
5
* * * * *
* * * *
* * *
* *
*
'''
class Solution:
    def printSquare(self, N):
        a=N
        for i in range (N):
            for j in range(a):
                print("*",end=" ") 
            print( )
            a=a-1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)

'''program to print:
	5
5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''
class Solution:
    def printSquare(self, N):
        a=N
        for i in range (N):
            b=1
            for j in range(a):
                print(b,end=" ") 
                b=b+1
            print( )
            a=a-1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        if(N>=1 and N<=20):
        	ob = Solution()
        	ob.printSquare(N)