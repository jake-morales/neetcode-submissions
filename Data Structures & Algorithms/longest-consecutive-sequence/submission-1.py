class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create Set
        seen = {}
        for num in nums:
            seen[num] = True
        
        # Iterate through array. Count sequence only if element is start
        max_sequence_cnt = 0
        for num in nums:
            if num - 1 in seen: # not start
                continue
            
            curr_sequence_cnt = 0
            next = True
            while next:
                if num + 1 not in seen: # end of sequence
                    next = False
                
                num += 1
                curr_sequence_cnt += 1
            
            if curr_sequence_cnt > max_sequence_cnt:
                max_sequence_cnt = curr_sequence_cnt
        
        return max_sequence_cnt

            

            

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
                

