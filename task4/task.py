from collections import deque

# ─── Graph definition (adjacency list) ───────────────────────────────────────
# Represents an undirected graph with nodes A–H
GRAPH = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['D'],
    'H': ['E'],
}

# ─── BFS ─────────────────────────────────────────────────────────────────────
def bfs(graph, start, goal):
    """
    Breadth-First Search: explores nodes level by level.
    Uses a queue (FIFO). Finds the SHORTEST path.

    Args:
        graph: adjacency list dict
        start: starting node label
        goal:  target node label
    Returns:
        path as a list of nodes, or None if no path exists
    """
    # Queue stores (current_node, path_taken_so_far)
    queue = deque([(start, [start])])
    visited = set([start])

    print(f"\n── BFS: {start} → {goal} ──")
    print(f"  Initial queue: [{start}]")

    while queue:
        node, path = queue.popleft()  # Take from front (FIFO)
        print(f"  Exploring: {node}  |  Path so far: {' → '.join(path)}")

        if node == goal:
            print(f"  ✓ Goal reached!")
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    print("  ✗ No path found.")
    return None

# ─── DFS ─────────────────────────────────────────────────────────────────────
def dfs(graph, start, goal, path=None, visited=None, depth=0):
    """
    Depth-First Search: explores as deep as possible before backtracking.
    Uses recursion (implicit call stack). Does NOT guarantee shortest path.

    Args:
        graph:   adjacency list dict
        start:   current node being explored
        goal:    target node label
        path:    accumulated path (list of nodes)
        visited: set of already-visited nodes
        depth:   current recursion depth (for display)
    Returns:
        path as a list of nodes, or None if no path exists
    """
    if path is None:
        path = [start]
        visited = set([start])
        print(f"\n── DFS: {start} → {goal} ──")

    indent = "  " + "  " * depth
    print(f"{indent}Visiting: {start}  |  Path: {' → '.join(path)}")

    if start == goal:
        print(f"{indent}✓ Goal reached!")
        return path

    for neighbour in graph[start]:
        if neighbour not in visited:
            visited.add(neighbour)
            result = dfs(graph, neighbour, goal, path + [neighbour], visited, depth + 1)
            if result:
                return result
            print(f"{indent}  ↩️ Backtracking from {neighbour}")

    return None

# ─── Run both searches ────────────────────────────────────────────────────────
if __name__ == "__main__":
    START = 'A'
    GOAL  = 'H'

    bfs_path = bfs(GRAPH, START, GOAL)
    dfs_path = dfs(GRAPH, START, GOAL)

    print("\n═══ Results ═══")
    print(f"BFS path (shortest): {' → '.join(bfs_path) if bfs_path else 'Not found'}")
    print(f"DFS path (first found): {' → '.join(dfs_path) if dfs_path else 'Not found'}")