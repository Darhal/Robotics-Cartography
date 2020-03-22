import pygame # import pygame library

"""
@class: Image
@brief: Image class to create simple empty image and facilate image handling
"""
class Image:
    """
        @function: constructor
        @brief: contruct the image class, and intilize pygame
    """
    def __init__(self, path, width, height):
        pygame.init() # init pygame
        self.name = path # save the path
        self.size = (width, height) # save the image size
        self.surface = pygame.Surface(self.size)  # create the surface


    """
        @function: save
        @brief: save the surface as png
    """
    def save(self):
        pygame.image.save(self.surface, self.name) # save the image using the name passed to the constructor


    """
        @function: point
        @brief: add pixel to the surface at the coordinates given, default color is white
    """
    def point(self, coord, color = (255, 255, 255)):
        self.surface.set_at(coord, color) # change pixel at coord with color



# Simple test case for the Image class
"""img = Image("test.png", 255, 255)
for i in range(0, 255):
    img.point((i,i))
img.save()"""