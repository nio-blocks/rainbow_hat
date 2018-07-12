from nio.block.base import Block
from nio import TerminatorBlock
from nio.properties import VersionProperty, Property
from nio.signal.base import Signal

import rainbowhat as rh


class AndroidThingsRGB(TerminatorBlock):

    version = VersionProperty("0.1.0")

    red = Property(title='Red', default=False, order=0)
    green = Property(title='Green', default=False, order=1)
    blue = Property(title='Blue', default=False, order=2)

    def _all_off(self, signal):
        prop_array = \
            [self.red(signal), self.blue(signal), self.green(signal)]
        if True in prop_array:
            return False 
        else:
            return True

    def process_signals(self, signals):
        for signal in signals:
            if self._all_off(signal):
                rh.lights.rgb(0, 0, 0)
            else:
                if self.red(signal):
                    rh.lights.red.on()
                if self.green(signal):
                    rh.lights.green.on()
                if self.blue(signal):
                    rh.lights.blue.on()
