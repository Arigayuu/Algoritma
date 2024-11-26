# F55123044_I Wayan Arigayu Saputra
import random

# Generate bilangan random
random.seed(40)
numbers = [random.randint(0, 100) for _ in range(50)]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive merge sort
        merge_sort(left)
        merge_sort(right)

        # Merge the two halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    print("Original numbers:", numbers)
    sorted_numbers = merge_sort(numbers)
    print("Sorted numbers (Merge Sort):", sorted_numbers)