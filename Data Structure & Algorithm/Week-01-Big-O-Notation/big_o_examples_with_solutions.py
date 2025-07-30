"""
Week 1: Big O Notation - Examples with Solutions
================================================

This file contains 10 example problems to help you understand Big O notation
and algorithm analysis. Each problem includes the solution and time/space complexity analysis.
"""

# Problem 1: Find maximum element in an array
def find_maximum(arr):
    """
    Time Complexity: O(n) - we visit each element once
    Space Complexity: O(1) - only using constant extra space
    """
    if not arr:
        return None
    
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

# Problem 2: Check if number exists in sorted array (Binary Search)
def binary_search(arr, target):
    """
    Time Complexity: O(log n) - we eliminate half the search space each time
    Space Complexity: O(1) - only using constant extra space
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Problem 3: Print all pairs in an array
def print_all_pairs(arr):
    """
    Time Complexity: O(n²) - nested loops, each running n times
    Space Complexity: O(1) - only using constant extra space
    """
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs

# Problem 4: Calculate factorial recursively
def factorial(n):
    """
    Time Complexity: O(n) - we make n recursive calls
    Space Complexity: O(n) - recursion stack depth is n
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Problem 5: Access element at specific index
def get_element_at_index(arr, index):
    """
    Time Complexity: O(1) - constant time array access
    Space Complexity: O(1) - only using constant extra space
    """
    if 0 <= index < len(arr):
        return arr[index]
    return None

# Problem 6: Find all triplets with sum zero
def find_triplets_with_zero_sum(arr):
    """
    Time Complexity: O(n³) - three nested loops
    Space Complexity: O(1) - only using constant extra space (not counting output)
    """
    triplets = []
    n = len(arr)
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
    
    return triplets

# Problem 7: Linear search in unsorted array
def linear_search(arr, target):
    """
    Time Complexity: O(n) - might need to check all elements
    Space Complexity: O(1) - only using constant extra space
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Problem 8: Calculate power using repeated multiplication
def power_iterative(base, exponent):
    """
    Time Complexity: O(n) where n is the exponent
    Space Complexity: O(1) - only using constant extra space
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Problem 9: Check if string is palindrome
def is_palindrome(s):
    """
    Time Complexity: O(n) - we check n/2 characters
    Space Complexity: O(1) - only using constant extra space
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Problem 10: Count frequency of each element
def count_frequency(arr):
    """
    Time Complexity: O(n²) - for each element, we count occurrences
    Space Complexity: O(n) - storing frequency map
    """
    frequency = {}
    
    for element in arr:
        count = 0
        for item in arr:  # This makes it O(n²)
            if item == element:
                count += 1
        frequency[element] = count
    
    return frequency

# Test cases
if __name__ == "__main__":
    # Test Problem 1
    print("Problem 1 - Find Maximum:")
    test_arr = [3, 7, 1, 9, 4, 6]
    print(f"Maximum in {test_arr}: {find_maximum(test_arr)}")
    
    # Test Problem 2
    print("\nProblem 2 - Binary Search:")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13]
    print(f"7 exists in {sorted_arr}: {binary_search(sorted_arr, 7)}")
    print(f"8 exists in {sorted_arr}: {binary_search(sorted_arr, 8)}")
    
    # Test Problem 3
    print("\nProblem 3 - All Pairs:")
    small_arr = [1, 2, 3]
    print(f"All pairs in {small_arr}: {print_all_pairs(small_arr)}")
    
    # Test Problem 4
    print("\nProblem 4 - Factorial:")
    print(f"Factorial of 5: {factorial(5)}")
    
    # Test Problem 5
    print("\nProblem 5 - Get Element:")
    print(f"Element at index 2 in {test_arr}: {get_element_at_index(test_arr, 2)}")
    
    # Test Problem 9
    print("\nProblem 9 - Palindrome:")
    print(f"'racecar' is palindrome: {is_palindrome('racecar')}")
    print(f"'hello' is palindrome: {is_palindrome('hello')}")
