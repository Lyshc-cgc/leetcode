# 58. 区间和（第九期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1070
# https://programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html
import sys

def main():
    """
    前缀和方法
    :return:
    """
    while 1:
        try:
            n = int(sys.stdin.readline().strip())
            prefix_sum = 0  # 前缀和
            prefix_sum_res = []  # 存储各下标的前缀和
            for _ in range(n):
                number = int(sys.stdin.readline().strip())
                prefix_sum += number
                prefix_sum_res.append(prefix_sum)
            while(line := sys.stdin.readline()):
                start, end = map(int, line.strip().split())
                if start == 0:  # 注意越界问题
                    print(prefix_sum_res[end])
                else:
                    print(prefix_sum_res[end] - prefix_sum_res[start-1])
        except:
            break

if __name__ == '__main__':
    main()

