def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    # ans = -float('inf')
    # for i in range(N - K + 1):
    #     tmp_sum = S[i + K] - S[i]
    #     ans = max(ans, tmp_sum)

    ans = max(S[i + K] - S[i] for i in range(N - K + 1))

    print(ans)


if __name__ == "__main__":
    main()
