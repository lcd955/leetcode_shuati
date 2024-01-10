#13 罗马数字转数字
class Solution(object):
    def romanToInt(self, s):
        dct = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        i,res = 0,0
        while i < len(s)-1:
            if dct[s[i]] < dct[s[i+1]]:
                res -= dct[s[i]]
            else:
                res += dct[s[i]]
            i += 1
        return res+dct[s[-1]]

#14 最长公共前缀
class Solution():
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        res = ""
        for each in zip(*strs):
            if len(set(each)) == 1:
                res += each[0]
            else:
                break
        return res
#2696 删除子串后的最小字符串长度
class Solution:
    def minLength(self, s: str) -> int:
        a='AB'
        b='CD'
        while (a in s or b in s):
                s=s.replace(a,'')
                s=s.replace(b,'')
        return len(s)


