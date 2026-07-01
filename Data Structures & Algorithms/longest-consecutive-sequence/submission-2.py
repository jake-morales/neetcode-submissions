from collections import defaultdict
# Optimal O(n) - each element contributes once
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0

        for num in nums:
            if not mp[num]: # This creats an entry with default (0)
                # This is critical for updating the neighbor boundaries
                # e.g. mp[num - 0] = mp[num]
                mp[num] = mp[num-1] + mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
                longest = max(longest, mp[num])

        print(mp)
        # nums=[2,20,4,10,3,4,5]
        # defaultdict({2: 4, 1: 0, 3: 3, 20: 1, 19: 0, 21: 0, 4: 3, 5: 4, 10: 1, 9: 0, 11: 0, 6: 0})
        
        return longest



# Linear Solution
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # Create Set
#         seen = {}
#         for num in nums:
#             seen[num] = True
        
#         # Iterate through array. Count sequence only if element is start
#         max_sequence_cnt = 0
#         for num in nums:
#             if num - 1 in seen: # not start
#                 continue
            
#             curr_sequence_cnt = 0
#             next = True
#             while next:
#                 if num + 1 not in seen: # end of sequence
#                     next = False
                
#                 num += 1
#                 curr_sequence_cnt += 1
            
#             if curr_sequence_cnt > max_sequence_cnt:
#                 max_sequence_cnt = curr_sequence_cnt
        
#         return max_sequence_cnt

            

            
# Brute Force Solution
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # Create hash
#         # Go through each element, and see how far you can go in either direction
#         # Save the greatest length
#         seen = {}
#         for num in nums:
#             seen[num] = True

#         max_sequence_cnt = 0
#         for num in nums:
#             curr_sequence_cnt = 1
#             # Look Right
#             next = True
#             curr = num
#             while(next):
#                 if curr + 1 in seen:
#                     curr_sequence_cnt += 1
#                     curr += 1
#                 else:
#                     next = False
            
#             # Look Left
#             next = True
#             curr = num
#             while(next):
#                 if curr - 1 in seen:
#                     curr_sequence_cnt += 1
#                     curr -= 1
#                 else:
#                     next = False
            
#             if curr_sequence_cnt > max_sequence_cnt:
#                 max_sequence_cnt = curr_sequence_cnt
        
#         return max_sequence_cnt
                

