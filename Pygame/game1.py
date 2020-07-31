import pygame
import sys

pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)

clock = pygame.time.Clock()
# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置标题
pygame.display.set_caption("初次见面请大家多多关照!")

# 加载图片
cat = pygame.image.load("e1.png")
# 获得图像的位置
position = cat.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 移动图像
    position = position.move(speed)
    # 碰撞检测
    if position.left < 0 or position.right > width:
        cat = pygame.transform.flip(cat, True, False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    # 更新图像
    screen.blit(cat, position)
    # 更新界面
    pygame.display.flip()
    # pygame.time.delay(10)
    clock.tick(200)
