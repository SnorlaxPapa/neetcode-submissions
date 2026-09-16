class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        check if len(hand) % groupSize == 0
        if its not, prune early

        sort array in groupSize
        we create a frequency map of each character in ascending order 
        iterate through frequency map, decrementing everytime we encounter a valid number
        if invalid, skip
        increment group size everytime we hit

        O(n) space for the frequency map, O(nlogn) for the sort
        """

        hand.sort()
        freq = {}
        total_count = 0
        for num in hand:
            freq[num] = freq.get(num, 0) + 1
            total_count += 1

        while total_count != 0: 
            prev_num = None
            curr_size = 0
            for num, count in freq.items():
                #used all occurences
                if count == 0:
                    if curr_size != 0: return False #next number not avail, in middle of group
                    else: continue #new set, skip this number

                #initialize new
                if not prev_num:
                    prev_num = num
                    curr_size += 1
                
                #invalid combination
                elif num - prev_num > 1: return False
                #valid combination
                elif num - prev_num == 1:
                    curr_size += 1
                    prev_num = num
                total_count -= 1
                freq[num] -= 1

                if curr_size == groupSize:
                    break

            if curr_size != groupSize: return False

        return True

                
        
        


            
