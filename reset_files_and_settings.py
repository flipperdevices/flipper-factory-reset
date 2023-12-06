#!/usr/bin/env python3

import binascii
import filecmp
import os
import tempfile

from scripts.flipper.app import App
from scripts.flipper.storage import FlipperStorage, FlipperStorageOperations
from scripts.flipper.utils.cdc import resolve_port


def WrapStorageOp(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return 0
        except Exception as e:
            print(f"Error: {e}")
            # raise  # uncomment to debug
            return 1

    return wrapper


class Main(App):
    def init(self):
        self.parser.add_argument("-p", "--port", help="CDC Port", default="auto")

        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_disable_debug = self.subparsers.add_parser(
            "disable_debug", help="Disable debug mode for 0.64 firmware"
        )
        self.parser_disable_debug.set_defaults(func=self.disable_debug)

        self.parser_factory_reset = self.subparsers.add_parser(
            "factory_reset", help="Factory reset with auto-confirm"
        )
        self.parser_factory_reset.set_defaults(func=self.factory_reset)

    def _get_port(self):
        if not (port := resolve_port(self.logger, self.args.port)):
            raise Exception("Failed to resolve port")
        return port

    @WrapStorageOp
    def disable_debug(self):
        self.logger.debug("Disabling debug on device, log level will not reset")
        with FlipperStorage(self._get_port()) as storage:
            storage.debug_off()

    @WrapStorageOp
    def factory_reset(self):
        self.logger.debug("Factory reset")
        with FlipperStorage(self._get_port()) as storage:
            storage.factory_reset()


if __name__ == "__main__":
    Main()()
