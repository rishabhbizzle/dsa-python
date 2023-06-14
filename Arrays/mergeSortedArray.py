class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = m - 1
        second = n - 1
        end = (m + n) - 1

        while second >= 0 and first >= 0:
            if nums1[first] > nums2[second]:
                nums1[end] = nums1[first]
                first -= 1
            else:
                nums1[end] = nums2[second]
                second -= 1
            end -= 1

        while second >= 0:
            nums1[end] = nums2[second]
            second -= 1
            end -= 1