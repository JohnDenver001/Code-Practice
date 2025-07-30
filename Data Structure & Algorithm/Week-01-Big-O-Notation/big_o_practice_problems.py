"""
Week 1: Big O Notation - Practice Problems (No Solutions)
=========================================================

Solve these problems and analyze their time and space complexity.
Try to identify the Big O notation for each solution you write.
"""

# Problem 1: Find the second largest element in an array
def find_second_largest(arr):
    """
    TODO: Implement this function
    
    Given an array of integers, find the second largest element.
    If there's no second largest (e.g., all elements are same), return None.
    
    Example:
    Input: [3, 7, 1, 9, 4, 6]
    Output: 7
    
    Input: [5, 5, 5]
    Output: None
    
    Analyze:
    - What's the time complexity of your solution?
    - What's the space complexity?
    - Can you solve it in one pass?
    """

arr = [5, 1, 2, 5, 1, 8, 2, 5, 3, 2, 9, 13, 1, 10, 13, 11, 12]
find_second_largest(arr)
"""
    Analyze:
    - What's the time complexity of your solution? O(n)
    - What's the space complexity? O(n)
    - Can you solve it in one pass? No, got a really hard time
"""

# Problem 2: Check if array contains duplicates
def has_duplicates(arr):
    """
    TODO: Implement this function
    
    Given an array, return True if it contains duplicates, False otherwise.
    
    Example:
    Input: [1, 2, 3, 1]
    Output: True
    
    Input: [1, 2, 3, 4]
    Output: False
    
    Analyze:
    - Try multiple approaches (nested loops, sorting, using extra space)
    - Compare their time and space complexities
    """     

# Problem 3: Reverse an array in-place
def reverse_array_inplace(arr):
    """
    TODO: Implement this function
    
    Reverse the given array without using extra space.
    
    Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1] (modify the original array)
    
    Analyze:
    - What's the time complexity?
    - What's the space complexity?
    """
    pass

# Problem 4: Count inversions in array
def count_inversions(arr):
    """
    TODO: Implement this function
    
    An inversion is when a larger element appears before a smaller element.
    Count the total number of inversions.
    
    Example:
    Input: [2, 3, 8, 6, 1]
    Output: 5
    Inversions: (2,1), (3,1), (8,6), (8,1), (6,1)
    
    Analyze:
    - What's the brute force approach complexity?
    - Can you think of a more efficient solution?
    """
    pass

# Problem 5: Find missing number in sequence
def find_missing_number(arr, n):
    """
    TODO: Implement this function
    
    Given an array containing n-1 distinct numbers in range [1, n],
    find the missing number.
    
    Example:
    Input: [1, 2, 4, 6, 3, 7, 8], n = 8
    Output: 5
    
    Analyze:
    - Try different approaches (sum formula, XOR, sorting)
    - Compare their complexities
    """
    pass

# Problem 6: Rotate array by k positions
def rotate_array(arr, k):
    """
    TODO: Implement this function
    
    Rotate array to the right by k steps.
    
    Example:
    Input: [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]
    
    Analyze:
    - Try multiple approaches
    - What's the optimal time and space complexity?
    """
    pass

# Problem 7: Find peak element
def find_peak_element(arr):
    """
    TODO: Implement this function
    
    A peak element is greater than its neighbors.
    Find any peak element's index.
    
    Example:
    Input: [1, 2, 3, 1]
    Output: 2 (element 3 at index 2)
    
    Input: [1, 2, 1, 3, 5, 6, 4]
    Output: 1 or 5 (either peak)
    
    Analyze:
    - What's the linear search complexity?
    - Can you solve it in O(log n)?
    """
    pass

# Problem 8: Merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    """
    TODO: Implement this function
    
    Merge two sorted arrays into one sorted array.
    
    Example:
    Input: [1, 3, 5], [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]
    
    Analyze:
    - What's the time complexity?
    - What's the space complexity?
    """
    pass

# Problem 9: Find majority element
def find_majority_element(arr):
    """
    TODO: Implement this function
    
    Find the element that appears more than n/2 times.
    Assume such element always exists.
    
    Example:
    Input: [3, 2, 3]
    Output: 3
    
    Input: [2, 2, 1, 1, 1, 2, 2]
    Output: 2
    
    Analyze:
    - Try different approaches (brute force, sorting, hash map)
    - Can you solve it in O(1) space? (Boyer-Moore algorithm)
    """
    pass

# Problem 10: Calculate power efficiently
def power_optimized(base, exponent):
    """
    TODO: Implement this function
    
    Calculate base^exponent more efficiently than O(n).
    
    Example:
    Input: base = 2, exponent = 10
    Output: 1024
    
    Analyze:
    - What's wrong with the naive O(n) approach?
    - How can you use the property: x^n = (x^(n/2))^2?
    - What's the time complexity of the optimized solution?
    """
    pass

# Test cases - Uncomment and run after implementing the functions
if __name__ == "__main__":
    # Test your implementations here
    # Remember to analyze the time and space complexity of each solution
    
    print("Implement the functions above and test them here!")
    print("Don't forget to analyze the Big O notation for each solution.")
    
    # Example test for Problem 1:
    # test_arr = [3, 7, 1, 9, 4, 6]
    # print(f"Second largest in {test_arr}: {find_second_largest(test_arr)}")
    
    # Add more test cases for each problem...
