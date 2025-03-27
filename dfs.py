import csv

edgeFile = "edges.csv"
from bfs import load_edges


def dfs(start, end):
    # Begin your code (Part 2)
    edges = load_edges()
    stack = [(start, 0.0, [])]
    visited = set()
    num_visited = 0

    while stack:
        current_node, current_dist, current_path = stack.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        num_visited += 1
        path = current_path + [current_node]
        # 到达终点
        if current_node == end:
            return path, current_dist, num_visited
        if current_node not in edges:
            continue
        # 将邻居结点压入栈中
        for neighbor in list(edges[current_node].keys()):
            if neighbor not in visited:
                new_dist = current_dist + edges[current_node][neighbor]
                stack.append((neighbor, new_dist, path))

    return [], 0.0, num_visited
    # End your code (Part 2)


if __name__ == "__main__":
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f"The number of path nodes: {len(path)}")
    print(f"Total distance of path: {dist:.3f}")
    print(f"The number of visited nodes: {num_visited}")
