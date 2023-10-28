import pygame as pg
import random
import time

class Brick(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # 生成随机颜色
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image = pg.Surface([38, 13])  # 方块大小
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 初始化 Pygame
pg.init()

# 设置窗口
width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("This is animation")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

# 创建砖块矩阵
brick_matrix = []
for row in range(5):
    for col in range(5):
        brick = Brick(col * 40, row * 15)
        brick_matrix.append(brick)

# 创建精灵组并添加砖块
allsprites = pg.sprite.Group(brick_matrix)

clock = pg.time.Clock()  # 创建时钟对象
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 清空屏幕
    screen.blit(bg, (0, 0))

    # 更新精灵组中的精灵
    allsprites.update()

    # 绘制所有精灵
    allsprites.draw(screen)

    # 更新屏幕
    pg.display.update()
    clock.tick(30)  # 每秒运行30帧

pg.quit()
