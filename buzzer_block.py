from nio.block.base import Block
from nio.properties import VersionProperty, FloatProperty

import rainbowhat as rh


class Buzzer(Block):

    version = VersionProperty("0.1.0")
    frequency = FloatProperty(title='Note Freuquency (Hz)', default=261)
    duration = FloatProperty(title='Note Duration (s)', default=1)

    def process_signals(self, signals):

        for signal in signals:
            rh.buzzer.note(self.frequency(signal), self.duration(signal))
        self.notify_signals(signals)
