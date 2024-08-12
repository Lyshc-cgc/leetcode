# 55. 右旋字符串（第八期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1065

from typing import List


def reverse(s: List[str], start, end):
    """
    左闭右闭区间，字符串反转
    :param s:
    :param start:
    :param end:
    :return:
    """
    left, right = start, end
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def main():
    k = int(input().strip())
    string = list(input().strip())
    reverse(string, 0 , len(string) - 1)
    reverse(string, 0, k - 1)
    reverse(string, k, len(string) - 1)
    print(''.join(string))


if __name__ == '__main__':
    main()