import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

sizes = [100, 1000, 2000, 3000, 4000, 5000]

for size in sizes:
    # Generate a random list
    lst = [random.randint(0, 1000) for _ in range(size)]

    # Measure the time taken to sort
    start_time = time.time()
    _ = quick_sort(lst)
    elapsed_time = time.time() - start_time

    print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

