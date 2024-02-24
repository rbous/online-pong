import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

clientNumber = 0


class Player:
    def __init__(self, player_num, x, y=50, width=10, height=70, color=(255, 255, 255)):
        self.player_num = player_num
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if self.player_num == 1:

            if keys[pygame.K_w]:
                self.y -= self.velocity

            if keys[pygame.K_s]:
                self.y += self.velocity

        elif self.player_num == 2:

            if keys[pygame.K_UP]:
                self.y -= self.velocity

            if keys[pygame.K_DOWN]:
                self.y += self.velocity

        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(player, win=window):
    win.fill((0, 0, 0))
    player.draw(win)
    pygame.display.update()


def main():
    running = True

    p2 = Player(2, SCREEN_WIDTH - 50)

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        p2.move()
        redraw_window(p2)


main()
