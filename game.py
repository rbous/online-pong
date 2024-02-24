import pygame


class Player:
    def __init__(self, position):
        self.slider = pygame.Rect((position, 50, 10, 70))

    def move(self, direction):
        if direction == "up":
            self.slider.move_ip(0, -1)
        elif direction == "down":
            self.slider.move_ip(0, 1)
        else:
            self.slider.move_ip(0, 0)


def main():

    # initialise screen
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")

    # initialise players
    global p1
    global p2
    p1 = Player(50)
    p2 = Player(SCREEN_WIDTH - 50)

    # event loop
    while True:

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), p1.slider)
        pygame.draw.rect(screen, (255, 255, 255), p2.slider)

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            p1.move("up")
        elif key[pygame.K_s]:
            p1.move("down")
        elif key[pygame.K_UP]:
            p2.move("up")
        elif key[pygame.K_DOWN]:
            p2.move("down")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.display.update()


pygame.quit()

if __name__ == "__main__":
    main()
