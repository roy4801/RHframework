'''
opencv_test_1

To test the basic functions of opencv intergation
'''
import sys, pygame, os
sys.path.append("../")
from window import *
from input import MouseHandler, KeyHandler
from utils import *

from opencv import Camera

c = Camera(0)

SET_ROOT('..')

display_width = 800
display_height = 600

class App(Window):
    def __init__(self, title, size, win_flag=W_NONE):
        super().__init__(title, size, win_flag)
        self.keyboard = KeyHandler()
        self.add_event_handle(self.keyboard.handle_event)
        self.mouse = MouseHandler()
        self.add_event_handle(self.mouse.handle_event)

        self.frame = None

    def setup(self):
        pass

    def update(self):
        self.frame = c.get_frame_image()

    def render(self):
        self.frame.draw(0, 0)

    def ask_quit(self):
        print('On quit')
        self.quit()

def main():
    app = App('example', (display_width, display_height), W_OPENGL)
    app.run()

if __name__ == '__main__':
    main()