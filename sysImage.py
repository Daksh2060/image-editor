import pygame
import numpy

def getImage(filename):
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).transpose(1, 0, 2).tolist()

def saveImage(pixels, filename):
  nparray = numpy.asarray(pixels).transpose(1, 0, 2)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  pygame.surfarray.blit_array(surf, nparray)
  pygame.image.save(surf, filename)

def showImage(pixels):
  nparray = numpy.asarray(pixels).transpose(1, 0, 2)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  pygame.display.init()
  pygame.display.set_caption("CMPT120 - Image")
  screen = pygame.display.set_mode((width, height))
  screen.fill((225, 225, 225))
  screen.blit(surf, (0, 0))
  pygame.display.update()
    
def getBlackImage(width, height):
  return [[[0, 0, 0] for i in range(width)] for j in range(height)]
