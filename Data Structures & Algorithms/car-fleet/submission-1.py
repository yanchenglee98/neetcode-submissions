class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = sorted([(position[i], speed[i]) for i in range(len(speed))], reverse=True)
        time = [(target-temp[i][0]) / temp[i][1] for i in range(len(speed))]
        stack = [time[0]]
        for i in range(1, len(speed)):
            if stack[-1] < time[i]:
                stack.append(time[i])
        return len(stack)
        