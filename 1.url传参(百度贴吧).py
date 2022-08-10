# 复习
# 1.requests的基本使用
# 2.发送get请求
# 3.携带请求头
# 4.携带参数
# 5.爬取图片
# 6. w 和 wb 文本数据和二进制数据


# 爬虫流程
# 1.确定url
# 2.使用requests发送get
# 3.解析数据
# 4.把数据保存


import requests
# url_png = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201305%2F30%2F220025pxfkhykvkgkvuktq.jpg&refer=http%3A%2F%2Fattach.bbs.miui.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1614168299&t=fe1c0bdc6550ea01646153dbebcac117'
# res = requests.get(url_png)
#
# with open('图片.png','wb') as f:
#     f.write(res.content)

# 1. 确定url
# tieba = input('请输入你要爬取的贴吧：')  # 你要爬取的贴吧是哪个
# url = 'https://tieba.baidu.com/f?'    # 确定url
# params = {            # 这个参数传递给url中
#     'kw':tieba
# }
# headers = {   # 请求头
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
# }
# res = requests.get(url,params,headers=headers)   # 请求
# print(res.content.decode())   # 打印请求


# 封装称为一个类
# 1.__init__ 初始化
# 2.new_params方法 接收一个参数，给到self.params
# 3.response方法 发送请求
# 4.把数据保存到html中
class TiebaSpider:

    def __init__(self,url):
        self.url = url    # 确定url
        self.headers = {  # 请求头
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
            }
        self.params = None  # 先给他初始化一个值，一般为空值，
        self.tieba = None
    def new_params(self,tieba):
        '''url 传参 这里的self.parmas传递给get当中 运行了之后才会产生 '''
        self.params = {
            'kw':tieba
        }


    def response(self):
        self.res = requests.get(self.url, headers = self.headers,params=self.params)  # get请求中 可以放url headers params
        # print(res.content.decode())

    def save(self):
        with open('%s.html'%self.params['kw'],'w',encoding='utf-8') as f:
            f.write(self.res.content.decode())


if __name__ == '__main__':
    pass
    # url = 'https://tieba.baidu.com/f?'  # 变量
    # tb = TiebaSpider(url)   # 实例化一个类
    # tb.tieba = input('请输入你要查询的贴吧名字：')
    # tb.new_params(tb.tieba)  # 必须先调用new_params才能调用response 因为要先使用self.params
    # tb.response()
    # tb.save()

print(__name__)

# if __name__ == '__main__': 固定写法  主函数的入口 程序调用的时候写在 入口里
# 实例化对象 给他创建了一个tieba这个属性  后面self.tieba 就会使用到 实例化对象当中的tieba  self.tieba = tb.tieba

# 总结
# 掌握：把爬虫封装为类的思想 封装为一个类
# if __name__ == '__main__' 主函数的入口

# 网站 前端（html，js，css） + 后端 （python【django】，java）
# 数据分析
