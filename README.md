## cube-emu

pyhton emulator for CubeSat on-board systems. (coming soon)


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

### Components

1. On-board Computer (OBC) - command and data handling
2. Camera
3. Image Processor (IP) - compression, storage
4. ACDS

Below are a few polling based state machines for the OBC and IP.

__OBC State Machine__

```
if state:
  take_photo:
    imageProcessor.state = shootAndStore
    state = orbiting
    if not have_power:
      state = sleep
  orbiting:
    if distress_recorded and have_space and have_power
        state = take_photo
  sleep:
    if have_power:
      state = orbiting
```

__Image Processor SM__

```
if state:
  shootAndStore:
    camera.state = shoot
    sate = waitPhoto
  waitPhoto:
    if photo_ready:
      state = compressing
  compresing:
    compress()
    state = saving:
  saving:
    save()
    state = wait
  wait:
    if photo_request:
      state = shootAndStore
```
