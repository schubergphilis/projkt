from .constants import VALID_LICENSES
from .helpers import EmailValidator, LicenseValidator

DEFAULT_TEMPLATE_ARGUMENTS = {
    "project_name": {
        "default": "Example Project",
    },
    "project_slug": {
        "default": "example",
    },
    "description": {
        "default": "This is an example project.",
    },
    "license": {
        "default": "Apache-2.0",
        "options": VALID_LICENSES,
        "validator": LicenseValidator(),
    },
    "author": {
        "default": "John Doe",
    },
    "email": {
        "default": "john.doe@example.com",
        "validator": EmailValidator(),
    },
}

DEFAULT_TEMPLATE_IGNORED_ARGUMENTS = [
    "_copy_without_render",
]
