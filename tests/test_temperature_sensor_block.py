from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestTemperatureSensor(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..temperature_sensor_block import TemperatureSensor
        global TemperatureSensor

    def test_temp(self):
        with patch(TemperatureSensor.__module__ + '.rh.weather') as mock_weather:
            blk = TemperatureSensor()
            self.configure_block(blk, {})
            blk.start()
            blk.process_signals([Signal({'incoming': 'pewpew'})])
            blk.stop()
            mock_weather.pressure.assert_called_with()
            mock_weather.temperature.assert_called_with()
            self.assertDictEqual(
                {'temp_C': ANY, 'pressure_Pa': ANY},
                self.last_notified[DEFAULT_TERMINAL][0].to_dict())
