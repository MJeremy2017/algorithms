"""
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
"""


def partition(l, low, high):
    pivot = l[high]
    i = low  # the current index of smaller value
    for j in range(low, high):
        if l[j] < pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[high], l[i] = l[i], l[high]
    return i


def quick_sort(l, low, high):
    if low < high:
        i = partition(l, low, high)
        quick_sort(l, low, i-1)
        quick_sort(l, i+1, high)
