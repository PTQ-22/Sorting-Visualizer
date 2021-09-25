import sys
import pygame
import random

pygame.init()

# colors
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 200)


class Button:

    buttons = []

    def __init__(self, x, y, width, height, color, dark_color, text='', font_color=(0, 0, 0), font_size=20):
        Button.buttons.append(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.normal_color = color
        self.dark_color = dark_color
        self.text = text
        self.font_color = font_color
        self.font_size = font_size
        self.border_size = 5

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.border_size, self.y - self.border_size,
                                          self.width + self.border_size*2, self.height + self.border_size*2), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', self.font_size)
            text = font.render(self.text, True, self.font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                            self.y + (self.height / 2 - text.get_height() / 2)))
        if self.is_mouse(pygame.mouse.get_pos()):
            self.color = self.dark_color
        else:
            self.color = self.normal_color

    def is_mouse(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


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

    def draw_sort(self, win, j, k, end=False):
        redraw_window(win)
        for i, v in enumerate(self.array):
            x = i * 10
            height = v * 5
            y = 800 - height
            if i == j:
                pygame.draw.rect(win, RED, (x, y, 10, height), 0)
            elif i == k:
                pygame.draw.rect(win, DARK_RED, (x, y, 10, height), 0)
            elif end and i <= j:
                pygame.draw.rect(win, GREEN, (x, y, 10, height), 0)
            else:
                pygame.draw.rect(win, WHITE, (x, y, 10, height), 0)
        pygame.display.update()
        # pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def draw_green(self, win):
        for j in range(0, len(self.array)):
            self.draw_sort(win, j, j+1, end=True)
        self.color = GREEN

    def bubble_sort(self, win):
        n = len(self.array)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    pom = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = pom

                self.draw_sort(win, j, j+1)

        self.draw_green(win)

    def selection_sort(self, win):
        n = len(self.array)
        for i in range(0, n-1):
            mini = self.array[i]
            index_mini = i
            for j in range(i+1, n):
                if self.array[j] < mini:
                    mini = self.array[j]
                    index_mini = j
                self.draw_sort(win, j, mini)

            pom = self.array[i]
            self.array[i] = self.array[index_mini]
            self.array[index_mini] = pom

        self.draw_green(win)

    def merge_sort(self, win):
        n = len(self.array)
        self.merge_sort_algo(win, 0, n-1)

        self.draw_green(win)

    def merge(self, win, start, middle, end):
        n_left = middle - start + 1
        n_right = end - middle
        left = [0 for _ in range(n_left)]
        right = [0 for _ in range(n_right)]
        for i in range(0, n_left):
            left[i] = self.array[start + i]
        for i in range(0, n_right):
            right[i] = self.array[middle + 1 + i]

        pointer_left = 0
        pointer_right = 0
        arr_i = start

        while pointer_left < n_left and pointer_right < n_right:
            if left[pointer_left] <= right[pointer_right]:
                self.array[arr_i] = left[pointer_left]
                pointer_left += 1
            else:
                self.array[arr_i] = right[pointer_right]
                pointer_right += 1
            self.draw_sort(win, pointer_left+arr_i, pointer_right+arr_i)
            arr_i += 1

        while pointer_left < n_left:
            self.array[arr_i] = left[pointer_left]
            pointer_left += 1
            arr_i += 1
            self.draw_sort(win, pointer_left+arr_i, pointer_left+arr_i)
        while pointer_right < n_right:
            self.array[arr_i] = right[pointer_right]
            pointer_right += 1
            arr_i += 1
            self.draw_sort(win, pointer_right+arr_i, pointer_right+arr_i)

    def merge_sort_algo(self, win, start, end):
        if start < end:
            middle = (start + end) // 2
            self.merge_sort_algo(win, start, middle)
            self.merge_sort_algo(win, middle+1, end)

            self.merge(win, start, middle, end)


def redraw_window(win):
    win.fill(GREY)
    for b in Button.buttons:
        b.draw(win)


def main():

    width = 1000
    height = 800
    win = pygame.display.set_mode((width, height))

    visual_array = VisualArray()

    restart_button = Button(900, 10, 80, 40, RED, DARK_RED, "RESTART", font_size=15)

    button_y = 100
    button_width = 150
    button_height = 50
    button_bubble_sort = Button(10, button_y, button_width, button_height, BLUE, DARK_BLUE, "BubbleSort")
    button_selection_sort = Button(200, button_y, button_width, button_height, BLUE, DARK_BLUE, "SelectionSort")
    button_merge_sort = Button(390, button_y, button_width, button_height, BLUE, DARK_BLUE, "MergeSort")

    loop = True
    ready_to_start = True
    clock = pygame.time.Clock()
    while loop:
        clock.tick(60)
        redraw_window(win)
        visual_array.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ready_to_start:
                    if button_bubble_sort.is_mouse(pos):
                        ready_to_start = False
                        visual_array.bubble_sort(win)
                    elif button_selection_sort.is_mouse(pos):
                        ready_to_start = False
                        visual_array.selection_sort(win)
                    elif button_merge_sort.is_mouse(pos):
                        ready_to_start = False
                        visual_array.merge_sort(win)
                elif restart_button.is_mouse(pos):
                    visual_array = VisualArray()
                    ready_to_start = True

        pygame.display.update()


if __name__ == "__main__":
    main()
