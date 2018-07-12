from unittest.mock import patch, MagicMock

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestFloatDisplay(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..float_display_block import FloatDisplay
        global FloatDisplay

    def test_floats(self):
        with patch(FloatDisplay.__module__ + '.rh.display') as mock_display:
            blk = FloatDisplay()
            self.configure_block(blk, {'numbers': 800.8})
            blk.start()
            blk.process_signals([Signal({})])
            blk.stop()
            mock_display.print_float.assert_called_with(800.8)
            mock_display.show.assert_called_with()
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {})
