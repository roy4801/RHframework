import sys, pygame, os
sys.path.append("../RHframework/")

from input import MouseHandler
from font import *
from utils import *

SET_ROOT('..')

display_width = 800
display_height = 600
store = []

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)
		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)
		self.font = Font(GET_PATH(FONT_MAIN, "LucidaBrightDemiBold.ttf"), 100)

	def setup(self):
		pass

	def update(self):
		if self.mouse.btn[MOUSE_L]:
			store.append((self.mouse.x, self.mouse.y))

	def render(self):
		for i in store:
			self.font.draw_str((i[0], i[1]), "hello", (191, 0, 0))

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('font_test', (display_width, display_height), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()