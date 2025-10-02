class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_num = { "I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000 }

        total = 0
        i = 0
        x = len(s)

        while i < x :
            if i < x-1 and roman_num[s[i]] < roman_num[s[i+1]] :
                total += roman_num[s[i+1]] - roman_num[s[i]]
                i += 2
            else :
                total += roman_num[s[i]]
                i += 1
        return total

 
 # Testing the function
s = "MCMXCIV"

solution = Solution()
result = solution.romanToInt(s) 
print(result) 