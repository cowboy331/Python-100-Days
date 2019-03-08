"""
什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
目的是为了发现原始数据是否被人篡改过
哈希摘要 - 数字签名/指纹 - 单向哈希函数（没有反函数不可逆），有可能，但非常非常困难
应用领域：
1. 数据库中的用户敏感信息保存成哈希摘要
2. 给数据生成签名验证数据没有被恶意篡改
3. 云存储服务的秒传功能（去重功能）
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。




"""


class StreamHasher():
    """摘要生成器"""

    def __init__(self, algorithm='md5', size=4096):
        """初始化方法
        @params:
            algorithm - 哈希摘要算法
            size - 每次读取数据的大小
        """
        self.size = size
        # getattr(object, name[, default])，返回对象属性的值
        # __import__(module)相当于import module；__import__返回的模块也是module模块
        # lower()将algorithm中所有的大写字母转换为小写字母
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """生成十六进制的摘要字符串"""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        # iter(object, sentinel)，object -- 支持迭代的集合对象。
        # sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
        # 此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
        for data in iter(lambda: file_stream.read(self.size), b''):     # 当返回值为二进制''时抛出异常
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """主函数"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('api-ms-win-crt-process-l1-1-0_jb51.rar', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
