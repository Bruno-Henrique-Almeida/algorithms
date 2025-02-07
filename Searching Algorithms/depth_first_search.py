import logging
from typing import Optional, Set, List, Dict

logging.basicConfig(level=logging.INFO)


def dfs(graph: Dict[str, List[str]],
        node: str,
        visited: Optional[Set[str]] = None,
        path: Optional[List[str]] = None) -> List[str]:
    '''
    Performs a Deapth-First Search (DFS) on a graph starting from a given node.

    Args:
        graph (Dict[str, List[str]]): The graph represented as a adjacency list.
        node (str): The stating node for the DFS traversal.
        visited (Optional[Set[str]]): A set to track visited nodes. Defaults to None.
        path (Optional[List[str]]): A list to store the traversal path. Defaults to None.
    Returns:
        List[str]: A list representing the DFS traversal path.
    '''

    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path


def dfs_iterative(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    '''
    Performs an iterative Depth-First Search (DFS) on a graph starting from a given node.

    Args:
        graph (Dict[str, List[str]]): The graph represented as an adjacency list.
        start_node (str): The starting node for the DFS traversal.
    Returns:
        List[str]: A list representing the DFS traversal path.
    '''

    visited: Set[str] = set()
    stack: List[str] = [start_node]
    path: List[str] = []

    while stack:
        current_node: str = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            path.append(current_node)
            stack.extend(reversed(graph[current_node]))
    return path


def main():
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': ['A'],
        'D': ['A', 'G'],
        'E': ['B'],
        'F': ['B', 'H'],
        'G': ['D'],
        'H': ['F']
    }

    node: str = 'A'
    result_dfs: List[str] = dfs(graph, node=node)
    logging.info('DFS Search result: %s', result_dfs)

    result_dfs_iterative: List[str] = dfs_iterative(graph=graph, start_node=node)
    logging.info('DFS Iteratve Search result: %s', result_dfs_iterative)


if __name__ == '__main__':
    main()
