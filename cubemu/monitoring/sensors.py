"""This module should contain interfaces to all the cubesat sensors."""


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
