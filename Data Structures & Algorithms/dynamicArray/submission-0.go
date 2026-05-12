type DynamicArray struct {
	arr []int
	cap int
	len int
}

func NewDynamicArray(capacity int) *DynamicArray {
	newDA := &DynamicArray{}
	newDA.arr = make([]int, capacity)
	newDA.cap = capacity
	return newDA
}

func (da *DynamicArray) Get(i int) int {
	return da.arr[i]
}

func (da *DynamicArray) Set(i int, n int) {
	da.arr[i] = n
}

func (da *DynamicArray) Pushback(n int) {
	if da.len+1 > da.cap {
		da.resize()
	}

	da.arr[da.len] = n
	da.len++
}

func (da *DynamicArray) Popback() int {
	var pb int
	pb = da.arr[da.len-1]
	da.arr[da.len-1] = 0
	da.len--
	return pb
}

func (da *DynamicArray) resize() {
	newArr := make([]int, da.cap*2)
	copy(newArr, da.arr)
	da.arr = newArr
	da.cap = da.cap * 2
}

func (da *DynamicArray) GetSize() int {
	return da.len
}

func (da *DynamicArray) GetCapacity() int {
	return da.cap
}
