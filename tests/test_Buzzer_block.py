from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestBuzzer(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..buzzer_block import Buzzer
        global Buzzer

    def test_process_signals(self):
        with patch(Buzzer.__module__ + '.rh.buzzer') as mock_buzz:
            blk = Buzzer()
            self.configure_block(blk, {'incoming': 'pewpew',
                                       'frequency': 261,
                                       'duration': 1})
            blk.start()
            blk.process_signals([Signal({})])
            blk.stop()
            mock_buzz.note.assert_called_with(261.0, 1.0)
            mock_buzz.note.assert_called_with(261, 1)
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {})
