from pathlib import Path

from cement import init_defaults

from .constants import APP_NAME

DEFAULT_CONFIG = init_defaults(
    "general",
    "user",
)
