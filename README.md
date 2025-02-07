# Algorithms

This repository contains implementations of various algorithms in Python, organized into folders:
- **Sorting Algorithms**: Algorithms that arrange data in a specific order (Quick Sort, Merge Sort, Bubble Sort, Heap Sort).
- **Searching Algorithms**: Algorithms that search for elements within a dataset (Linear Search, Binary Search, Depth-first Search, Breadth-first Search).

---

### **Comparison Graph**  
Imagine an input with 10 elements, 100 elements, and 1000 elements:

| Complexity   | 10 elements    | 100 elements   | 1000 elements      |
|--------------|----------------|----------------|--------------------|
| **O(1)**     | 1 operation    | 1 operation    | 1 operation        |
| **O(log n)** | ~3 operations  | ~7 operations  | ~10 operations     |
| **O(n)**     | 10 operations  | 100 operations | 1000 operations    |
| **O(n log n)** | ~30 operations | ~700 operations | ~10,000 operations |
| **O(n²)**    | 100 operations | 10,000 operations | 1,000,000 operations |

---

## Sorting Algorithms

This folder contains different sorting algorithms implemented in Python.
Sorting algorithms are used to arrange data in a specific order, such as ascending or descending.

### Available Algorithms

1. **Bubble Sort**
   - **Time Complexity**: O(n²) | **Quadratic**. The running time grows proportionally to the square of the input size. It is inefficient for large inputs but may be acceptable for small datasets.
   - **Space Complexity**: O(1) | **Constant**. The algorithm uses a fixed amount of additional memory regardless of the input size.

2. **Merge Sort**
   - **Time Complexity**: O(n log n) | **Nearly linear**. The running time grows proportionally to the size of the input multiplied by the logarithm of the input size.
   - **Space Complexity**: O(n) | **Linear**. The algorithm's memory usage grows linearly with the size of the input due to auxiliary arrays used in the merging process.

3. **Quick Sort**
   - **Time Complexity**: O(n log n) | **Nearly linear** (on average; worst-case is O(n²) if poor pivot choices are made).
   - **Space Complexity**: O(log n) | **Logarithmic**. The algorithm uses additional memory for the recursion stack, which grows logarithmically with the input size.

4. **Heap Sort**
   - **Time Complexity**: O(n log n) | **Nearly linear**.
   - **Space Complexity**: O(1) | **Constant**. Heap Sort is performed in-place without requiring additional memory.

---

## Searching Algorithms

This folder contains different searching algorithms implemented in Python.
Searching algorithms are used to locate a specific element or determine its absence within a collection of data.

### Available Algorithms

1. **Linear Search**
   - **Description**: Iterates through each element in the dataset until the target element is found or the end of the dataset is reached.
   - **Time Complexity**: O(n) | **Linear**. The time taken increases linearly with the size of the dataset.
   - **Space Complexity**: O(1) | **Constant**. Only a fixed amount of additional memory is required.

2. **Binary Search**
   - **Description**: Works on sorted datasets by repeatedly dividing the search interval in half until the target element is found.
   - **Time Complexity**: O(log n) | **Logarithmic**. Highly efficient for large, sorted datasets.
   - **Space Complexity**: O(1) | **Constant** for the iterative version.

3. **Depth-first Search (DFS)**
   - **Description**: Explores as far as possible along each branch before backtracking. Commonly used in tree or graph traversals.
   - **Time Complexity**: O(V + E) | where V is the number of vertices and E is the number of edges (in graphs).
   - **Space Complexity**: O(V) | **Linear** in the worst case, due to the recursion stack or explicit stack used.

4. **Breadth-first Search (BFS)**
   - **Description**: Explores all neighbor nodes at the present depth before moving on to nodes at the next depth level.
   - **Time Complexity**: O(V + E) | where V is the number of vertices and E is the number of edges.
   - **Space Complexity**: O(V) | **Linear**. Requires additional memory to store the nodes at each level in a queue.

---
