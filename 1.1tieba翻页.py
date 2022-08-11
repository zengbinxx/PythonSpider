import requests
import os

# 翻页
# 第一页数据和第二页url有什么不同
#
# https://tieba.baidu.com/f?kw=%E6%9F%AF%E5%8D%97 #第一页 pn=0 50*0
# https://tieba.baidu.com/f?kw=%E6%9F%AF%E5%8D%97&pn=50 #第二页 pn=50 50*1
# https://tieba.baidu.com/f?kw=%E6%9F%AF%E5%8D%97&pn=100 #第三页 pn=100 50*2

tieba = input('请输入你要查询贴吧的名字：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://tieba.baidu.com/f?'
os.mkdir(r'c:/%s'%tieba)
for i in range(3):
    params = {
        'kw': tieba,
        'pn': 50*i
    }
    res = requests.get(url, params=params, headers=headers)
    # 海贼王/海贼王_1.html
    with open(r'C:/%s/%s_%s.html'%(tieba,tieba,i+1),'w',encoding='utf-8') as f:
        f.write(res.content.decode())

# 打开一个文件，不会创建一个文件夹

# 相对路径 当前文件的路径 柯南_1.html
# 绝对路径 从最顶级目录一直写到最后 C:\2021Python学习\202103长青老师爬虫\长清老师爬虫\柯南_1.html

# f1 = open('柯南_1.html')
# f2 = open('C:\2021Python学习\202103长青老师爬虫\长清老师爬虫\柯南_1.html')

# os.mkdir() 创建一个文件夹 注意不能重复创建
# r''取消字符串中的转义

# f'{1}'
# ''.format(1)
# '%s'%1
# 以上3者效果一样


