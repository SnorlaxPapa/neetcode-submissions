class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        we maintain a fixed sliding window of size k
        at each step, 
        we evaluate if this window is a good candidate
        good if new right distance < old left distance
        """
        left = 0
        right = k

        while (right < len(arr)):
            distance_left = abs(x - arr[left])
            distance_nxt = abs(x - arr[right])

            if distance_nxt < distance_left:
                left += 1
                right += 1
            elif distance_nxt <= distance_left and arr[right] == arr[left]:
                left += 1
                right += 1
            else:
                break


        return arr[left: right]
