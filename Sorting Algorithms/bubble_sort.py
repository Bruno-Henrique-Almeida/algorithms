import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def bubble_sort(arr: List[int]) -> List[int]:
    '''
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Args:
        arr (List[int]): The list of elements to sort.
    Returns:
        list[int]: The sorted list in ascending order.
    '''

    n: int = len(arr)

    for i in range(n):
        swapped: bool = False
        for x in range(0, n - i - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                swapped: bool = True

        if not swapped:
            break
    return arr


def main():
    input_data: List[int] = [
        34, 67, 23, 89, 90, 12, 11, 56, 76, 45, 38, 29, 78, 65,
        92, 10, 7, 3, 88, 21, 40, 32, 60, 70, 80, 17, 50, 49,
        37, 81, 22, 36, 25, 91, 5, 19, 26, 33, 55, 72
    ]
    result: List[int] = bubble_sort(arr=input_data)

    logging.info('Bubble Sort result: %s', result)


if __name__ == '__main__':
    main()
