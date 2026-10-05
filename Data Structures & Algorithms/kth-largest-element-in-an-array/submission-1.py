class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a plain list to act as your min-heap
        minHeap = []
        
        for n in nums:
            # Pass the list and the element into the heapq functions
            heapq.heappush(minHeap, n)
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        # Access the root element (the minimum) without removing it
        return minHeap[0]

        