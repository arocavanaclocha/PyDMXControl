"""
 *  PyDMXControl: A Python 3 module to control DMX using uDMX.
 *                Featuring fixture profiles, built-in effects and a web control panel.
 *  <https://github.com/MattIPv4/PyDMXControl/>
 *  Copyright (C) 2018 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
"""

from serial import Serial
import time

from ._transmittingController import transmittingController


class SerialController(transmittingController):

    def __init__(self, port, *args, **kwargs):
        """
        Serial port interface requires port string to establish connection, e.g. 'COM1' for
        windows operating systems.

        Parameters
        ----------
        port: Serial port string.
        """
        self._port = Serial(port=port, baudrate=250000, bytesize=8, stopbits=2)
        super().__init__(*args, **kwargs)

    def close(self):
        # Close serial port
        self._port.close()
        super().close()

    def _send_data(self):
        data = [0] + self.get_frame()
        self._port.send_break(100e-6)
        time.sleep(10e-6)
        self._port.write(bytearray(data))
