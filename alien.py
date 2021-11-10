import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	
	def __init__(self, ai_game):
		"""Initialize the alien and set its start position"""
		super().__init__()
		self.screen = ai_game.screen
		
		# Load the alien image and get its rect.
		self.image = pygame.image.load('image/alien.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
