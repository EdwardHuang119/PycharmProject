# 尝试一下序列的写法
# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# a = 0
# # while x < 3:
# for x in range(3):
#     showname = names[a]
#     showscores = scores[a]
#     print(showname,showscores)
#     a = x + 1
#
# z = 0
# while z < 3:
#     showname = names[z]
#     showscores = scores[z]
#     print(showname, showscores)
#     z = z + 1
#
#
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# if c <= 2:
#    print('学生姓名是%S，成绩是%S' %(showname,showscores))
#    c=c+1
# # else:

# 通过一个dict来录入股票和股票代码的关系并打印出来
# d = {'工商银行': '601398', '中国银行': '601988', '平安银行': '000001'}
# stockname = input('请输入股票的名称：')
# shocknumber = input('请输入股票的代码:')
# d[stockname]=shocknumber
# print(d)
# print(d['工商银行'])
# print(d[stockname])
# 变量在[]中可以不加入引号了。这个比较好。

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dictionary = dict(zip(keys, values))
# print (dictionary)


import win32api
# win32api.MessageBox(0, 'hello', 'title')
win32api.ShellExecute(0, 'open', r'C:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe', '', '', 1)          # 运行程序
