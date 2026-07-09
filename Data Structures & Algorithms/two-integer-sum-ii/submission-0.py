class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 3 4

        # 1 4 5 6 7 9, t = 12
        #     ^
        #         ^
        i = 0
        j = len(numbers)-1

        while (i < j):
            diff = target - numbers[i] - numbers[j]
            print("diff", diff)
            print("i", i, " number: ", numbers[i])
            print("j", j, " number: ", numbers[j])
            if diff == 0:
                return [i+1, j+1]
            elif diff < 0: # number sum is too big. Decrease big side
                j -= 1
            else: # number sum too small. Incrase smaller side
                i += 1

        return []

        