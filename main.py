import sys
import pygame
import random

# colors
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
GREEN = (0, 255, 0)


class VisualArray:
    def __init__(self):
        self.size = 100
        self.max_value = 100
        self.values = [i for i in range(1, self.max_value+1)]
        self.array = []
        for i in range(self.size):
            x = random.choice(self.values)
            self.values.remove(x)
            self.array.append(x)
        self.color = WHITE

    def draw(self, win):
        for i, v in enumerate(self.array):
            x = i * 10
            height = v * 5
            y = 800 - height
            pygame.draw.rect(win, self.color, (x, y, 10, height), 0)

    def draw_sort(self, win, j, end=False):
        redraw_window(win)
        for i, v in enumerate(self.array):
            x = i * 10
            height = v * 5
            y = 800 - height
            if i == j:
                pygame.draw.rect(win, RED, (x, y, 10, height), 0)
            elif i == j+1:
                pygame.draw.rect(win, DARK_RED, (x, y, 10, height), 0)
            elif end and i <= j:
                pygame.draw.rect(win, GREEN, (x, y, 10, height), 0)
            else:
                pygame.draw.rect(win, WHITE, (x, y, 10, height), 0)
        pygame.display.update()
        # pygame.time.wait(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def draw_green(self, win):
        for j in range(0, len(self.array)):
            self.draw_sort(win, j, end=True)
        self.color = GREEN

    def bubble_sort(self, win):
        n = len(self.array)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    pom = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = pom

                self.draw_sort(win, j)

        self.draw_green(win)


def redraw_window(win):
    win.fill(GREY)


def main():

    width = 1000
    height = 800
    win = pygame.display.set_mode((width, height))

    visual_array = VisualArray()

    loop = True
    x = True
    clock = pygame.time.Clock()
    while loop:
        clock.tick(60)
        redraw_window(win)
        visual_array.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and x:
                x = False
                visual_array.bubble_sort(win)
        pygame.display.update()


if __name__ == "__main__":
    main()
