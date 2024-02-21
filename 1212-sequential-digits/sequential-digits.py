class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        def add(current,low,high):
            print(current)
            if int(current) >= int(low) and int(current) <= int(high):
                answer.append(int(current))
            if len(current) < len(high) and (current[-1] != "9"):
                current = current + str(1+ int(current[-1]))
                add(current,low,high)

        low = str(low)
        high = str(high)
        for current in range(1,10):
            add(str(current),low,high)
        return sorted(answer)