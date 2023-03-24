#merge array
# get no of el in new array
#sort using merge sort
# get middle index
# [1,2,3,4,5]
import math
def median_of_two_sorted_array(nums1, nums2):
    merged = nums1 + nums2

    # merge sort
    def mergeSort(arr, l, r):
        if l < r:
    
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2
    
            # Sort first and second halves
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
    
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    mergeSort(merged, 0, len(merged) - 1)

    # the sort algo happens in place 
    if len(merged) % 2 == 0:
        #even
        return (merged[int(len(merged) / 2)] + merged[int((len(merged) / 2)-1)]) /2
    else:
        return merged[int(math.floor(len(merged)/2))]
    