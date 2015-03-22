"""This module should contain interfaces to all the cubesat sensors."""

import numpy as np
import matplotlib.pyplot as plt
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

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))

def getPosition():
    x = (time.time()%5400)*(360./5400)
    y = 360*(gaussian(x, 180, 0.001))
    return x, y
