from time import sleep
from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class FloatDisplay(Block):

    version = VersionProperty("0.1.0")
    numbers = Property(title="Numbers to Screen", default=None, allow_none=True)

    def configure(self, context):
        super().configure(context)
        rh.display.clear()
        rh.display.show()

    def process_signals(self, signals):

        for signal in signals:
            rh.display.print_float(self.numbers(signal))
            rh.display.show()
        self.notify_signals(signals)

    def stop(self):
        rh.display.clear()
        rh.display.show()
        super().stop()
