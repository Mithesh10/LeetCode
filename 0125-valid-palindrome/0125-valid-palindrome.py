class Solution(object):
    def isPalindrome(self, s):
        ns=""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    ns+=i.lower()
                else:
                    ns+=i
        l=len(ns)
        if l<=1:
            return True
        if l==2:
            if ns[0]==ns[1]: return True
        for i in range(l//2):
            if ns[i]!=ns[-i-1]:
                return False
        return True