from unittest.mock import patch, MagicMock

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestLedStrip(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..led_strip_block import LedStrip
        global LedStrip

    color0 = (1, 1, 1)
    color1 = (2, 2, 2)
    color2 = (3, 3, 3)
    color3 = (4, 4, 4)
    color4 = (5, 5, 5)
    color5 = (6, 6, 6)
    color6 = (7, 7, 7)

    def test_led(self):
        with patch(LedStrip.__module__ + '.rh.rainbow') as mock_led:
            blk = LedStrip()
            self.configure_block(blk, ({'pixelrgb0': self.color0,
                                        'pixelrgb1': self.color1,
                                        'pixelrgb2': self.color2,
                                        'pixelrgb3': self.color3,
                                        'pixelrgb4': self.color4,
                                        'pixelrgb5': self.color5,
                                        'pixelrgb6': self.color6}))
            blk.start()
            blk.process_signals([Signal({})])
            blk.stop()
            mock_led.set_pixel.assert_called_with(6, 7, 7, 7)
            mock_led.show.assert_called_with()
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {})
