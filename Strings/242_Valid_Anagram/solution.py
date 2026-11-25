class Solution(object):

    def isAnagramV1(self , s , t ) -> bool :

        s_map ={}
        t_map={}

        if len(s) != len(t):
            return False

        for chac in s :
            if chac in s_map:
                s_map[chac] += 1
            else :
                s_map[chac] = 1

        
        for chac in t:
            if chac in t_map:
                t_map[chac] += 1
            else :
                t_map[chac] =1

        if s_map == t_map :
            return True
        return False

    def isAnagramV2(self , s , t ) -> bool :

        s_map ={}
        t_map={}
        
        if len(s) != len(t):
            return False
        
        for chac in s :
            s_map[chac] = s_map.get(chac , 0) + 1
                
        for chac in t:
            t_map[chac] = t_map.get(chac , 0) + 1

        return s_map == t_map


solution = Solution()
print(solution.isAnagramV2("anagram" , "nagaram"))


