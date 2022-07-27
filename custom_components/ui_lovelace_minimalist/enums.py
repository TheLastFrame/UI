"""Helper constants."""
# pylint: disable=missing-class-docstring
from enum import Enum


class ConfigurationType(str, Enum):
    """What typ of config is used."""

    YAML = "yaml"
    CONFIG_ENTRY = "config_entry"

class UlmDisabledReason(str, Enum):
    RATE_LIMIT = "rate_limit"
    INVALID_TOKEN = "invalid_token"
    LOAD_ULM = "load_ulm"
