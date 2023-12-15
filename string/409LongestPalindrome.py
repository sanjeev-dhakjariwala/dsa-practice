from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0
        has_odd = False

        for count in char_count.values():
            length += count // 2 * 2  # Use even counts
            if count % 2 == 1:
                has_odd = True

        # If there's at least one character with an odd count, add 1 to the length
        return length + 1 if has_odd else length


# Example usage:
solution = Solution()
s1 = "abccccdd"
print(solution.longestPalindrome(s1))  # Output: 7

# s2 = "a"
# print(solution.longestPalindrome(s2))  # Output: 1
