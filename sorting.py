# I Wayan Arigayu Saputra_F55123044
# Data yang akan diurutkan
X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 0]

# Implementasi Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Analisis Merge Sort:
# Worst case: O(n log n), terjadi pada setiap skenario karena proses pembagian dan penggabungan selalu sama.
# Best case: O(n log n), sama dengan worst case, karena tetap membutuhkan pembagian dan penggabungan.
# Average case: O(n log n), kompleksitas ini berlaku secara umum untuk merge sort.

# Implementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Analisis Quick Sort:
# Worst case: O(n^2), terjadi jika pivot yang dipilih adalah elemen terkecil atau terbesar setiap kali, sehingga pembagian tidak seimbang.
# Best case: O(n log n), terjadi jika pivot membagi array secara merata pada setiap pembagian.
# Average case: O(n log n), berlaku pada kebanyakan kasus jika pivot yang dipilih cukup baik.

# Pemanggilan fungsi untuk pengurutan dan menampilkan hasil
print("Merge Sort:")
merge_sort(X)
print(X)

X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 0]
print("\nQuick Sort:")
sorted_X = quick_sort(X)
print(sorted_X)