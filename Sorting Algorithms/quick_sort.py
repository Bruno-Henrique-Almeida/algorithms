import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def quick_sort(arr: List[int]) -> List[int]:
    '''
    Sorts a list of integers using the Quick Sort algorithm.

    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    '''

    if len(arr) <= 1:
        return arr
    else:
        mid: int = len(arr) // 2
        pivot: int = arr[mid]

        left_half: List[int] = [x for x in arr if x < pivot]
        right_half: List[int] = [x for x in arr if x > pivot]

    return quick_sort(left_half) + [pivot] + quick_sort(right_half)


def main():
    input_data: List[int] = [
        34, 67, 23, 89, 90, 12, 11, 56, 76, 45, 38, 29, 78, 65,
        92, 10, 7, 3, 88, 21, 40, 32, 60, 70, 80, 17, 50, 49,
        37, 81, 22, 36, 25, 91, 5, 19, 26, 33, 55, 72
    ]

    result = quick_sort(arr=input_data)

    logging.info('Quick Sort result: %s', result)


if __name__ == '__main__':
    main()
