import math
import sys


def main():
    tokens = iter(sys.stdin.read().split())

    N = int(next(tokens))

    P = [int(next(tokens)) for _ in range(N)]

    # ミス
    # dp = [math.inf] * N

    if N == 1:
        print(P[0])
        return

    # 最大値問題なので、 0で初期化すべき
    dp = [0] * N

    dp[0] = P[0]

    dp[1] = max(P[0], P[1])

    for i in range(2, N):
        dp[i] = max(
            dp[i-1],
            dp[i-2] + P[i]
        )

    print(dp[N-1])


if __name__ == "__main__":
    main()
