#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

"""Module containing utilities for querying platform parameters
for ROCK testing."""

import platform


ROCKCRAFT_PLATFORM_AMD64 = "amd64"
ROCKCRAFT_PLATFORM_I386 = "i386"
ROCKCRAFT_PLATFORM_ARM64 = "arm64"
ROCKCRAFT_PLATFORM_ARMHF = "armhf"
ROCKCRAFT_PLATFORM_S390X = "s390x"
ROCKCRAFT_PLATFORM_PPC64EL = "ppc64el"
ROCKCRAFT_PLATFORM_RISCV64 = "riscv64"

# NOTE(aznashwan): these constants are automatically derived at runtime with
# no static definition for them, so we must maintain the definitions ourselves:
PYTHON_MACHINE_X86 = "x86"
PYTHON_MACHINE_X86_64 = "x86_64"
PYTHON_MACHINE_ARM64 = "arm64"


_PYTHON_MACHINE_TO_ROCKCRAFT_PLATFORM_ARCHITECTURE_MAP = {
    PYTHON_MACHINE_X86: ROCKCRAFT_PLATFORM_I386,
    PYTHON_MACHINE_X86_64: ROCKCRAFT_PLATFORM_AMD64,
    PYTHON_MACHINE_ARM64: ROCKCRAFT_PLATFORM_ARM64
}


def get_current_rockcraft_platform_architecture() -> str:
    """ Returns a string containing the rockcraft-specific platform
    architecture label of the currently running process.

    https://documentation.ubuntu.com/rockcraft/en/latest/reference/rockcraft.yaml/#platforms

    :raises OSError: if `platform.machine()` does not return anything.
    :raises ValueError: if `platform.machine()` returns unrecognized value.
    """

    machine = platform.machine()
    if not machine:
        raise OSError(
            "Failed to get current platform through `platform.machine()` "
            f"which returned: {machine}")

    if machine not in _PYTHON_MACHINE_TO_ROCKCRAFT_PLATFORM_ARCHITECTURE_MAP:
        raise ValueError(
            f"Unknown platform machine type '{machine}'. Known values are: "
            f"{list(_PYTHON_MACHINE_TO_ROCKCRAFT_PLATFORM_ARCHITECTURE_MAP)}")

    return _PYTHON_MACHINE_TO_ROCKCRAFT_PLATFORM_ARCHITECTURE_MAP[machine]

