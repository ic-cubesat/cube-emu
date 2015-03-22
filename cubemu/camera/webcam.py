"""Webcam substitute for the camera subsystems."""
import pygame
import pygame.camera

def takePicture():
  pygame.camera.init()
  cam = pygame.camera.Camera('/dev/video0',(640,480))
  cam.start()
  img = cam.get_image()
  path = 'filename.jpg'
  pygame.image.save(img, path)
  return img, path
