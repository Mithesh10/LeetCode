class Solution(object):
    def isPalindrome(self, s):
        ns = ""
        for i in s:
            if i.isalnum():
                ns += i.lower()
        for i in range(len(ns) // 2):
            if ns[i] != ns[-i - 1]:
                return False
        return True