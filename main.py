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


