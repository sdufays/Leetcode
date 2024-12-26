from typing import List

"""
Python Notes:

.count gives every char and its frequency
index, value from enumerate(list)
sorted(word) returns list of every character in sorted order
"".join(sorted(word)) returns 1 string with characters in sorted order

"""
class Solution:
    #easy
    def containsDuplicate(self, nums: List[int]) -> bool:
        # visited set, iterate over lst
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
    #o(n) runtime and memory
    
    #easy
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    #o(n log n) runtime and o(n) memory

    #easy
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map, complement
        hash_map = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[number] = i
    #o(n) runtime and memory
    
    #medium
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n words, k average length
        result = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in result:
                result[key] = []
            result[key].append(word)
        return list(result.values())
    #o(n * k log k) runtime and o(nk) memory


        
