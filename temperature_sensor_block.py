from nio.block.base import Block
from nio.properties import VersionProperty, Property
from nio.signal.base import Signal
from nio.block.mixins.enrich.enrich_signals import EnrichSignals

import rainbowhat as rh


class TemperatureSensor(EnrichSignals, Block):

    version = VersionProperty("0.1.0")

    def process_signals(self, signals):
        output_signals = []
        for signal in signals:
            temp = rh.weather.temperature()
            pressure = rh.weather.pressure()
            output = {'temp_C': temp, 'pressure_Pa': pressure}
            output_signals = self.get_output_signal(output, signal)
        self.notify_signals(output_signals)
