import heapq

class MedianFinder:

    def __init__(self):
        # small: Max-Heap (stores smaller half, store negative values)
        # large: Min-Heap (stores larger half)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Default push to max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Handle size balance (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd number of total elements: top of small is median
        if len(self.small) > len(self.large):
            return float(-self.small[0])
            
        # Even number of elements: average of both tops
        return (-self.small[0] + self.large[0]) / 2.0