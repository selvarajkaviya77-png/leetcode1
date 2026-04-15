class MedianFinder:
    import heapq
    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:

        # Push into the correct heaps
        if len(self.right) == 0 or num <= self.right[0]:
            heapq.heappush(self.left, -num)  # Switch polarity when pushing into the max heap
        else:
            heapq.heappush(self.right, num)


        # Balance them
        if len(self.left) > len(self.right) + 1:
            curr = -heapq.heappop(self.left)
            heapq.heappush(self.right, curr)
        elif len(self.right) > len(self.left):
            curr = heapq.heappop(self.right)
            heapq.heappush(self.left, -curr)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        # If they're the same size, that means the median is the first number of both left and right heaps divide 2
        else:
            return (-self.left[0])
        # If they are not the same size, the median is in the left heap
        # as right is always smaller if not the same size as left
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()