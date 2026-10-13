class Solution:
    def partition(self, s: str) -> List[List[str]]:
      res = []
      cur = []

      def backtrack(i):
        if i >= len(s):
          res.append(cur.copy())
          return

        right = i
        for right in range(i, len(s)):
          if not self.is_palindrome(i, right, s): continue
          cur.append(s[i: right+1])
          backtrack(right+1)
          cur.pop()
          right += 1

      backtrack(0)

      return res

    def is_palindrome(self, l, r, s):
      while l < r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
      return True