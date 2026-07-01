class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create hash
        # Go through each element, and see how far you can go in either direction
        # Save the greatest length
        seen = {}
        for num in nums:
            seen[num] = True

        max_sequence_cnt = 0
        for num in nums:
            curr_sequence_cnt = 1
            # Look Right
            next = True
            curr = num
            while(next):
                if curr + 1 in seen:
                    curr_sequence_cnt += 1
                    curr += 1
                else:
                    next = False
            
            # Look Left
            next = True
            curr = num
            while(next):
                if curr - 1 in seen:
                    curr_sequence_cnt += 1
                    curr -= 1
                else:
                    next = False
            
            if curr_sequence_cnt > max_sequence_cnt:
                max_sequence_cnt = curr_sequence_cnt
        
        return max_sequence_cnt
                

