from __future__ import annotations

from prompt_toolkit import HTML, PromptSession, prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator


class Prompt:
    def __init__(self) -> None:
        self._session = None

    def __enter__(self) -> Prompt:
        self._session = PromptSession()
        return self

    def __exit__(self, type, value, traceback) -> None:
        del self._session
        self._session = None

    def ask(
        self,
        message: str,
        default: str = "",
        options: list[str] = None,
        validator: Validator = None,
    ) -> str:
        answer = prompt(
            HTML(
                f"<bullet>\\</bullet> <message>{message}</message> "
                + (f"<default>[{default}]</default> " if default else "")
                + "<prompt> > </prompt>"
            ),
            style=Style.from_dict(
                {
                    "bullet": "cyan bold",
                    "default": "gray italic",
                    "message": "white",
                    "prompt": "cyan bold",
                },
            ),
            completer=WordCompleter(options) if options and len(options) > 0 else None,
            validator=validator,
        )

        if not answer:
            answer = default

        return answer
