def linear_search(items, x):
    for i in range(len(items)):
        if items[i] == x:
            return i
    return False


arr = [1, 2, 3, 4, 5, 6, 7, 8]
x = 5
result = linear_search(arr, x)
print('value {0} is found at index {1}'.format(x, result))
