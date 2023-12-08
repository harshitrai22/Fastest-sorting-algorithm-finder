import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])

    # Swap the pivot element with
    # the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(arr, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursive call on the left of pivot
        quicksort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(arr, pi + 1, high)


def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)


# The main function to sort an array of given size


def heapSort(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Generate a list of 10000 random integers
arr = [random.randint(1, 10000) for i in range(10000)]

"""
arr = [93, 59, 62, 78, 56, 79, 65, 67, 36, 3, 36, 46, 36, 77, 47, 2, 45, 61, 5, 8,
       6, 18, 68, 80, 87, 2, 21, 92, 36, 16, 99, 4, 67, 22, 21, 92, 62, 17, 64, 86,
       19, 50, 68, 47, 32, 72, 61, 21, 32, 5, 24, 93, 59, 62, 78, 56, 79, 65, 67,
       36, 3, 36, 46, 36, 77, 47, 2, 45, 61, 5, 8,6, 18, 68, 80, 87, 2, 21, 92, 36,
       16, 99, 4, 67, 22, 21, 92, 62, 17, 64, 86, 19, 50, 68, 47, 32, 72, 61, 21, 32,
       5, 24, 93, 59, 62, 78, 56, 79, 65, 67, 36, 3, 36, 46, 36, 77, 47, 2, 45, 61,
       5, 8,6, 18, 68, 80, 87, 2, 21, 92, 36, 16, 99, 4, 67, 22, 21, 92, 62, 17, 64, 86,
       19, 50, 68, 47, 32, 72, 61, 21, 32, 5, 24, 93, 59, 62, 78, 56, 79, 65, 67, 36, 3,
       36, 46, 36, 77, 47, 2, 45, 61,5, 8,6, 18, 68, 80, 87, 2, 21, 92, 36, 16, 99, 4,
       67, 22, 21, 92, 62, 17, 64, 86,19, 50, 68, 47, 32, 72, 61, 21, 32, 5, 24]
"""

# Sort the list using each algorithm and calculate the time
import time

start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(arr.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

start_time = time.time()
mergeSort(arr.copy())
mergeSort_time = time.time() - start_time

start_time = time.time()
quicksort(arr.copy(), 0, len(arr) - 1)
quicksort_time = time.time() - start_time

start_time = time.time()
heapSort(arr.copy())
heapSort_time = time.time() - start_time

print("Bubble Sort time:", bubble_sort_time)
print("Selection Sort time:", selection_sort_time)
print("Insertion Sort time:", insertion_sort_time)
print("Merge Sort time:", mergeSort_time)
print("Quick Sort time:", quicksort_time)
print("Heap Sort time:", heapSort_time)

#Creating a dictionary and storing the algorithm name as key and time taken as values

fastest = {'Bubble sort': bubble_sort_time, 'Heap sort': heapSort_time, 'Quick sort': quicksort_time,
           'Merge sort': mergeSort_time, 'Insertion sort': insertion_sort_time, 'selection sort': selection_sort_time}

minimum = min(fastest.values())
res = [key for key in fastest if fastest[key] == minimum]

print("The fastest algorithm for this array is " + str(res), ", Time Taken is:", minimum)
