import pygame
import random

# colors
GREY = (50, 50, 50)
WHITE = (255, 255, 255)


class VisualArray:
    def __init__(self):
        self.size = 100
        self.max_value = 100
        self.array = [random.randint(1, self.max_value) for _ in range(self.size)]

    def draw(self, win):
        for i, v in enumerate(self.array):
            x = i * 10
            height = v * 5
            y = 800 - height
            pygame.draw.rect(win, WHITE, (x, y, 10, height), 0)


def redraw_window(win):
    win.fill(GREY)


def main():

    width = 1000
    height = 800
    win = pygame.display.set_mode((width, height))

    visual_array = VisualArray()

    loop = True
    while loop:
        redraw_window(win)
        visual_array.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        pygame.display.update()


if __name__ == "__main__":
    main()
