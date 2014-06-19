# Xively Temperature Logging

## Description

This is an arduino sketch + python script for reading out a temperature sensor and sending the data to Xively.

The arduino acts as a ADC for the raspberry pi, connected to it over USB and relying on the Pi for power.


## Setup

1. Set up the raspberry pi, adding the Xively SDK and Arduino IDE
1. Set up a xively account and a channel for the raspberry Pi
1. Build the circuit. It's only a TMP36 sensor, so this is left as an exercise for the reader.
1. Connect the arduino to the Pi and upload the sketch
1. Launch the python script on the Pi to read the input and put it to the Xively cloud
