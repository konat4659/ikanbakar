# Data yang akan diurutkan
data = [45, 12, 78, 23, 56, 89, 34, 67, 90, 11, 5, 38, 72]

# Mengurutkan data menggunakan metode Heap Sort
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Mengubah list menjadi heap
    return [heapq.heappop(arr) for _ in range(len(arr))]  # Mengambil elemen-elemen dari heap

# Mengurutkan data
sorted_data = heap_sort(data)

# Fungsi untuk melakukan Interpolation Search
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        # Menghitung posisi perkiraan mid
        mid = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # Cek apakah x ditemukan pada mid
        if arr[mid] == x:
            return mid  # Return posisi indeks
        # Jika nilai yang dicari lebih besar, maka pindah ke kanan
        elif arr[mid] < x:
            low = mid + 1
        # Jika nilai yang dicari lebih kecil, maka pindah ke kiri
        else:
            high = mid - 1
    return -1  # Jika tidak ditemukan

# Menampilkan hasil pencarian untuk x = 11 dan x = 23
x1 = 11
x2 = 23

# Pencarian untuk x = 11
index1 = interpolation_search(sorted_data, x1)
if index1 != -1:
    print(f"Data {x1} ditemukan pada indeks {index1}.")
else:
    print(f"Data {x1} tidak ditemukan.")

# Pencarian untuk x = 23
index2 = interpolation_search(sorted_data, x2)
if index2 != -1:
    print(f"Data {x2} ditemukan pada indeks {index2}.")
else:
    print(f"Data {x2} tidak ditemukan.")
