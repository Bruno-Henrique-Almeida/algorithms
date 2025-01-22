from typing import List
import logging

logging.basicConfig(level=logging.INFO)


def heapify(arr: List[int], n: int, i: int) -> None:
    '''
    Ensures the subtree rooted at index 1 satifies the max-heap property.

    Args:
        arr (List[int]): The list representing the heap.
        n (int): The size of the heap.
        i (int): The index of the current root node.
    Returns:
        one: The list is modified in place.
    '''

    largest: int = i
    left: int = 2 * i + 1
    right: int = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]):
    '''
    Sorts a list in ascending order using the Heap Sort algorithm.

    Args:
        arr (List[int]): The list of elements to sort.
    Returns:
        list[int]: The sorted list in ascending order.
    '''

    n: int = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def main():
    input_data: List[int] = [
        34, 67, 23, 89, 90, 12, 11, 56, 76, 45, 38, 29, 78, 65,
        92, 10, 7, 3, 88, 21, 40, 32, 60, 70, 80, 17, 50, 49,
        37, 81, 22, 36, 25, 91, 5, 19, 26, 33, 55, 72
    ]

    result: List[int] = heap_sort(arr=input_data)

    logging.info('Heap Sort result: %s', result)


if __name__ == '__main__':
    main()
