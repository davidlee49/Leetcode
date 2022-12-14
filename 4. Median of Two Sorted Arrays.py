#https://leetcode.com/problems/median-of-two-sorted-arrays/


def findMedianSortedArrays(nums1, nums2):
    # find total length of combined arrays
    total_len = len(nums1) + len(nums2)

    # determine if len is even or odd
    is_even = False
    if total_len % 2 == 0:
        is_even = True

    nums1_l, nums1_r = 0, len(nums1) - 1
    nums1_mid = (nums1_l + nums1_r) // 2
    nums2_l, nums2_r = 0, len(nums2) - 1
    nums2_mid = (nums2_l + nums2_r) // 2

    while nums1_mid not in {0, len(nums1) - 1} and nums2_mid not in {0, len(nums2) - 1}:
    # set up conditions to determine mid-point
        mid_a = (nums1_l + nums1_r) // 2
        if len(nums1) > len(nums2):
            mid_a = (nums1_l + nums1_r) // 2
            mid_b = (nums2_l + nums2_r) // 2
        else:
            mid_a = (nums2_l + nums2_r) // 2
            mid_b = (nums1_l + nums1_r) // 2

        if nums1[mid_a] > nums2[mid_b]:
            nums2_r = mid_b - 1
        else:
            nums1_l = mid_a + 1


        if nums1[mid_a] <= nums2[mid_b] and nums2[mid_b] <= nums1[mid_a]:
            if is_even:
                return (nums1[mid_a] + nums2[mid_b]) / 2
            else:
                return max(nums1[mid_a], nums2[mid_b])



    # use binary search in both arrays to find Total len mid-point


    #
    #
