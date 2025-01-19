from typing import List
import logging


logging.basicConfig(level=logging.INFO)


def merge_sort(arr: List[int]) -> List[int]:
    '''
    Sorts a list of integers using the Merge Sort algorithm.

    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    '''

    if len(arr) <= 1:
        return arr

    mid: int = len(arr) // 2
    left_half: List[int] = merge_sort(arr[:mid])
    right_half: List[int] = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left_half: List[int], right_half: List[int]) -> List[int]:
    '''
    Merges two sorted lists into a single sorted list.

    Args:
        left_half (List[int]): The first sorted list.
        right_half (List[int]): The second sorted list.
    Returns:
        List[int]: The merged and sorted list.
    '''

    merged: List[int] = []

    i: int = 0
    x: int = 0

    while i < len(left_half) and x < len(right_half):
        if left_half[i] < right_half[x]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[x])
            x += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[x:])
    return merged


def main():
    input: List[int] = [34, 67, 23, 89, 90, 12, 11, 56, 76, 45, 38, 29, 78, 65,
                        92, 10, 7, 3, 88, 21, 40, 32, 60, 70, 80, 17, 50, 49,
                        37, 81, 22, 36, 25, 91, 5, 19, 26, 33, 55, 72]

    merge_sort_result: List[int] = merge_sort(input)

    logging.info(merge_sort_result)


if __name__ == '__main__':
    main()
