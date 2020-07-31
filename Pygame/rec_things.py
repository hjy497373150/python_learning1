import pygame
import sys

pygame.init()

size = width, height = 600, 400
# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置标题
pygame.display.set_caption("初次见面请大家多多关照!")

f = open("record.txt", "w")

while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')

        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
