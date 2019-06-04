
def find_closest_num(arr, target):
    min_diff = float("inf")
    low = 0
    high = len(arr) - 1
    closest_num = None

    # Edge cases for empty list or when the list is only one element
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid + 1] - target)
        if mid - 1 > 0:
            min_diff_left = abs(arr[mid - 1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = arr[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid + 1]

        # move the mid-point accordingly
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return arr[mid]

    return closest_num

A = [1, 2, 4, 5, 6, 6, 8, 9]
B = [2, 5, 6, 7, 8, 8, 9]
t = 5

value = find_closest_num(A, 11)
print(value)



