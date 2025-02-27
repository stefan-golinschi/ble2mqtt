import importlib.metadata
import sys

import bleak


def get_loop_param(loop):
    if sys.version_info >= (3, 8):
        return {}
    return {'loop': loop}


def get_bleak_version():
    # returns None if version info is messed up
    return importlib.metadata.version('bleak')


def get_scanner(hci_adapter: str, detection_callback) -> bleak.BleakScanner:
    bleak_version = get_bleak_version()
    if bleak_version and bleak_version < '0.18':
        scanner = bleak.BleakScanner(adapter=hci_adapter)
        scanner.register_detection_callback(detection_callback)
    else:
        scanner = bleak.BleakScanner(
            adapter=hci_adapter,
            detection_callback=detection_callback,
        )

    return scanner
