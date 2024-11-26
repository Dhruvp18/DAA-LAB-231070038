def count_inversions_brute_force(arr):
    inversions = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
                
    return inversions

def count_inversions_divide_and_conquer(arr):
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inversions = merge_sort(arr, left, mid)
    inversions += merge_sort(arr, mid + 1, right)
    inversions += merge_and_count(arr, left, mid, right)
    
    return inversions

def merge_and_count(arr, left, mid, right):
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    inversions = 0
    
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            inversions += (mid - i + 1 - left)  
            j += 1
        k += 1
    
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
        
    return inversions

students_random_numbers = [
    [12, 17, 14, 18, 11, 15], [14, 12, 11, 13, 19, 16], [17, 19, 13, 18, 12, 15],
    [12, 16, 18, 14, 15, 11], [18, 17, 11, 15, 19, 14], [18, 13, 11, 12, 17, 10],
    [12, 14, 18, 15, 17, 13], [14, 16, 18, 11, 12, 10],
    
    [16, 19, 12, 17, 14, 15], [13, 18, 16, 14, 11, 12], [13, 11, 18, 17, 15, 19],
    [16, 13, 18, 14, 15, 12], [15, 19, 13, 17, 18, 10], [17, 14, 19, 11, 13, 12],
    [15, 11, 18, 12, 19, 14], [16, 15, 19, 13, 14, 11],
    
    [12, 19, 11, 13, 18, 14], [11, 14, 19, 15, 16, 10], [14, 15, 16, 18, 12, 17],
    [13, 14, 19, 11, 15, 16], [17, 11, 14, 19, 15, 12], [14, 18, 17, 13, 10, 19],
    [14, 11, 19, 18, 12, 10], [18, 13, 19, 17, 16, 11],
    
    [19, 16, 11, 13, 14, 12], [17, 13, 14, 15, 11, 12], [12, 19, 18, 17, 15, 14],
    [16, 17, 14, 12, 15, 10], [19, 12, 17, 11, 13, 14], [13, 16, 15, 19, 12, 10],
    [15, 12, 19, 16, 14, 11], [18, 15, 13, 12, 10, 19],
    
    [17, 18, 19, 14, 15, 10], [11, 19, 12, 13, 14, 16], [14, 15, 19, 12, 11, 13],
    [16, 19, 13, 14, 11, 15], [15, 18, 14, 13, 19, 12], [11, 12, 19, 18, 15, 10],
    [19, 17, 11, 12, 14, 15], [16, 14, 18, 12, 13, 19],
    
    [12, 14, 15, 19, 18, 10], [19, 17, 11, 13, 15, 12], [14, 19, 15, 11, 12, 10],
    [16, 18, 12, 14, 19, 15], [15, 12, 10, 19, 13, 18], [17, 13, 14, 15, 11, 12],
    [11, 19, 18, 14, 10, 16], [16, 15, 11, 19, 12, 13],
    
    [13, 14, 19, 18, 10, 15], [15, 12, 16, 14, 19, 11], [18, 19, 12, 11, 10, 17],
    [16, 15, 13, 14, 19, 11], [14, 12, 19, 15, 10, 18], [11, 17, 18, 12, 13, 19],
    [16, 11, 19, 15, 13, 10], [12, 19, 14, 11, 18, 15],
    
    [19, 17, 10, 14, 16, 12], [12, 19, 15, 11, 18, 14], [19, 10, 15, 13, 18, 16],
    [16, 12, 19, 17, 10, 14], [11, 18, 19, 10, 15, 13], [15, 12, 19, 11, 16, 18],
    [12, 19, 15, 14, 10, 13], [13, 11, 16, 10, 12, 19],
    
    [10, 15, 14, 12, 19, 18], [11, 12, 17, 13, 16, 19], [10, 14, 15, 12, 17, 18],
    [13, 19, 10, 16, 18, 12], [15, 10, 14, 17, 18, 12], [12, 13, 16, 19, 11, 14],
    [17, 18, 15, 10, 14, 19], [11, 10, 19, 16, 14, 12],
    
    [19, 12, 10, 14, 15, 17], [10, 11, 15, 19, 12, 14], [17, 19, 12, 10, 18, 16],
    [11, 18, 16, 12, 15, 19], [15, 14, 19, 11, 12, 17], [18, 16, 12, 19, 14, 10],
    [14, 12, 11, 15, 18, 10], [10, 15, 11, 19, 14, 17]
]

brute_force_inversion_counts = [count_inversions_brute_force(sublist) for sublist in students_random_numbers]

divide_and_conquer_inversion_counts = [count_inversions_divide_and_conquer(sublist[:]) for sublist in students_random_numbers]

total_inversion_count_brute_force = sum(brute_force_inversion_counts)
total_inversion_count_divide_and_conquer = sum(divide_and_conquer_inversion_counts)

def categorize_inversion_counts(inversion_counts):
    categories = {}
    for index, count in enumerate(inversion_counts):
        if count not in categories:
            categories[count] = []
        categories[count].append(index + 1)  
    return categories

brute_force_categories = categorize_inversion_counts(brute_force_inversion_counts)
divide_and_conquer_categories = categorize_inversion_counts(divide_and_conquer_inversion_counts)

print("Total inversion count (Brute Force) across all students:", total_inversion_count_brute_force)
print("Total inversion count (Divide and Conquer) across all students:", total_inversion_count_divide_and_conquer)

print("\nCategorized Inversion Counts (Brute Force):")
for count, students in sorted(brute_force_categories.items()):
    print(f"Inversion Count {count}: Students {students}")

print("\nCategorized Inversion Counts (Divide and Conquer):")
for count, students in sorted(divide_and_conquer_categories.items()):
    print(f"Inversion Count {count}: Students {students}")
