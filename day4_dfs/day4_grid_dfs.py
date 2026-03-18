# 到達可能性についての問題は再帰を使う
# 再帰を使うときはsetrecursionlimitを引き上げる

import sys


sys.setrecursionlimit(10**6)


def main():
    tokens = iter(sys.stdin.read().split())

    H = int(next(tokens))
    W = int(next(tokens))

    # --- 自分の回答 ---
    grid = [next(tokens) for _ in range(H)]
    grid = [[grid[y][x] for x in range(W)] for y in range(H)]
    # ----------------

    # --- より良い書き方 ---
    grid = [list(next(tokens)) for _ in range(H)]
    # -------------------

    # print(grid)

    # queue = deque()

    num_of_cluster = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(y, x):
        grid[y][x] = '.'
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < H and 0 <= nx < W) and grid[ny][nx] == '#':
                dfs(ny, nx)

    for y in range(H):
        for x in range(W):
            # print(grid[y][x])
            if grid[y][x] == '#':
                num_of_cluster += 1
                dfs(y, x)

    print(num_of_cluster)


if __name__ == "__main__":
    main()
