"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，
不追求最优解，快速找到满意解。
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()   # str.split(str="", num=string.count(str)),str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())   # map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))    # 将函数input_thing的返回值作为可变参数传入Thing的实例
    all_things.sort(key=lambda x: x.value, reverse=True)    # 按照x.value反向排序
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()
