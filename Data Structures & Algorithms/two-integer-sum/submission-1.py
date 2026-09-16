class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positionMap = {}

        for index, value in enumerate (nums):
            if positionMap.get(value) == None:
                positionMap[value] = [index]
            else:
                positionMap[value].append(index)
            

        for index, num in enumerate(nums):
            complementary = target - num

            if positionMap.get(complementary) != None:
                if complementary != num:
                    firstIndex = positionMap[complementary][0]
                    return sorted([firstIndex, index])
                
                if len(positionMap[num]) > 1:
                    return positionMap[num][:2]


# iterate through the array
# we create a hashmap of the key being the number, and the value being the list of its indexes
# then we iterate through the array again, and we calculate the complementary value for num + com = target
# we lookup the comp value in the hashmap, if it exists, we verify that it is not the same index. if not same inddex, then we return the sorted indexes. if it is the only available index is the same as the lookup, then we proceed with the search