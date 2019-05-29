import pygame, cv2

import asset

def cvimage_to_pygame(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	surface = pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
								   "RGB")
	return surface

class Camera:
	def __init__(self, cam_id):
		self.cam_obj = cv2.VideoCapture(cam_id)

	'''
	get_frame_cv() -> retval, image
	'''
	def get_frame_cv(self):
		return self.cam_obj.read()
	'''
	get_frame_surface() -> pygame.Sufrace
	'''
	def get_frame_surface(self):
		_, frame = self.get_frame_cv()
		img = cvimage_to_pygame(frame)
		return img
	'''
	get_frame_image() -> Image
	'''
	def get_frame_image(self):
		return asset.pygame_surface_to_image(self.get_frame_surface())
