# 232. 用栈实现队列
# https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.st_in = []
        self.st_out = []

    def push(self, x: int) -> None:
        self.st_in.append(x)

    def pop(self) -> int:
        if not self.st_out:
            while self.st_in:
                self.st_out.append(self.st_in.pop())
        return self.st_out.pop()

    def peek(self) -> int:
        res_list = []
        if not self.empty():
            res = self.pop()
            res_list.append(res)
        while not self.empty():
            res_list.append(self.pop())
        for e in res_list:
            self.push(e)

        return res

    def empty(self) -> bool:
        if not self.st_in and not self.st_out:
            return True
        return False

if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()