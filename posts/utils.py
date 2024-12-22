def binary_search(data, s_title):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == s_title:
            return mid
        elif data[mid] < s_title:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def bubble_sort(data, key=lambda post: post):

    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if key(data[j]) > key(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data