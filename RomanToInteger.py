class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # , 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900

        total = 0
        i = 0
        #string = len(s)

        while i < len(s):

            if (i < len(s) - 1) and (s[i] == 'C') and (s[i+1] == 'M'):
                total = total + 900
                i = i + 2
            elif (i < len(s) - 1) and (s[i] == 'C') and (s[i+1] == 'D'):
                total = total + 400
                i = i + 2
            elif (i < len(s) - 1) and (s[i] == 'X') and (s[i+1] == 'L'):
                total = total + 40
                i = i+2
            elif (i < len(s) - 1) and (s[i] == 'X') and (s[i+1] == 'C'):
                total = total + 90
                i = i+2
            elif (i < len(s) - 1) and (s[i] == 'I') and (s[i+1] == 'V'):
                total = total + 4
                i = i+2
            elif (i < len(s) - 1) and (s[i] == 'I') and (s[i+1] == 'X'):
                total = total + 9
                i = i+2
            else:
                total = total + dictionary[s[i]]
                i = i + 1
        
        return total

        
