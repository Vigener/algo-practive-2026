import sys
from collections import deque


def main():
    tokens = iter(sys.stdin.read().split())

    # 1. 入力の受け取り
    try:
        R = int(next(tokens))
        C = int(next(tokens))
    except StopIteration:
        return

    grid = [next(tokens) for _ in range(R)]

    # 2. 距離を管理する2次元配列（未訪問は -1 で初期化）
    # dist[y][x] には、スタートからの最短距離が入る
    dist = [[-1] * C for _ in range(R)]

    # 3. BFSの初期設定
    queue = deque()

    # スタート地点 (y=0, x=0) をキューに入れ、距離を0にする
    queue.append((0, 0))
    dist[0][0] = 0

    # 上下左右に移動するための方向ベクトル (y, x)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 4. BFSのメインループ
    while queue:
        # キューの先頭から「現在地」を取り出す
        y, x = queue.popleft()

        # もしゴールに到達したら、その時点の距離を出力して終了
        if y == R - 1 and x == C - 1:
            print(dist[y][x])
            return
        # else:
        #     print(f"There is x = {x}, y = {y}")
        #     print(f"dist = {dist[y][x]}")

        # 上下左右の4方向を探索
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # TODO: 以下の条件をすべて満たす場合のみ、次の一歩を進める
            # 1. 新しい座標 (ny, nx) がグリッドの範囲内である (0 <= ny < R など)
            # 2. その場所が壁 ('#') ではない
            # 3. まだ訪問していない (dist[ny][nx] == -1)
            if (0 <= ny < R and 0 <= nx < C) and (grid[ny][nx] != '#') and (dist[ny][nx] == -1):
                # 条件を満たしたら：
                # - dist[ny][nx] に現在地の距離 + 1 を書き込む
                # - キューに (ny, nx) を追加する
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))

    # ゴールに到達できなかった場合
    print(-1)


if __name__ == "__main__":
    main()
