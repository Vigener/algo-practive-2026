from ast import Try
from collections import deque
import math
import sys


def main():
    tokens = iter(sys.stdin.read().split())

    N = int(next(tokens))
    M = int(next(tokens))

    # 今回は「自分と繋がっているノードのリスト」を事前に作る必要があります。

    # ノード番号をそのままインデックスとして使うため、N+1個の空リストを用意する
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u = int(next(tokens))
        v = int(next(tokens))
        graph[u].append(v)
        graph[v].append(u)

    dist = [math.inf] * (N+1)
    # print(dist)

    queue = deque()

    queue.append(1)
    dist[1] = 0

    # queueに入っているのは、まだ探索する必要があるノードのキュー
    while queue:
        current_node = queue.popleft()
        # print(f"current_node is {current_node}")

        if current_node == N:
            print(dist[current_node])
            return

        for next_node in graph[current_node]:
            # if dist[next_node] != -1 and dist[next_node] > dist[current_node] + 1:
            if dist[next_node] > dist[current_node] + 1:
                dist[next_node] = dist[current_node] + 1
                queue.append(next_node)

    print(-1)


if __name__ == "__main__":
    main()
