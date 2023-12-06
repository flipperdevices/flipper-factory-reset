import serial.tools.list_ports as list_ports

# Returns a valid port or None, if it cannot be found
def resolve_port(portname: str = "auto"):
    if portname != "auto":
        return portname
    # Try guessing
    flippers = list(list_ports.grep("flip_"))
    if len(flippers) == 1:
        flipper = flippers[0]
        print(flipper.serial_number.strip("flip_"))
        return flipper.device
    elif len(flippers) == 0:
        pass
    elif len(flippers) > 1:
        pass


def main():
    return resolve_port()


if __name__ == "__main__":
    main()
