from unittest import TestCase
from typer.testing import CliRunner

from todo import __app_name__, __version__, cli


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_version__results_in_exit_code_zero(self):
        # arrange
        expected_exit_code = 0
        # act
        result = self.runner.invoke(cli.app, ["--version"])
        # assert
        self.assertEqual(result.exit_code, expected_exit_code)

    def test_version__produces_version_and_app_name(self):
        # arrange
        expected_result_string = f"{__app_name__} v{__version__}\n"
        # act
        result = self.runner.invoke(cli.app, ["--version"])
        # assert
        self.assertIn(expected_result_string, result.stdout)
