"""
上面在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r），
所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，
说得更直接一点就是字符串中没有所谓的转义字符啦。
因为正则表达式中有很多元字符和需要进行转义的地方，
如果不使用原始字符串就需要将反斜杠写作\\，例如表示数字的\d得书写成\\d，
这样不仅写起来不方便，阅读的时候也会很吃力。
"""

import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配qq
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
