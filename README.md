# PAA (Perancangan Analisis Algoritma) 
# Nama : I Wayan Arigayu Saputra
# NIM  : F55123044
# Kelas: Teknik Informatika B

# Analisis Quiz1
- Worst case: O(n^2), terjadi jika pivot yang dipilih adalah elemen terkecil atau terbesar setiap kali, sehingga pembagian tidak seimbang.
- Best case: O(n log n), terjadi jika pivot membagi array secara merata pada setiap pembagian.
- Average case: O(n log n), berlaku pada kebanyakan kasus jika pivot yang dipilih cukup baik.

# Analisis Quiz2
## Bubble Sort
- Best Case: Ketika array sudah terurut (kompleksitas O(n)).
- Langkah-langkah: Bubble Sort hanya memeriksa elemen tanpa melakukan swap.
- Kelemahan: Tidak efisien untuk array besar.
## Merge Sort
- Best Case: Kompleksitas tetap O(n log n), karena pembagian dan penggabungan tetap dilakukan terlepas dari keadaan array.
- Kelebihan: Lebih cepat untuk array besar dibandingkan Bubble Sort.
