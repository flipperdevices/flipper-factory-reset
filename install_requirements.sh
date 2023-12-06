#!/usr/bin/env bash
set -eux

echo "Clone Flipper repo and install toolchain. 1gb download total"

echo "Install flipper zero repository as a submodule"
git submodule update --init --recursive

echo "Download and activate toolchain"
export FBT_TOOLCHAIN_PATH=flipperzero-firmware
source flipperzero-firmware/scripts/toolchain/fbtenv.sh