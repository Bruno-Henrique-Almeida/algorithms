import logging
from collections import deque
from typing import Dict, List, Set

logging.basicConfig(level=logging.INFO)


def bfs(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    '''
    Perform a breadth-first search on the graph starting from the given node.

    Args:
        graph (Dict[str, List[str]]): The graph represented as an adjacency list.
        start_node (str): The node to start the BFS from.
    Returns:
        List[str]: List of nodes in the order they were visited.
    '''

    visited: Set[str] = {start_node}
    queue: deque[str] = deque([start_node])
    order: List[str] = []

    visited.add(start_node)
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'D': ['A', 'G'],
        'C': ['A'],
        'E': ['B'],
        'F': ['B', 'H'],
        'H': ['F'],
        'G': ['D']
    }

    node: str = 'A'
    result_bfs: List[str] = bfs(graph, start_node=node)
    logging.info('BFS Search result: %s', result_bfs)


if __name__ == '__main__':
    main()
