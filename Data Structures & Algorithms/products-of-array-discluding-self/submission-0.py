class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            passed in an array of integers
            first naive solution is to iterate through array once and get multiplication
            iterate again to get product without nums[i]

            to do it in O(n) time without using divison, 
            we consider 
            [2, 3, 4] for nums, product = 24
            [12, 8, 6] = [3*4, 2*4, 2*3]
            We could create a hashmap with keys [1: i] and [i+1:] as we iterate down the array
            simultaenously we can iterate backwards from the array to calculate [i+1:len(nums)]
            so for [2, 3, 4], it looks like {"0:1": 2, "0:2": 6}
            then {"2:": 4, "1:": 12}
            then we can iterate through the array again and calculate the product by multipying [1: i] with [i+1:]
            O(n) time complexity

            nums min length is 2 so no need to consider edge case when len(nums)==1
            """
            
        productMap = {}
        reverseIndex = -1
        lengthNums = len(nums)

        for index, num in enumerate(nums):
            if index == 0:
                continue

            prefixKey = f"0:{index}"
            reverseKey = f"{lengthNums+reverseIndex}:{lengthNums}"

            if index == 1 and reverseIndex == -1:
                productMap[prefixKey] = nums[0]
                productMap[reverseKey] = nums[-1]
            else:
                prevPrefixKey = f"0:{index-1}"
                productMap[prefixKey] = productMap[prevPrefixKey] * nums[index-1]

                prevReverseKey = f"{lengthNums+reverseIndex+1}:{lengthNums}" 
                productMap[reverseKey] = productMap[prevReverseKey] * nums[reverseIndex]
            
            reverseIndex-=1

        print(productMap)
        answer = []

        length = len(nums)
        for index, num in enumerate(nums):
            if index == 0:
                answer.append(productMap[f"1:{length}"])
            elif index == length - 1:
                answer.append(productMap[f"0:{index}"])
            else:
                answer.append(productMap[f"0:{index}"] * productMap[f"{index+1}:{length}"])
        
        return answer
        
                
            

