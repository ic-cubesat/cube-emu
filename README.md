## cube-emu

pyhton emulator for CubeSat on-board systems. (coming soon)

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
     
