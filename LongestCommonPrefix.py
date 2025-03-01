class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Prefix = ''

        if strs == [""]:
            print("Returning empty string because input list is empty")
            return ""

        for i in range(len(strs[0])):
            print("length of first string: ", len(strs[0]))

            for j in range(len(strs)):
                print("length of all strings: ", len(strs[j]))

                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return Prefix

            Prefix += strs[0][i]
            print(Prefix)
        #print("full string: ", str1)
        return Prefix
