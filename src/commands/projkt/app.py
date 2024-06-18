import traceback

from cement import App

from .config import DEFAULT_CONFIG
from .constants import APP_NAME
from .controllers.about import AboutController
from .controllers.base import BaseController
from .controllers.new import NewController
from .exceptions import AppError

#
# APP
#


class ProjktApp(App):
    class Meta:
        config_defaults = DEFAULT_CONFIG
        label = APP_NAME
        log_handler = "colorlog"
        output_handler = "tabulate"

        config_files = [
            f"~/.config/{APP_NAME}/{APP_NAME}.conf",
        ]

        extensions = [
            "colorlog",
            "tabulate",
        ]

        handlers = [
            BaseController,
            AboutController,
            NewController,
        ]

        hooks = []


#
# START
#


def run() -> None:
    with ProjktApp() as app:
        try:
            app.run()
        except AppError as e:
            if app.debug:
                print("")
                traceback.print_exception(e)

            exit(1)
        except Exception as e:
            print("")
            traceback.print_exception(e)
            exit(1)
        else:
            app.exit_code = 0


if __name__ == "__main__":
    run()
