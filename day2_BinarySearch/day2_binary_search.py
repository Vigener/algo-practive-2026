import bisect


def main():
    # 入力受け取り (テスト用に直接代入でも可、標準入力でも可)
    N, Q = 5, 3
    A = [16, 32, 64, 128, 256]
    queries = [32, 100, 300]

    for x in queries:
        # bisect_left(A, x) は、「配列Aの中で、x を挿入すべき一番左のインデックス」を O(log N) で返します。
        # 例: bisect_left(A, 32) は 1 (インデックス1の場所) を返します。
        # 例: bisect_left(A, 100) は 3 (インデックス3の場所) を返します。

        idx = bisect.bisect_left(A, x)

        # TODO: idx を使って、「条件を満たすノードの数(ans)」を計算してください。
        # ヒント: 全体の台数 N から、条件を満たさない台数（インデックス番号そのもの）を引けば...？
        ans = N - idx

        print(ans)


if __name__ == "__main__":
    main()
