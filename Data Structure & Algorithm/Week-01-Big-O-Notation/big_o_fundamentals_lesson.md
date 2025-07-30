# Week 1: Big O Notation & Time Complexity - Fundamentals Lesson
*📚 Read this lesson first before attempting the practice problems*

---

## 🎯 Learning Objectives
By the end of this lesson, you will:
1. Understand what Big O notation represents
2. Analyze time and space complexity of algorithms
3. Recognize common complexity patterns
4. Make informed decisions about algorithm efficiency

---

## 🤔 What is Big O Notation?

**Big O notation** describes the **worst-case** performance of an algorithm as the input size grows to infinity. It helps us:
- Compare algorithm efficiency
- Predict how algorithms scale
- Choose the best solution for large datasets

### 🎭 The Analogy
Think of Big O like describing how long it takes to find a book:
- **O(1)**: You know exactly where the book is (constant time)
- **O(log n)**: You use the library catalog system (logarithmic time)
- **O(n)**: You check every book one by one (linear time)
- **O(n²)**: You compare every book with every other book (quadratic time)

---

## 📊 Common Big O Complexities (Best to Worst)

### 1. **O(1) - Constant Time** ⚡
```python
def get_first_element(arr):
    return arr[0]  # Always takes the same time regardless of array size

def hash_lookup(dictionary, key):
    return dictionary[key]  # Hash table lookup
```
**Real-world example**: Accessing array element by index, dictionary lookup

### 2. **O(log n) - Logarithmic Time** 📈
```python
def binary_search(arr, target): #[6, 5, 4, 3, 2, 1], 6
    left = 0 #Represent starting index (0)
    #After first iteration - 4
    #After second iteration - 5
    #After third iteration - 

    right = len(arr) - 1 #Represents the last index
    
    while left <= right:
        mid = (left + right) // 2 #Mid represents the index

        if arr[mid] == target: #arr[mid] represents the number in that index
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return -1
```
**Real-world example**: Binary search, finding element in balanced binary tree

### 3. **O(n) - Linear Time** 📏
```python
def find_maximum(arr):
    max_val = arr[0]
    for num in arr:  # Must check every element once
        if num > max_val:
            max_val = num
    return max_val

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1
```
**Real-world example**: Finding max/min, linear search, printing all elements

### 4. **O(n log n) - Linearithmic Time** 📊
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # log n levels
    right = merge_sort(arr[mid:])   # log n levels
    
    return merge(left, right)       # O(n) work at each level
```
**Real-world example**: Efficient sorting algorithms (merge sort, heap sort)

### 5. **O(n²) - Quadratic Time** 🐌
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # Outer loop: n times
        for j in range(n-1):    # Inner loop: n times
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):       # n iterations
        for j in range(len(arr)):   # n iterations for each i
            pairs.append((arr[i], arr[j]))
    return pairs
```
**Real-world example**: Bubble sort, comparing all pairs, nested loops

### 6. **O(2ⁿ) - Exponential Time** 💥
```python
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)  # Two recursive calls each time
```
**Real-world example**: Naive recursive solutions, generating all subsets

---

## 🧠 How to Analyze Time Complexity

### **Step 1: Identify the Basic Operations**
Look for:
- Loops
- Recursive calls
- Function calls
- Basic operations (comparisons, assignments)

### **Step 2: Count How Operations Scale**
```python
# Example 1: What's the complexity?
def example1(arr):
    total = 0                    # O(1)
    for num in arr:              # O(n) - loops n times
        total += num             # O(1) - constant operation
    return total                 # O(1)
# Overall: O(1) + O(n) * O(1) + O(1) = O(n)

# Example 2: What's the complexity?
def example2(arr):
    for i in range(len(arr)):           # O(n) - outer loop
        for j in range(len(arr)):       # O(n) - inner loop
            print(arr[i] + arr[j])      # O(1) - constant operation
# Overall: O(n) * O(n) * O(1) = O(n²)

# Example 3: What's the complexity?
def example3(arr):
    if len(arr) == 0:           # O(1)
        return
    example3(arr[1:])           # O(n) recursive calls, each creating O(n) slice
# Overall: O(n²) due to string/list slicing in recursion
```

