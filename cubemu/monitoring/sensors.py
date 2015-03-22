"""This module should contain interfaces to all the cubesat sensors."""

import numpy as np
import time

def read(sensorName):
    """Read the value of a sensor."""
    if sensorName == 'temp1':
        return 15.7
    print 'Sensor unavailable'
    return None


def check(sensorName):
    """Check the status of a sensor."""
    if sensorName == 'temp1':
        return 'Up'

    print 'Sensor unavailable'
    return None

def getPosition():
    x = time.time()%5400*(360./5400)
    y = 180*np.sin(x*np.pi/180) + 180
    return x, y
