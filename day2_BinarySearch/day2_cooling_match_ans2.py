import math
import sys
import bisect


def main():
    # tokens: 「複数の単語が入った箱」のイメージ
    tokens = iter(sys.stdin.read().split())

    n = int(next(tokens))
    q = int(next(tokens))

    T = [- math.inf] + [int(next(tokens)) for _ in range(n)] + [math.inf]

    for _ in range(q):
        x = int(next(tokens))
        idx = bisect.bisect_left(T, x)
        ans = min(
            x - T[idx-1],
            T[idx] - x
        )
        print(ans)


if __name__ == "__main__":
    main()
