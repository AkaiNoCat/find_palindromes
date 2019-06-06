# coding=utf-8
# author by akai
# date: 2019-03-09 20:12:57
'''find Palindrome_word in long_string
input:'1234321aba123'
ouput:{'343': 3, 'aba': 3, '23432': 5, '1aba1': 5, '1234321': 7, '21aba12': 7, '321aba123': 9}
'''


def find_Palindrome(string):
    dic={}
    for n in range(2,len(string)+1):# 此处的n是回文的可能长度区间
        for i in range(len(string)-n+1):
            if string[i:i+n] == string[i:i+n][::-1]: 
                dic[string[i:i+n]] = n
    return dic


# a line code for effect
def aline_find_Palindrome(string):
    return { string[i:i+n]:n for n in range(2,len(string)+1) for i in range(len(string)-n+1) if string[i:i+n] == string[i:i+n][::-1]}

# 此处的n是回文的可能长度区间
# 长度n的字符串在string中遍历,应该需要0到len(string)-n次,也就是range(len(string)-n+1)
# 同时 n的长度应该大于2 小于len(string)+1次 所以就是 range(2,len(string)+1)     


# 中心扩展法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        n = len(s)
        self.res = ""
        def check(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i -1 :
                self.res = s[i+1:j]
        for i in range(n):
            j=i
            check(i,j)
            check(i,j+1)
        return self.res

    
if __name__ == "__main__":
    string = input('please input ling_string:')
    print(find_Palindrome(string))
    print(aline_find_Palindrome(string))
