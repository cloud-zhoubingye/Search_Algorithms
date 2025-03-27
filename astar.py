import csv
from bfs import load_edges
import heapq
import csv


def load_heuristics(end: int):
    heuristics = {}
    with open("heuristic_values.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            heuristics[int(row["node"])] = float(row[f"{end}"])
    return heuristics


def astar(start, end):
    # Begin your code (Part 4)
    # raise NotImplementedError("To be implemented")
    edges = load_edges()
    heuristics = load_heuristics(end)
    opened = []
    closed = []
    heapq.heappush(opened, (heuristics[start], start, [start]))
    while opened:
        current_fn, current_node, current_path = heapq.heappop(opened)
        if current_node == end:
            return current_path, current_fn, len(closed) + 1
        if current_node not in closed:
            closed.append(current_node)
            # 对每个邻居结点
            if current_node not in list(edges.keys()):
                continue
            for neighbour_node in list(edges[current_node].keys()):
                if neighbour_node not in closed:
                    new_fn = (
                        current_fn
                        - heuristics[current_node]
                        + edges[current_node][neighbour_node]
                        + heuristics[neighbour_node]
                    )
                    new_path = current_path + [neighbour_node]
                    # 将邻居结点加入opened中
                    if neighbour_node not in [_[1] for _ in opened]:
                        heapq.heappush(opened, (new_fn, neighbour_node, new_path))
                    # 更新opened中的邻居结点的路径信息
                    else:
                        for i in range(len(opened)):
                            if opened[i][1] == neighbour_node:
                                # 新路径更好，则更新
                                if new_fn < opened[i][0]:
                                    opened[i] = (
                                        new_fn,
                                        neighbour_node,
                                        new_path,
                                    )
                                    heapq.heapify(opened)
                                break
    return [], 0.0, len(closed)
    # End your code (Part 4)


if __name__ == "__main__":
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f"The number of path nodes: {len(path)}")
    print(f"Total distance of path: {dist:.3f}")
    print(f"The number of visited nodes: {num_visited}")
