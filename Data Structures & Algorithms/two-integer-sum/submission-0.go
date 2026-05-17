func twoSum(nums []int, target int) []int {
    seen := make(map[int]int) // num -> index

	for i,num := range nums {
		need := target - num
		if idx, ok := seen[need]; ok {
			return []int{idx, i}
		}

		seen[num] = i
	}

	return []int{0,0}
}
