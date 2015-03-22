## cube-emu!

pyhton emulator for Cubesat on-board systems.

### Requires

1. Python 2.7
2. [pip](https://pypi.python.org/pypi/pip/)
3. [GNU Make](http://www.gnu.org/software/make/manual/make.html)

```
pip install nose coverage
```

```
apt-get install python-pygame
```

### Instructions

To run the main emulator loop:

```
trixie:  ~/workspaces/cubesat/cube-emu  |master ✗|
→ python cubemu/main.py
[CmdRead]  READ_TEMP temp1
[Process]   =  15.7
[Send]     15.7
[Sleep]    ...
```

To run the tests:

```
trixie:  ~/workspaces/cubesat/cube-emu  |master ✗|
→ make test
rm -rf cover
nosetests --with-coverage --cover-html --cover-package=cubemu
.
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
cubemu                           0      0   100%
cubemu.communication             0      0   100%
cubemu.communication.basic      19      5    74%   10-11, 14, 22, 35
cubemu.monitoring                0      0   100%
cubemu.monitoring.sensors       10      6    40%   8-9, 14-18
----------------------------------------------------------
TOTAL                           29     11    62%
----------------------------------------------------------------------
Ran 1 test in 0.027s

OK
```

You can open the coverage report from `cover/index.html`.
