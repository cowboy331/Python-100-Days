'''
用多线程下载比不用多线程时间节省一个数量级
'''

from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]   # rfind返回从右向左最后一次出现/的位置
        resp = requests.get(self.url)
        with open('../' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    begin=time()
    # 通过requests模块的get函数获取网络资源
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=64cf218ea5a3fb60d288d896adaba4e6')
    # 将服务器返回的JSON格式的数据解析为字典
    # print(resp)
    # print(type(resp))
    data_model = resp.json()
    # print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()
        # filename = url[url.rfind('/') + 1:]   # rfind返回从右向左最后一次出现/的位置
        # resp = requests.get(url)
        # with open('../' + filename, 'wb') as f:
        #     f.write(resp.content)
    end=time()
    print('耗时：%f秒' %(end-begin))

if __name__ == '__main__':
    main()
