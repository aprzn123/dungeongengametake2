import pygame

pygame.init()

win = pygame.display.set_mode((800, 450), flags=pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.ACTIVEEVENT:
            print(f'Gain: {event.gain} | State: {event.state}')
    pygame.display.flip()