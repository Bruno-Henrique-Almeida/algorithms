import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def binary_search(arr: List[int], target: int) -> str:
    '''
    Performs a Binary search in a list to find the target value.

    Args:
        arr (List[int]): List of integers where the search will be performed.
        target (int): The value to search for.
    Returns:
        str: A message indicating whether the value was found and its position,
        or that the value was not found.
    '''

    low, high = 0, len(arr) - 1

    while low <= high:
        mid: int = low + (high - low) // 2

        if arr[mid] == target:
            return f'Value {target} found at index {arr.index(mid)}'

        if arr[mid] < target:
            low: int = mid + 1
        else:
            high: int = mid - 1

    return 'Value {target} not found'


def main():
    input_data: List[int] = [
        34, 67, 23, 89, 90, 12, 11, 56, 76, 45, 38, 29, 78, 65,
        92, 10, 7, 3, 88, 21, 40, 32, 60, 70, 80, 17, 50, 49,
        37, 81, 22, 36, 25, 91, 5, 19, 26, 33, 55, 72
    ]

    target_value: int = 60
    result: str = binary_search(arr=input_data, target=target_value)

    logging.info('Binary Search result: %s', result)


if __name__ == '__main__':
    main()
