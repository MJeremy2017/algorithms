
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge 2 sorted array
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        if i == len(left):
            arr[k:] = right[j:]
        else:
            arr[k:] = left[i:]


if __name__ == "__main__":
    arr = [7, 15, 2, 1, 18, 1, 34, 12]
    merge_sort(arr)
    print(arr)
