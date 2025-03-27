import queue
import csv

edgeFile = "edges.csv"


# 加载结点间的距离
def load_edges():
    edges = {}
    with open(edgeFile, "r") as f:
        reader = csv.reader(f)
        next(reader)  # 跳过第一行表头
        for row in reader:
            node1, node2, dist = row
            node1, node2, dist = int(node1), int(node2), float(dist)
            # 从node1到node2的距离
            if node1 not in edges:
                edges[node1] = {}
            edges[node1][node2] = dist
    return edges


def bfs(start, end):
    # Begin your code (Part 1)
    # raise NotImplementedError("To be implemented")
    edges = load_edges()
    bfs_queue = queue.Queue()
    bfs_queue.put((start, 0.0, [start]))
    visited_nodes = set()

    while not bfs_queue.empty():
        current_node, current_dist, current_path_list = bfs_queue.get()
        visited_nodes.add(current_node)
        # print(f'>>> bfs: visiting node {current_node}, distance {current_dist}')
        # 到达终点，退出循环
        if current_node == end:
            return current_path_list, current_dist, len(visited_nodes)
        # 加入当前节点的邻居结点
        if current_node not in list(edges.keys()):
            continue
        neighbor_nodes = list(edges[current_node].keys())
        for neighbor_node in neighbor_nodes:
            if neighbor_node not in visited_nodes:
                new_dist = current_dist + edges[current_node][neighbor_node]
                new_path_list = current_path_list + [neighbor_node]
                bfs_queue.put((neighbor_node, new_dist, new_path_list))
    return [], 0.0, len(visited_nodes)
    # End your code (Part 1)


if __name__ == "__main__":
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f"The number of path nodes: {len(path)}")
    print(f"Total distance of path: {dist:.3f}")
    print(f"The number of visited nodes: {num_visited}")
