import re

from prompt_toolkit.validation import ValidationError, Validator

from .constants import VALID_LICENSES


class LicenseValidator(Validator):
    def validate(self, document):
        license = document.text

        if license in VALID_LICENSES:
            return

        raise ValidationError(message="The provided license is not supported")


class EmailValidator(Validator):
    def validate(self, document):
        email = document.text
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if pattern.match(email):
            return

        raise ValidationError(message="The provided e-mail is not valid")
