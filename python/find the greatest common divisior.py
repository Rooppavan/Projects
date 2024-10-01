def RearrangeArray(arr, m): 
    if arr is None or m == 0: 
        return None 
 
    arr.sort() 
    result = [0] * m 
    left, right = 0, m - 1 
    i = 0 
 
    while left <= right: 
        if i % 2 == 0: 
            result[i] = arr[left] 
            left += 1 
        else: 
            result[i] = arr[right] 
            right -= 1 
        i += 1 
 
    return result 
 
def get_input(): 
    m = int(input().strip()) 
    arr = list(map(int, input().strip().split())) 
    return arr, m 
 
if name == "_main_": 
    arr, m = get_input() 
    result = RearrangeArray(arr, m) 
    if result is None: 
        print("None") 
    else: 
        print(*result)
