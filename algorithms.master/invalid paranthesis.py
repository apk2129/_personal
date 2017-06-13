class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.removeHelper(s, 0, 0, '(', ')', ans)
        return ans

    def removeHelper(self, s, last_i, last_j, char1, char2, ans):
        """ Remove invalid parentheses in two rounds:
            1st round: detect ')' appears more times then '('
            2nd round: detect '(' appears more times then ')'
        """
        sum = 0
        for i in range(last_i, len(s)):
            if s[i] == char1:
                sum += 1
            if s[i] == char2:
                sum -= 1
            if sum >= 0:
                continue
            # anytime when sum < 0, we can start deleting a char2 between [last_j, i]
            for j in range(last_j, i+1):
                # deleted char2 should be first seen or not repeating (to avoid duplication)
                if s[j] == char2 and (j == last_j or s[j] != s[j-1]):
                    self.removeHelper(s[:j] + s[j+1:], i, j, char1, char2, ans)
            # invalid string has had valid result added to ans in recursion. so stop here.
            return

        s = s[::-1]
        if char1 == '(':
            self.removeHelper(s, 0, 0, ')', '(', ans)
        else:
            ans.append(s)

print(Solution().removeInvalidParentheses("(a)())()"))
