from cubemu.communication import basic
from cubemu.monitoring import sensors

import unittest


class TestMain(unittest.TestCase):

    def testNothing(self):
        basic.send(basic.DataPacket('blah'))
        sensors.read('temp1')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
