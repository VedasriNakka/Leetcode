class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0

        while x > 0:
            dig = x % 10
            rev = rev *10 + dig
            x = x // 10
        
        if num == rev:
            return True
        return False


        # x = str(x)
        # l = 0
        # r = len(x) - 1

        # while l < r:
        #     if x[l] != x[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

            # if x[l] == x[r]:
            #     l += 1
            #     r -= 1
            #     return True
            # else:
            #     return False
