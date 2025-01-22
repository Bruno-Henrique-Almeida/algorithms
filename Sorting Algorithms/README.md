# Sorting Algorithms

This folder contains different sorting algorithms implemented in Python.
Sorting algorithms are used to arrange data in a specific order, such as ascending or descending.

---

### **Comparison Graph**  
Imagine an input with 10 elements, 100 elements, and 1000 elements:

| Complexity | 10 elements   | 100 elements   | 1000 elements     |
|------------|---------------|----------------|-------------------|
| O(1)       | 1 operation   | 1 operation    | 1 operation       |
| O(log n)   | ~3 operations | ~7 operations  | ~10 operations    |
| O(n)       | 10 operations | 100 operations | 1000 operations   |
| O(n log n) | ~30 operations| ~700 operations| ~10,000 operations|
| O(n²)      | 100 operations| 10,000 operations | 1,000,000 operations |

## Available Algorithms

1. **Bubble Sort**
   - Time Complexity: O(n²) | **Quadratic**. The running time grows proportionally to the square of the input size. It is inefficient for large inputs but may be acceptable for small datasets.
   - Space Complexity: O(1) | **Constant**. The algorithm uses a fixed amount of additional memory, regardless of the input size. This ensures better performance in terms of memory usage, as it does not grow with the size of the input.

2. **Merge Sort**
   - Time complexity: O(n log n) | **Nearly linear**. The running time grows proportionally to the size of the input multiplied by the logarithm of the input size. This complexity is common in algorithms that divide the input into smaller parts, solve them independently, and combine the results.
   - Space complexity: O(n)      | **Linear**. The algorithm's memory usage grows linearly with the size of the input. This means the amount of additional memory required is proportional to the input size. Common examples include algorithms that store all elements in a new data structure, such as recursive algorithms or those using auxiliary arrays.

3. **Quick Sort**
   - Time complexity: O(n log n) | **Nearly linear**.
   - Space complexity: O(log n)  | **Logarithmic**. The memory usage grows logarithmically with the size of the input. This typically occurs in divde-and-conquer algorithms, where the input is repeatedly divided into smaller parts, and only a small amount of memory is required for each division. A common example is recursive algorithms like Binary Search, where the recursion depth is proportional.

4. **Heap Sort**
   - Time complexity: O(n log n) | **Nearly linear**.
   - Space complexity: O(1)      | **Constant**.
