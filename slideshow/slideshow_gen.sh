#!/usr/bin/env bash

export FBT_TOOLCHAIN_PATH=../flipperzero-firmware
source ../flipperzero-firmware/scripts/toolchain/fbtenv.sh

cd $(dirname "$0")

# requirements:
#python3 -m pip install Pillow==9.1.1 heatshrink2==0.11.0

# examples:
#python3 renderer.py --font=haxrcorp_4089_cyrillic_altgr.ttf -i frame_02_tpl.png -o frame_02d_mod.png "Ziwerawd" --xy 77,15; open frame_02d_mod.png 
#python3 renderer.py --font=haxrcorp_4089_cyrillic_altgr.ttf -i frame_02_tpl.png -o frame_02d_mod.png "Iil" --xy 77,15; open frame_02d_mod.png

#python3 ../scripts/slideshow.py -i ./assets/slideshow/first_start -o /tmp/slideshow -d

if [[ ! -z $1 ]]; then
    FLP_NAME="$1"
else
    echo "Usage: $0 <name>"
    exit 1
fi

OUTF="slides"

set -xe

# Clean
echo -n > ./first_start/frame_02.png
if [[ -e "$OUTF" ]]; then
rm "$OUTF"
fi

# Render
python3 renderer.py --font=haxrcorp_4089_cyrillic_altgr.ttf -i frame_02_tpl.png -o ./first_start/frame_02.png "$FLP_NAME" --xy 77,15

# Pack:
python3 ../flipperzero-firmware/scripts/slideshow.py -i ./first_start -o "$OUTF"

if [[ ! -e "$OUTF" ]]; then
exit 222
fi

