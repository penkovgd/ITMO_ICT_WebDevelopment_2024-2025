# Задачи leetcode

## 1. [№1 Two Sum](https://leetcode.com/problems/two-sum/description/)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if num in remainders:
                return [i, remainders[num]]
            remainders[remainder] = i
        return None
```

## 2. [№13 Roman to integer](https://leetcode.com/problems/roman-to-integer/)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90. 

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        roman_to_arabic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        while i < len(s):
            if i + 1 < len(s):
                s1 = s[i]
                s2 = s[i + 1]
                if roman_to_arabic[s1] < roman_to_arabic[s2]:
                    sum += roman_to_arabic[s2] - roman_to_arabic[s1]
                    i += 2
                    continue
            ss = s[i]
            if ss in roman_to_arabic:
                sum += roman_to_arabic[ss]
                i += 1
                continue
        return sum
        
```

## 3. [№14 Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = 200
        for s in strs:
            if len(s) < minlen:
                minlen = len(s)
        result = ""
        for i in range(minlen):
            candidate = strs[0][i]
            valid = True
            for s in strs:
                if s[i] != candidate:
                    valid = False
                    break
            if not valid:
                break
            result += candidate
        return result

```

## 4. [№125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        for i in range(len(s) // 2):
            left = i
            right = len(s) - 1 - i
            if s[left] != s[right]:
                return False
        return True

```

## 5. [№20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { '}': '{', ']': '[', ')': '(' }
        for c in s:
            if c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack

```

## 6. [№21 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        while True:
            if list1 is None and list2 is None:
                break

            if list1 is None:
                if tail is None:
                    head = list2
                else:
                    tail.next = list2
                break

            if list2 is None:
                if tail is None:
                    head = list1
                else:
                    tail.next = list1
                break

            if head is None:
                if list1.val <= list2.val:
                    head = ListNode(list1.val)
                    tail = head
                    list1 = list1.next
                else:
                    head = ListNode(list2.val)
                    tail = head
                    list2 = list2.next
            else:
                if list1.val <= list2.val:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                    list1 = list1.next
                else:
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                    list2 = list2.next

        return head

```

## 7. [№242 Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if not c in d:
                return False
            else: 
                d[c] -= 1
        return all(count == 0 for count in d.values())

```

## 8. [№217 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

## 9. [№121 Best time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

ou are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min = 10e9
        max_profit = 0
        for price in prices:
            if price <= min:
                min = price
            if price - min >= max_profit:
                max_profit = price - min
        return max_profit
```

## 10. [№53 Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0
        for i in range(len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum
        return maxsum

```

## 11. [№392 Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_pointer = 0
        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
        return False
```

## 12. [№88 Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1 
        j = n - 1 
        k = m + n - 1  

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

## 13. [№226 Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)

Given the root of a binary tree, invert the tree, and return its root.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
```

## 14. [№205 Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for c1, c2 in zip(s,t):
            if (c1 in ds and ds[c1] != c2) or (c2 in dt and dt[c2] != c1):
                return False
            ds[c1] = c2
            dt[c2] = c1
        return True
```

## 15. [№83 Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head

```

## 16. [№28 Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

```

## 17. [№724 Find Pivot Index](https://leetcode.com/problems/find-pivot-index/description/)

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l_sum = 0
        for i in range(len(nums)):
            r_sum = total - nums[i] - l_sum
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
```

## 18. [№704 Binary Search](https://leetcode.com/problems/binary-search/description/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
```

## 19. [№344 Reverse String](https://leetcode.com/problems/reverse-string/description/)

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
```

## 20. [№206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the head of a singly linked list, reverse the list, and return the reversed list.


``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev
```