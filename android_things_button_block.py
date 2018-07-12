import rainbowhat as rh
from enum import Enum

from nio.block.base import Block
from nio import GeneratorBlock
from nio.block import output
from nio.properties import VersionProperty, FloatProperty, SelectProperty
from nio.signal.base import Signal

class ButtonSelector(Enum):
    A = 'A' 
    B = 'B' 
    C = 'C'

@output('released', label='Released')
@output('pressed', label='Pressed')
class AndroidThingsButton(GeneratorBlock):

    version = VersionProperty("0.1.0")

    button_selected = SelectProperty(
        ButtonSelector,
        title='Button',
        order=0,
        default=ButtonSelector.A
    )

    def configure(self, context):
        super().configure(context)
        button = self.button_selected().name
        if button == 'A':
            rh.touch.A.press(self.pressed)
            rh.touch.A.release(self.released)
        elif button == 'B':
            rh.touch.B.press(self.pressed)
            rh.touch.B.release(self.released)
        elif button == 'C':
            rh.touch.C.press(self.pressed)
            rh.touch.C.release(self.released)

    def pressed(self, channel):
        self.notify_signals(Signal(), 'pressed')

    def released(self, channel):
        self.notify_signals(Signal(), 'released')
