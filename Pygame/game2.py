import pygame
import sys

pygame.init()

size = width, height = 600, 400
# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置标题
pygame.display.set_caption("仿黑客帝国")
bg = (0, 0, 0)

# 设置字体和大小
font = pygame.font.Font(None, 20)
position = 0
line_high = font.get_linesize()

screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_high

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()
