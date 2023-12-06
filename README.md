# flipper-factory-reset

## This was tested on ubuntu 22.10 and above and on latest macOS. Current version is for NON-TRANSPARENT VERSION!!

Fully reset flipper and set it to the shipping state:

Here are two ways of resetting your flipper zero to factory state:

# Required items
- SD card (preferably less 8GB, but not crucial)
- USB Type-C cable for flipper
- Flipper must be updated with any OFFICIAL release firmware >= 0.64.3
- Ubuntu 22.10 or latest macOS

# Semi-automatic reset

## Preparation
You will need to have git installed and clone this repository
```shell
git clone --recursive https://github.com/flipperdevices/flipper-factory-reset.git
```

Do following step one time, when setting up your reset bench. It will clone our repo and download the toolchain.
It will download about 1gb of data, so it may take a while.
```shell
./install_requirements.sh
```
This needs to be done single time as well, unless you need new SD card. Prepare an SD card, preferably lower size, insert it into a functional Flipper Zero. 

!! THIS ACTION WILL WIPE ALL DATA ON SD CARD

You can check [flipper docs](https://docs.flipper.net/basics/first-start) on how to insert SD card or power on the device
```shell
./prepare_sdcard.sh
```

## Flipper reset

- Plug USB cable into device and computer.

- Insert SD card into the device

This script will update to a factory firmware, prepare a slideshow, disable debug and do a factory reset
```shell
./automatic_reset.sh
```
- Unplug the device and remove SD card.

- Power off the device by holding back button for 5 seconds and then pressing right.


# Manual reset (Advanced)
You can check [flipper docs](https://docs.flipper.net/basics/first-start) on how to insert SD card or power on the device

- Install [qFlipper](https://update.flipperzero.one/builds/firmware/0.64.4/) app for your operating system. Or alternatively you can use internal update system, by copying files into an update folder on your formatted sd-card. (Manual update folder in this repository)


- Install BLE stack for the firmware. Note that version of firmware, its location and file type may vary on your system
```shell
./qFlipper-x86_64-1.3.2.AppImage cli core2radio ./stm32wb5x_BLE_Stack_full_fw.bin
```
- Install factory firmware
```shell
./qFlipper-x86_64-1.3.2.AppImage cli firmware ./flipper-z-f7-full-0.64.4.dfu
```
- Install python 3.10 or higher
- Install all required python packages
```shell
pip install pyserial colorlog numpy==1.22.3 protobuf==3.20.2 protoletariat Pillow isort opencv-python termcolor
```
- Go to flipper settings->system->factory reset. 
- Go to settings->system and disable debug and set logging level to Default.
- Make sure you do not open any apps, if you do, factory reset flipper again continue from this point. 
- Copy following script and change flipper name to one on the device.
```shell
./slideshow/slideshow_gen.sh flipper
```
```shell
./storage.py send /tmp/flipper_slideshow /int/.slideshow
```

- Make sure SD-card is removed from the device
- Power off the device and place it in the box


# Troubleshooting
- If you get errors when installing firmware, or flipper does not boot, try to use Repair in qFlipper app