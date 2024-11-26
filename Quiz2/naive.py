# F55123044_F55123044
import random

# Generate bilangan random
random.seed(40)
numbers = [random.randint(0, 100) for _ in range(50)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    print("Original numbers:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers (Bubble Sort):", sorted_numbers)