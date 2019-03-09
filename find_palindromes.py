# coding=utf-8
# author by akai
# date: 2019-03-09 20:12:57
'''find Palindrome_word in long_string
input:'1234321aba123'
ouput:{'343': 3, 'aba': 3, '23432': 5, '1aba1': 5, '1234321': 7, '21aba12': 7, '321aba123': 9}
'''


def find_Palindrome(a):
    dic={}
    for n in range(2,len(a)+1):# 此处的n是回文的可能长度区间
        for i in range(len(a)-n+1):
            if a[i:i+n] == a[i:i+n][::-1]: 
                dic[a[i:i+n]] = n
    return dic


# a line code for effect
def aline_find_Palindrome(a):
    return { a[i:i+n]:n for n in range(2,len(a)+1) for i in range(len(a)-n+1) if a[i:i+n] == a[i:i+n][::-1]}

# 此处的n是回文的可能长度区间
# 长度n的字符串在a中遍历,应该需要0到len(a)-n次,也就是range(len(a)-n+1)
# 同时 n的长度应该大于2 小于len(a)+1次 所以就是 range(2,len(a)+1)     

if __name__ == "__main__":
    string = input('please input ling_string:')
    print(find_Palindrome(string))
    print(aline_find_Palindrome(string))