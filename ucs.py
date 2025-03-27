import csv
edgeFile = 'edges.csv'
import heapq
from bfs import load_edges

def ucs(start, end):
    # Begin your code (Part 3)
    # raise NotImplementedError("To be implemented")
    edges = load_edges()
    # edges = {
    #     0:{1:3, 3:2},
    #     1:{0:3, 4:2},
    #     2:{3:6, 4:2},
    #     3:{0:2, 2:6},
    #     4:{1:2, 2:2}
    # }
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    explored = []
    while priority_queue:
        dist, node, path = heapq.heappop(priority_queue)
        # 如果dist最小的结点是end，则找到了最短路径
        if node == end:
            return path, dist, len(explored) + 1
        if node in explored:
            continue
        explored.append(node)
        if node not in list(edges.keys()):
            continue
        for neighbour_node in list(edges[node].keys()):
            if neighbour_node not in explored:
                if neighbour_node not in [i[1] for i in priority_queue]:
                    # 如果邻居结点不在表中中，则加入其路径信息
                    heapq.heappush(priority_queue, (dist + edges[node][neighbour_node], neighbour_node, path + [neighbour_node]))
                else:
                    for i in range(len(priority_queue)):
                        if priority_queue[i][1] == neighbour_node:
                            if dist + edges[node][neighbour_node] < priority_queue[i][0]:
                                # 路程更短，则更新路径
                                priority_queue[i] = (dist + edges[node][neighbour_node], neighbour_node, path + [neighbour_node])
                                heapq.heapify(priority_queue)
                            break
    return [], 0.0, len(explored)
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    # path, dist, num_visited = ucs(0,2)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
