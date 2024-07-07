class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversedString = s[::-1]
        
        for i in range(len(s) - 1):
            subString = s[i:i+2]  
            if subString in reversedString:
                return True
        
        return False