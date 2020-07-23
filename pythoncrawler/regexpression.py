import re

print(re.search(r'baidu', 'www.baidu.com'))
print(re.search(r'.', 'I love you'))
print(re.search(r'lov.', 'I love you'))
print(re.search(r'\d', 'I love 123 you'))
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.118.124.115'))
print(re.search(r'[aeiou]', 'I love you'))
print(re.search(r'[a-z]', 'I love you'))
print(re.search(r'ab{3}c', 'abbbc'))
print(re.search(r'love(A|B)', 'loveB'))
print(re.search(r'(love)\1', 'lovelove'))
# 正则表达式查找ip地址的写法
# print(re.search(r'([01]{0, 1}\d{0, 1}\d | 2{0-4}\d | 25{0-5})\.', '192'))
# print(re.search(r'(([01]{0, 1}\d{0, 1}\d|2{0-4}\d|25{0-5})\.){3}([01]{0, 1}\d{0, 1}\d|2{0-4}\d|25{0-5})',
# '192.128.122.122'))
