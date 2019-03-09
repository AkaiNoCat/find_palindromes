#motto:Fun&Enjoy
author:AKai
date:2019-03-09 20:53:19
project:输出字符串中所有回文字
background:
 	18年参加极客大赛的第四题,当时刚入python,
	花了1个小时才解出来,找到字符串中最长的回文字,
	心心念念了很久终于把它给收服.
'''python
def aline_find_Palindrome(a):
    return { a[i:i+n]:n for n in range(2,len(a)+1) for i in range(len(a)-n+1) if a[i:i+n] == a[i:i+n][::-1]}	
'''

