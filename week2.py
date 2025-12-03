# ============================
# 1. Recursion to sum first 10 numbers
# ============================
def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)

print("Sum of first 10 numbers:", sum_recursive(10))  # 55


# ============================
# 2. Fibonacci series of 8 terms
# ============================
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print("Fibonacci (8 terms):", fibonacci(8))  
# Output: [0, 1, 1, 2, 3, 5, 8, 13]


# ============================
# 3. Dynamic array simulation
# ============================
def dynamic_array_insert(values):
    array = []
    capacity = 2
    print("\nDynamic Array Simulation:")
    print("Initial capacity:", capacity)

    for v in values:
        if len(array) == capacity:   # Need to resize
            capacity *= 2
            print(f"Resizing... New capacity: {capacity}")
        array.append(v)
        print("Array:", array)

values = [10, 20, 30, 40, 50]
dynamic_array_insert(values)


# ============================
# 4. Linear search
# ============================
def linear_search(arr, target):
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            return i
    return -1

arr = [2, 5, 7, 10, 14, 20]
print("\nLinear Search Result:", linear_search(arr, 10))  # index 3


# ============================
# 5. Trace binary search
# ============================
def binary_search_trace(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"low={low}, high={high}, mid={mid}, value={arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr2 = [1, 3, 5, 7, 9, 11, 13]
print("\nBinary Search Result:", binary_search_trace(arr2, 9))  # index 4


# ============================
# 6. Time and space complexities
# (Written as comments)
# ============================

# Linear Search:
# Time: O(n)
# Space: O(1)

# Binary Search:
# Time: O(log n)
# Space: O(1) iterative, O(log n) recursive