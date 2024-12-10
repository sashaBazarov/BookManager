import unittest
from unittest.mock import patch, MagicMock
from command import Command
from process_command.parse_command import parse_command


class TestParseCommand(unittest.TestCase):
    @patch("process_command.parse_command.load_command")
    def test_parse_command_success(self, mock_load_command):
        mock_load_command.return_value = "test_command"

        result = parse_command('command arg1 arg2 key1=value1 key2="value with spaces"')

        self.assertEqual(result.command, "test_command")
        self.assertEqual(result.args, ["arg1", "arg2"])
        self.assertEqual(result.kwargs, {"key1": "value1", "key2": "value with spaces"})

    @patch("process_command.parse_command.load_command", return_value=None)
    def test_parse_command_command_not_found(self, mock_load_command):
        with self.assertRaises(ValueError) as context:
            parse_command("unknown_command arg1")

        self.assertEqual(str(context.exception), "Command 'unknown_command' not found.")
        mock_load_command.assert_called_once_with("unknown_command")

    @patch("process_command.parse_command.load_command")
    def test_parse_command_empty_args_and_kwargs(self, mock_load_command):
        mock_load_command.return_value = "test_command"

        result = parse_command("command")

        self.assertEqual(result.command, "test_command")
        self.assertEqual(result.args, [])
        self.assertEqual(result.kwargs, {})

    @patch("process_command.parse_command.load_command")
    def test_parse_command_mixed_arguments(self, mock_load_command):
        mock_load_command.return_value = "test_command"

        result = parse_command('command "arg with spaces" key="value with spaces"')

        self.assertEqual(result.command, "test_command")
        self.assertEqual(result.args, ["arg with spaces"])
        self.assertEqual(result.kwargs, {"key": "value with spaces"})
