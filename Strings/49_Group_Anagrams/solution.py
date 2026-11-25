class Solution(object) :

    def groupAnagrams(self , strs ) :
        list_map = {}
        output_list = []

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in list_map :
                list_map[sorted_word].extend([word])
            else :
                list_map[sorted_word] = [word]

        for item in list_map : 
            output_list.append(list_map[item])

        return output_list

solution = Solution()
print(solution.groupAnagrams(["eat","tea", "tan","ate","nat","bat"]))