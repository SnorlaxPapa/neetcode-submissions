class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Enforce Pillar 1: Ensure nums1 is always the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
            
        totalLength = len(nums1) + len(nums2)
        halfTotal = (totalLength + 1) // 2
        
        # Pointers for binary search on the SMALLER array (nums1)
        left, right = 0, len(nums1)
        
        while left <= right:
            # Calculate dynamic partitions inside the loop
            partitionA = (left + right) // 2
            partitionB = halfTotal - partitionA
            
            # Pillar 3: Extract the 4 boundary elements with out-of-bounds protection
            A_left  = nums1[partitionA - 1] if partitionA > 0 else float('-inf')
            A_right = nums1[partitionA]     if partitionA < len(nums1) else float('inf')
            
            B_left  = nums2[partitionB - 1] if partitionB > 0 else float('-inf')
            B_right = nums2[partitionB]     if partitionB < len(nums2) else float('inf')
            
            # Core Check 1: Perfect Partition Found!
            if A_left <= B_right and B_left <= A_right:
                # Odd length case
                if totalLength % 2 != 0:
                    return float(max(A_left, B_left))
                # Even length case
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                    
            # Core Check 2: We took too many elements from nums1!
            elif A_left > B_right:
                right = partitionA - 1 # Shift search space left
                
            # Core Check 3: We took too few elements from nums1!
            else:
                left = partitionA + 1  # Shift search space right