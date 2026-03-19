import sys
import math


def main():
    tokens = iter(sys.stdin.read().split())

    try:
        N = int(next(tokens))
    except StopIteration:
        return

    H = [int(next(tokens)) for _ in range(N)]

    # 1. DP配列の初期化（すべて無限大で埋める）
    dp = [math.inf] * N

    # 2. 初期値の設定
    dp[0] = 0
    if N > 1:
        dp[1] = abs(H[1] - H[0])

    # 3. 漸化式を回す（i = 2 から N-1 まで）
    for i in range(2, N):
        # TODO: dp[i-1] から来た場合のコストと、dp[i-2] から来た場合のコストを比較し、
        # 小さい方（min）を dp[i] に代入する。
        # ヒント: dp[i-1] + abs(...)
        dp[i] = min(
            dp[i-2] + abs(H[i-2] - H[i]),
            dp[i-1] + abs(H[i-1] - H[i])
        )

    # ゴール（N-1番目）の最小コストを出力
    print(dp[N - 1])


if __name__ == "__main__":
    main()
