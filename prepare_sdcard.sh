#!/bin/bash
set -eux

echo "Download and activate toolchain"
export FBT_TOOLCHAIN_PATH=flipperzero-firmware
source flipperzero-firmware/scripts/toolchain/fbtenv.sh
echo "Format SD card"
python3 flipperzero-firmware/scripts/storage.py format_ext
