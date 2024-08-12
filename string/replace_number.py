# 54. 替换数字（第八期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1064

def main():
    string = input().strip()
    result = ''
    for e in string:
        if e.isdigit():
            result += 'number'
        else:
            result += e
    print(result)

if __name__ == '__main__':
    main()