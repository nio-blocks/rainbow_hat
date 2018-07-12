from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class LedStrip(Block):

    version = VersionProperty("0.1.0")
    pixelrgb0 = Property(title='pixel 0 r g b', default='{{(0, 0, 0)}}')
    pixelrgb1 = Property(title='pixel 1 r g b', default='{{(0, 0, 0)}}')
    pixelrgb2 = Property(title='pixel 2 r g b', default='{{(0, 0, 0)}}')
    pixelrgb3 = Property(title='pixel 3 r g b', default='{{(0, 0, 0)}}')
    pixelrgb4 = Property(title='pixel 4 r g b', default='{{(0, 0, 0)}}')
    pixelrgb5 = Property(title='pixel 5 r g b', default='{{(0, 0, 0)}}')
    pixelrgb6 = Property(title='pixel 6 r g b', default='{{(0, 0, 0)}}')

    def configure(self, context):
        super().configure(context)
        rh.rainbow.clear()
        rh.rainbow.show()

    def process_signals(self, signals):

        for signal in signals:
            for pixel in range(0, 7):
                red = getattr(self, 'pixelrgb{}'.format(pixel))(signal)[0]
                green = getattr(self, 'pixelrgb{}'.format(pixel))(signal)[1]
                blue = getattr(self, 'pixelrgb{}'.format(pixel))(signal)[2]
                rh.rainbow.set_pixel(pixel, red, green, blue)
                rh.rainbow.show()
        self.notify_signals(signals)

    def stop(self):
        rh.rainbow.clear()
        rh.rainbow.show()
        super().stop()
