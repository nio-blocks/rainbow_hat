This repo contains blocks for operating the various functions of the pimoroni rainbowhat. The rainbowhat python module requires dependencies that are not pip installable. Directions to install prerequisites for the rainbowhat package can be found [here].(https://github.com/pimoroni/rainbow-hat)


AlphaDisplay
============
The AlphaDisplay block will display a character string onto the display of the RainbowHat.

Properties
----------
- **words**: String, can only display four characters at a time.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

AndroidThingsButton
===================
The AndoridThings Button Block will output signals to specify when an configured Rainbow Hat button has been pressed and released. The button can be specified to check 'A', 'B', or 'C' for press and release events


Properties
----------
- **button_selected**: 

Inputs
------
None

Outputs
-------
- **Pressed**: 
- **Released**: 

Commands
--------
None

***

AndroidThingsRGB
================
The AndroidThingsRGB Block will accept signals to turn the RGB LEDS located above the 'A', 'B', and 'C' buttons on or off. The Red, Green, and Blue properties accept boolean 'True' or 'False' to turn the light on or off.

Properties
----------
- **blue**: 
- **green**: 
- **red**: 

Inputs
------
- **default**: 

Outputs
-------
None

Commands
--------
None

***

Buzzer
======
The Buzzer block will play a sound at a specified frequency and duration.

Properties
----------
- **duration**: The time in seconds for the note to play.
- **frequency**: The frequency in Hz of the note.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

FloatDisplay
============
The FloatDisplay block will display a float onto the display of the RainbowHat.

Properties
----------
- **numbers**: Float, can only display four numbers at a time.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

LedStrip
========
The LedStrip block will control the 7 leds of the RainbowHat.

Properties
----------
- **pixelrgb0**: Red, Green, Blue value to display on pixel 0.
- **pixelrgb1**: Red, Green, Blue value to display on pixel 1.
- **pixelrgb2**: Red, Green, Blue value to display on pixel 2.
- **pixelrgb3**: Red, Green, Blue value to display on pixel 3.
- **pixelrgb4**: Red, Green, Blue value to display on pixel 4.
- **pixelrgb5**: Red, Green, Blue value to display on pixel 5.
- **pixelrgb6**: Red, Green, Blue value to display on pixel 6.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

TemperatureSensor
=================
The TemperatureSensor block will notify a signal containing the temperature and pressure of the RainbowHat.

Properties
----------
- **enrich**: 

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: 

Commands
--------
None

