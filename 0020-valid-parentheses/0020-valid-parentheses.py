class Solution(object):
    def isValid(self, s):
        st = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = st.pop() if st else '#'
                if mapping[char] != top_element:
                    return False
            else:
                st.append(char)
        return not st