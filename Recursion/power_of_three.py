'''
Approach 1
Time Comlpexity -- O(log3n)
Space Complexity -- 0(1)
Divide number recursively by 3 until it reduces to 1 , if reduced to 1 true else false
'''

class Solution(object):
    def checkPower(self,n):
        if n<=0:
            return False
        if n==1:
            return True
        return n%3==0 and self.checkPower(n//3)
        
    def isPowerOfThree(self, n):
        return self.checkPower(n)

'''
Approach 2
Time Comlpexity -- O(1)
Space Complexity -- 0(1)

The input is a 32 bit integer , we select max number of 
32 bit integer which is 3^19 and thereby return 3^19%n==0
'''

class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        return 3**19%n==0

'''
Approach 3
Time Comlpexity -- O(1)
Space Complexity -- O(1)

3^x=n => take log base 10 both sides , equation : x=log10n/log103
'''
import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        value=math.log(n,10)/math.log(3,10)
        power=int(round(value))
        return 3**power==n
