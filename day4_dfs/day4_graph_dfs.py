import sys

# 【重要】Pythonの再帰上限を解放する（100万回に設定）
sys.setrecursionlimit(10**6)


def main():
    tokens = iter(sys.stdin.read().split())

    try:
        N = int(next(tokens))
        M = int(next(tokens))
        X = int(next(tokens))
    except StopIteration:
        return

    # 1. 隣接リストの構築（昨日のBFSと全く同じ！）
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(tokens))
        v = int(next(tokens))
        graph[u].append(v)
        graph[v].append(u)

    # 2. 訪問済みかどうかの管理リスト（False で初期化）
    # 距離は必要なく、「行ったか/行ってないか」だけでよい
    visited = [False] * (N + 1)

    # 3. 再帰関数 DFS の定義
    def dfs(current_node):
        # 現在のノードを「訪問済み」にする
        visited[current_node] = True

        # 隣接するノードを順番に見ていく
        for next_node in graph[current_node]:
            # TODO: もし next_node がまだ訪問されていない (visited が False) なら、
            # その next_node に向かってさらに dfs を呼び出す（再帰）
            # if visited[next_node] == False:
            # 以下の書き方のほうがいい
            if not visited[next_node]:
                dfs(next_node)

    # 4. スタート地点（ノード1）からDFSを開始！
    dfs(1)

    # 5. 探索終了後、目的のノードXが訪問済み(True)になっているかチェック
    if visited[X]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
