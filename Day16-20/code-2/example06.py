"""
编码和解码 - BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
序列化和反序列化
序列化 - 将对象变成字节序列(bytes)或者字符序列(str) - 串行化/腌咸菜
反序列化 - 把字节序列或者字符序列还原成对象
Python标准库对序列化的支持：
json - 字符形式的序列化
pickle - 字节形式的序列化
dumps / loads
"""

'''
Base64是一种用64个字符来表示任意二进制数据的方法。
用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，
所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
'''
import base64
import json
import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    # cli = redis.StrictRedis(host='120.77.222.217', port=6379,
    #                         password='123123')          # 创建StrictRedis对象，与redis服务器建⽴连接
    cli = redis.StrictRedis(host='120.77.222.217', port=6379)          # 创建StrictRedis对象，与redis服务器建⽴连接
    g=cli.get('guido')
    print(type(g))
    # 获取键name guido的值，变为base64编码。此处cli.get返回的是nonetype类型，
    # 而b64decode()的参数要求是byte类型或ASCII类型，因此会报错
    data = base64.b64decode(cli.get('guido'))
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    #     result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    #     Person('骆昊', 39), Person('王大锤', 18),
    #     Person('白元芳', 25), Person('狄仁杰', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()

