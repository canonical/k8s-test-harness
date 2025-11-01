#
# Copyright 2025 Canonical, Ltd.
# See LICENSE file for licensing details
#


def is_fips_rock(rockcraft_yaml: str) -> bool:
    """Returns True if the given rockcraft yaml indicates a FIPS ROCK."""
    return "fips" in rockcraft_yaml.lower()


def fips_expectations(rockcraft_yaml: str, GOFIPS: int) -> tuple:
    """
    Return (expected_returncode, expected_error) for a given rockcraft yaml and GOFIPS value.
    """
    if is_fips_rock(rockcraft_yaml):
        # fipsed ROCKs should fail if GOFIPS set on a non-fips system
        # since the modified Go toolchain checks for a FIPS-capable crypto backend.
        return (2, "FIPS") if GOFIPS == 1 else (0, "")
    # non-FIPS ROCKs should not care about GOFIPS setting and always succeed
    return 0, ""
