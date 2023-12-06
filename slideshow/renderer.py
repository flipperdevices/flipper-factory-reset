#!/usr/bin/env python3

import argparse

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Main:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", "--input", help="input folder", required=True)
        self.parser.add_argument("-o", "--output", help="output file", required=True)
        self.parser.add_argument(
            "-f",
            "--font",
            help="font filename",
            required=False,
            default="haxrcorp_4089_cyrillic_altgr.ttf",
        )
        self.parser.add_argument(
            "--fontsize",
            help="font size",
            required=False,
            type=int,
            default=16,
        )
        self.parser.add_argument(
            "--xy", help="coordinates", required=False, default="82,15"
        )
        self.parser.add_argument("text", help="text")

        self.args, self.other_args = self.parser.parse_known_args()

    def render(self):
        x, y = tuple(map(int, self.args.xy.split(",")))
        img = Image.open(self.args.input)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.args.font, self.args.fontsize)
        draw.text((x, y), f"{self.args.text},", (0, 0, 0), font=font)
        img.save(self.args.output)
        return 0


if __name__ == "__main__":
    Main().render()
