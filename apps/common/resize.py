# -*- coding: utf-8 -*-
from pilkit.lib import Image, ImageDraw


class ResizeToCircle:

    WHITE = 255

    def __init__(self, diameter):
        self.diameter = diameter

    def process(self, img):
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.ImageDraw(mask)
        draw.ellipse((0, 0, self.diameter, self.diameter), fill=self.WHITE)
        img.putalpha(mask)
        return img
