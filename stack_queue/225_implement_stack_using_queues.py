# 225. 用队列实现栈
# https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/implement-stack-using-queues/description/

class MyStack:

    def __init__(self):
        self.q0 = []
        self.q1 = []

    def get_the_empty(self):
        if not self.empty():
            if not self.q0:
                return self.q0
            elif not self.q1:
                return self.q1
        return self.q1  # 若都为空，则默认返回q1

    def get_the_not_empty(self):
        if not self.empty():
            if self.q0:
                return self.q0
            elif self.q1:
                return self.q1
        return None

    def push(self, x: int) -> None:
        q = self.get_the_not_empty()
        if not q:  # 若不存在非空队列，则默认q0
            self.q0.append(x)
        else:
            q.append(x)

    def pop(self) -> int:
        if not self.empty():
            in_q = self.get_the_not_empty()
            out_q = self.get_the_empty()
            while len(in_q) != 1:  # 除了最后一个，其他全部到另一个队列去
                out_q.append(in_q.pop(0))
            return in_q.pop(0)

        return None

    def top(self) -> int:
        if not self.empty():
            res = self.pop()
            self.push(res)
            return res
        return None

    def empty(self) -> bool:
        if not self.q0 and not self.q1:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()