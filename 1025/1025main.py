import pygame as pg ,random ,math,time


class Brick (pg.sprite.Sprite):
    def __init__ (self,color,x,y ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38,13])#方塊大小
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

brickA = Brick((153,205,255),1,1)


# 設置窗口
pg.init()
width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("This is animation")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

screen.blit(bg, (0, 0)) #空白畫布 
pg.display.update()


allsprites = pg.sprite.Group()
allsprites.add(brickA)


# 创建精灵组并添加砖块

clock = pg.time.Clock()  # 创建时间元件
running = True

while running:
    clock.tick(30)  # 每秒运行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    allsprites.draw(screen)
    pg.display.update()
    allsprites.update()
            
pg.quit()

