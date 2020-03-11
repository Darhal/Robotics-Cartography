import pygame

class Image:
    def __init__(self, path, width, height):
        pygame.init()
        self.name = path
        self.size = (width, height)
        self.surface = pygame.Surface(self.size)

    def save(self):
        pygame.image.save(self.surface, "test.png")

    def point(self, coord, color = (255, 255, 255)):
        self.surface.set_at(coord, color)



img = Image("test.png", 255, 255)
for i in range(0, 255):
    img.point((i,i))
img.save()