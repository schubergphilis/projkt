from src.commands.projkt.app import ProjktApp


def test_if_we_can_create_app_instance():
    app = ProjktApp()
    assert app is not None