### **Step 3: Focus on the Dominant Term**
```python
# This function has multiple parts:
def complex_function(arr):
    # Part 1: O(n²)
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(i, j)
    
    # Part 2: O(n)
    for num in arr:
        print(num)
    
    # Part 3: O(1)
    print("Done")

# Total: O(n²) + O(n) + O(1) = O(n²)
# We only keep the dominant (highest growing) term
```

---

## 💾 Space Complexity

Space complexity measures how much **extra memory** an algorithm uses.

### **Types of Space Usage:**
1. **Input space**: Memory for input (usually not counted)
2. **Auxiliary space**: Extra memory used by algorithm
3. **Output space**: Memory for output

### **Examples:**
```python
# O(1) Space - Constant extra memory
def find_sum(arr):
    total = 0        # Only using one extra variable
    for num in arr:
        total += num
    return total

# O(n) Space - Linear extra memory
def reverse_array(arr):
    reversed_arr = []      # Creating new array of size n
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# O(n) Space - Due to recursion call stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)  # n recursive calls on call stack
```

---

## 🔍 Common Patterns to Recognize

### **Pattern 1: Single Loop → O(n)**
```python
for i in range(n):
    # constant work
```

### **Pattern 2: Nested Loops → O(n²)**
```python
for i in range(n):
    for j in range(n):
        # constant work
```

### **Pattern 3: Divide and Conquer → O(log n) or O(n log n)**
```python
# Binary search: O(log n)
while left <= right:
    mid = (left + right) // 2
    # eliminate half each iteration

# Merge sort: O(n log n)
# log n levels, O(n) work per level
```

### **Pattern 4: Multiple Separate Loops → Add complexities**
```python
# O(n) + O(n) = O(n)
for i in range(n):
    # do something
for j in range(n):
    # do something else
```

### **Pattern 5: Drop Constants and Lower Terms**
```python
# O(3n + 5) → O(n)
# O(n² + n + 1) → O(n²)
# O(2^n + n²) → O(2^n)
```

---

## 🎯 Practical Tips for Beginners

### **1. Start Simple**
- Count loops first
- One loop = O(n), two nested loops = O(n²)
- Recursive calls often = O(depth of recursion)

### **2. Ask These Questions**
- How many times does each line execute?
- How does this change as input size grows?
- What's the worst-case scenario?

### **3. Common Mistakes to Avoid**
- ❌ Forgetting about space complexity
- ❌ Not considering worst-case scenarios
- ❌ Including constants in Big O
- ❌ Confusing average-case with worst-case

### **4. Red Flags for Inefficiency**
- Nested loops over same data
- Recursive functions that solve same subproblems multiple times
- Creating new data structures unnecessarily

---

## 📝 Practice Exercise

**Before moving to the coding problems, analyze these functions:**

```python
# Function A
def mystery_function_a(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            result.append(arr[i])
    return result

# Function B  
def mystery_function_b(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Function C
def mystery_function_c(n):
    if n <= 1:
        return 1
    return mystery_function_c(n//2) + mystery_function_c(n//2)
```

**Your turn:** Try to determine the time and space complexity of each function before checking the answers below.

<details>
<summary>🔍 Click to reveal answers</summary>

**Function A**: 
- Time: O(n) - single loop through array
- Space: O(n) - worst case, all elements are even

**Function B**: 
- Time: O(n²) - nested loops (selection sort)
- Space: O(1) - in-place sorting

**Function C**: 
- Time: O(n) - T(n) = 2T(n/2) + O(1), but this simplifies to O(n)
- Space: O(log n) - recursion depth

</details>

---

## 🚀 Next Steps

1. **📖 Read this lesson thoroughly**
2. **🧪 Practice with the examples above**
3. **💻 Move to `big_o_examples_with_solutions.py`**
4. **🎯 Solve `big_o_practice_problems.py`**
5. **📝 Update your progress tracker**

---

## 📚 Additional Resources

- **Visualizations**: [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- **Interactive**: Try [VisuAlgo](https://visualgo.net/) for algorithm visualization
- **Practice**: [LeetCode Time Complexity](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4725/)

---

**Remember**: Big O analysis is a skill that improves with practice. Don't worry if it feels confusing at first - it will become natural as you solve more problems! 🌟
