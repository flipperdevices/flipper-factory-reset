#!/usr/bin/env bash
set -eux

echo "Download and activate toolchain"
export FBT_TOOLCHAIN_PATH=flipperzero-firmware
source flipperzero-firmware/scripts/toolchain/fbtenv.sh

echo "Installing factory-firmware"
FLIPPER_NAME=$(python3 get_flipper.py)
if  [ -z "$FLIPPER_NAME" ]
then
    echo "Flipper not found, check that device is connected and functional"
    exit 1
fi
python3 flipperzero-firmware/scripts/selfupdate.py -p auto update/f7-update-0.64.3/update.fuf
sleep 3
python3 scripts/testing/await_flipper.py $FLIPPER_NAME

echo "Disable debug"
python3 ./reset_files_and_settings.py disable_debug
sleep 1

echo "Factory reset"
python3 ./reset_files_and_settings.py factory_reset
sleep 3
python3 scripts/testing/await_flipper.py $FLIPPER_NAME

echo "Generate slideshow"
./slideshow/slideshow_gen.sh $FLIPPER_NAME

echo "Copy slideshow to int. Don't forget to pull SD card out"
python3 flipperzero-firmware/scripts/storage.py send ./slideshow/slides /int/.slideshow
