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

students_random_numbers = []

if not students_random_numbers:
    print("ERROR: The list of course code is empty, so the inversion count cannot be found by neither brute force nor divide and conquer approach.")
else:
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
