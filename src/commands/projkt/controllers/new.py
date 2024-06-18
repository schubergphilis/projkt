import json
from pathlib import Path

from cement import Controller
from cookiecutter.main import cookiecutter
from inflection import titleize

from ....util.terminal.prompt import Prompt
from ....util.terminal.spinner import Spinner
from ..defaults import DEFAULT_TEMPLATE_ARGUMENTS
from ..exceptions import NotFoundAppError, RuntimeAppError


class NewController(Controller):
    class Meta:
        label = "new"
        stacked_on = "base"
        stacked_type = "nested"

        arguments = [
            (
                ["-f", "--force"],
                {
                    "default": False,
                    "action": "store_true",
                    "help": "Overwrite the contents of the output path if it exists.",
                    "dest": "force",
                },
            ),
            (
                ["--path"],
                {
                    "default": ".",
                    "help": "The path where the new project will be generated.",
                    "dest": "path",
                    "type": str,
                },
            ),
            (
                ["template_name"],
                {
                    "help": "The name of the template used to generate the new project.",
                },
            ),
        ]

    def _default(self) -> None:
        context = {}
        force = self.app.pargs.force
        output_path = Path(self.app.pargs.path).expanduser().absolute()
        template_name = self.app.pargs.template_name
        template_path = (
            (Path(__file__).parent.parent.parent.parent / "templates" / template_name)
            .expanduser()
            .absolute()
        )

        cookiecutter_config_path = template_path / "cookiecutter.json"

        if cookiecutter_config_path.exists():
            with open(cookiecutter_config_path.as_posix()) as f:
                context = json.loads(f.read())

        with Prompt() as prompt:
            for argument, _ in context.items():
                message = titleize(argument)

                try:
                    default = DEFAULT_TEMPLATE_ARGUMENTS[argument]["default"]
                except KeyError:
                    default = ""

                try:
                    options = DEFAULT_TEMPLATE_ARGUMENTS[argument]["options"]
                except KeyError:
                    options = None

                try:
                    validator = DEFAULT_TEMPLATE_ARGUMENTS[argument]["validator"]
                except KeyError:
                    validator = None

                answer = prompt.ask(message, default, options, validator)
                context[argument] = answer

        with Spinner("Generating project") as spinner:
            if not template_path.exists():
                spinner.error(f"Could not find '{template_name}' template")
                raise NotFoundAppError("Template not found")

            try:
                _ = cookiecutter(
                    extra_context=context,
                    no_input=True,
                    output_dir=output_path.as_posix(),
                    overwrite_if_exists=force,
                    template=template_path.as_posix(),
                )
            except Exception as e:
                spinner.error("Could not generate project")
                raise RuntimeAppError("Could not generate project") from e

            spinner.success("Project generated!")
