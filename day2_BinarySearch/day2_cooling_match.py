import bisect


def main():
    n, q = map(int, input().split())
    T = list(map(int, input().split()))
    for i in range(q):
        x = int(input())

        idx = bisect.bisect_left(T, x)

        # [10 20 30]
        # 18: idx = 1
        # 26: idx = 2
        # 5: idx = 0
        # 40: idx = 3

        if idx == 0:
            ans = abs(T[idx] - x)
        elif idx == n:
            ans = abs(T[idx-1]-x)
        else:
            ans = min(abs(x-T[idx-1]), abs(x-T[idx]))

        print(ans)


if __name__ == "__main__":
    main()
