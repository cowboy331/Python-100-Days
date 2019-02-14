"""
碰撞检测
"""
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique  # Enum中有重复值会报错
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


# 事件处理
def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化模块
    pygame.init()
    screen = pygame.display.set_mode((1800, 1600))
    pygame.display.set_caption('大球吃吃小球')
    running = True

    while running:
        # 从消息队列获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 鼠标处理事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球（大小、速度、颜色随机）
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球，如果没被吃掉就绘制，被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()

"""
其实上面的代码中还有很多值得改进的地方，
比如刷新窗口以及让球移动起来的代码并不应该放在事件循环中，
等学习了多线程的知识后，用一个后台线程来处理这些事可能是更好的选择。
如果希望获得更好的用户体验，
我们还可以在游戏中加入背景音乐以及在球与球发生碰撞时播放音效，
利用pygame的mixer和music模块，我们可以很容易的做到这一点，
大家可以自行了解这方面的知识。
事实上，想了解更多的关于pygame的知识，
最好的教程是pygame的官方网站，如果英语没毛病就可以赶紧去看看啦。
如果想开发3D游戏，pygame就显得力不从心了，
对3D游戏开发如果有兴趣的读者不妨看看Panda3D。
"""
