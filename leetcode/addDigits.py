class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while(num>=10):
            sum=0
            while(num>0):
                sum+=num%10
                num/=10
            num=sum    
        return num

"""
one line solution (num-1)%9 +1
"""
