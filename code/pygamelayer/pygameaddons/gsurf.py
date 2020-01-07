import pygame
class GSurface(pygame.Surface):
    def get_surface(self):
        return self
    def blit(self, source, dest, area=None, special_flags=0):
        super().blit(source.get_surface, dest, area, special_flags)