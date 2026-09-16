import heapq

class Solution:
    def get_distance(self, coord):
        x1, y1 = coord

        return x1 ** 2 + y1 ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        k closest so we maintain a k-sized max heap. 
        structure of the max heap is saved as (-distance, ([x1, y1], [x2,y2]))

        intuitively, we need to calculate the distance between each and every point which is O(n^2).
        this distance will be pushed to the heap which will take O(n) space where each insertion is O(logn)
        """

        result = []
        heapq.heapify(result)

        for point in points:
            distance = -1 * self.get_distance(point)
            heapq.heappush(result, (distance, point))

            if len(result) > k:
                heapq.heappop(result)
            
        result = [point[1] for point in result]

        return result

        