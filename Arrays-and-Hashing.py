from collections import defaultdict
from collections import Counter
from typing import List
import heapq

"""
Python Notes:

.count gives every char and its frequency
index, value from enumerate(list)
sorted(word) returns list of every character in sorted order
"".join(sorted(word)) returns 1 string with characters in sorted order
defaultdict(default) is a subclass of Python's built-in dict that automatically provides a default value for keys that don't exist
--> need * from collections import defaultdict * , can pass in list to init with empty lists or ints to init. with zero's
tuples are immutable, can use to pass in lists for keys of a dictionary
count[ord(char) - ord('a')] maps the character to an index in the range [0, 25] where 0 is a and 25 is z
can use Counter (from collections) to count the occurrences of each number/char in a list
.items() for when you want to iterate over both the keys and values in a dictionary
can use bucket sort when you need frequencies 
heaq gives you a min heap --> if you want a max heap, do heapq.nlargest(n, iterable, key=None) to get n largest vals

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
    
    #medium, better implementation
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n words, k average length
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26 # o(1) memory
            for char in word:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(word)
        return list(result.values())
    #o(n*k) for runtime and memory

    #medium
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, this approach is better when k << n
        frequency = Counter(nums) # o(n) time and space
        n = len(nums)
        buckets = [[] for _ in range(n+1)] # o(n) space
        for num, freq in frequency.items(): #o(n) time
            buckets[freq].append(num)
        top_k= [] 
        for freq in range(n,0,-1): # o(n) time
            for num in buckets[freq]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        return top_k
    #o(n) runtime and memory

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max heap, better when k !<< n
        frequency = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, frequency.items(), key=lambda x: x[1])]
    #o(n log k), o(n) memory


        
