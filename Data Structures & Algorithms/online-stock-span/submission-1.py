class StockSpanner:

    def __init__(self):
        # monotonically decreasing stack
        self.stack = [(float('inf'), -1)]
        self.days = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        res = self.days - self.stack[-1][1]
        self.stack.append((price, self.days))
        self.days+=1
        return res
'''
100
[(100,0)]

80
[(100,0), (80,1)] return 1-0 = 1

60
[(100,0), (80,1), (60,2)] return 2 - 1 = 1

70
[(100,0), (80,1), (60,2)] pop 60 < 70
[(100,0), (80,1)] current day 3 -1 = 2
[(100,0), (80,1), (70, 3)]

60
[(100,0), (80,1), (70, 3), (60, 4)] return 4 -3 = 1
'''

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)