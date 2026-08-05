class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        string = s.lower()
        for char in string:
            if char.isalnum():
                stack.append(char)
        stack1 = list(stack)
        stack2 = list(stack)
        for i in range(len(stack1)):
            if stack1[i] == stack2.pop():
                continue
            else:
                return False
        return True
