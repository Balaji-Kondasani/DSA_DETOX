'''
Approach 1
Time Complexity -- O(1)
Space Complexity -- O(1)

Technique Used -- log function to find nearest power
'''

import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        power=int(math.log(n,2))
        return 2**power==n
    
'''
Approach 2
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- log function to find nearest power followed by recursion
'''

import math
class Solution(object):
    def findPower(self,power):
        if power==0:
            return 1
        return 2*self.findPower(power-1)
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        power=int(math.log(n,2))
        return self.findPower(power)==n
    
'''
Approach 3
Time Complexity -- O(1)
Space Complexity -- O(1)

Technique Used -- Bit Manipulation
'''

import math
class Solution(object):
    def isPowerOfTwo(self, n):
        return n>0 and ((n)&(n-1)==0)