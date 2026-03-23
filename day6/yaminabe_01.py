import sys


def main():
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    Q = int(next(tokens))
    P = list(int(next(tokens)) for _ in range(N))
    # print(P)

    S = [0] * (N+1)  # 0ではなく1に1番目を入れる
    for i in range(N):
        S[i+1] = S[i] + P[i]

    for i in range(Q):
        L, R = int(next(tokens)), int(next(tokens))

        ans = S[R] - S[L - 1]

        print(ans)


if __name__ == "__main__":
    main()
