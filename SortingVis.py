# import libraries
import pygame
import random

# set visualizer loop to false
done = False
# initalize pygame enginer
pygame.init()
# setting window size
screen = pygame.display.set_mode((700, 500))

# setting title to the window
pygame.display.set_caption("Sorting Visualization")

# define variables
barX = 80
barY = 460
width = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()

# create list of random integers
array = []
for i in range(18):
    array.append(random.randrange(5, 50))
    print(array)

# create class to create buttons
class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 18)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))\

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

# function to draw all components of the window
def reDrawWindow(array):
    screen.fill(BLACK)
    bubbleButton.draw(screen, (255,255,255))
    insertionButton.draw(screen, (255, 255, 255))
    selectionButton.draw(screen, (255, 255, 255))
    pygame.font.init()
    myfont = pygame.font.SysFont('timesnewroman', 25)
    pickAlgorithmText = myfont.render('Choose The Algorithm To Sort With', False, (WHITE))
    screen.blit(pickAlgorithmText,(120,20))

# draw the bars of the integers
    for i in range(len(array)):
        pygame.draw.rect(screen, WHITE, (barX + 30 * i, barY, width, array[i] * -5))


# draw buttons
bubbleButton = Button(WHITE, 120, 80, 120, 60, 'Bubble Sort')
insertionButton = Button(WHITE, 300, 80, 120, 62, 'Insertion Sort')
selectionButton = Button(WHITE, 480, 80, 120, 62, 'Selection Sort')


# implement bubble sort
def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                print('Sorting Array..', array)

            reDrawWindow(array)
            pygame.time.delay(100)
            pygame.display.update()

print('Sorted Array:', array)


# implement insertion sort
def insertionSort(array):
    for i in range(1, len(array)):
        pygame.event.pump()
        reDrawWindow(array)
        pygame.time.delay(100)
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            reDrawWindow(array)
            pygame.time.delay(100)
            j = j-1
        array[j + 1] = key
        print('Sorting Array...', array)

        reDrawWindow(array)
        pygame.time.delay(100)
        pygame.display.update()

print('Sorted Array:', array)

# implement selection sort
def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        pygame.time.delay(100)
        reDrawWindow(array)

        array[i], array[min_idx] = array[min_idx], array[i]
        print('Sorting Array...', array)

        reDrawWindow(array)
        pygame.time.delay(100)
        pygame.display.update()

print('Sorted Array:', array)

# start the visualizer loop
while done is False:
    start = False
    pygame.time.delay(10)

# check for button clicks
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bubbleButton.isOver(pos):
                start = True
                bubbleSort(array)
            elif insertionButton.isOver(pos):
                start = True
                insertionSort(array)
            elif selectionButton.isOver(pos):
                start = True
                selectionSort(array)

        if event.type == pygame.MOUSEMOTION:
            if bubbleButton.isOver(pos):
                bubbleButton.color == RED
            elif insertionButton.isOver(pos):
                insertionButton.color == RED
            elif selectionButton.isOver(pos):
                selectionButton.color == RED
            else:
                bubbleButton.color == WHITE
                selectionButton.color == WHITE
                insertionButton.color == WHITE


# if user hasn't started yet create the bars
    if start is False:
        reDrawWindow(array)
        pygame.display.update()

pygame.quit()






