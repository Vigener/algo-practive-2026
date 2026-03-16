import sys
import bisect


def main():
    # 競技プログラミング必須の「高速入出力」
    # sys.stdin.readで一括読み込み
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    # 番兵(Sentinel)の配置: 両端に「ゼータい選ばれない極端な値(無限大)」を置く
    # これでidx = 0, n+1の配列外参照を物理的に消滅させる
    T = [-float('inf')] + [int(x) for x in input_data[2:2+n]] + [float('inf')]

    # if文が必要無くなる
    queries = [int(x) for x in input_data[2+n:]]

    for x in queries:
        idx = bisect.bisect_left(T, x)

        ans = min(x - T[idx-1], T[idx] - x)

        print(ans)


if __name__ == "__main__":
    main()
