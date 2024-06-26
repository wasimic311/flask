import pytest
from unittest.mock import patch
import click
from flask import Flask, json
from flask import branch_coverage

# Assuming the function show_server_banner is defined in the same module
# If it's in a different module, adjust the import statement accordingly
from flask.cli import show_server_banner


def save_coverage_to_json(file_path='coverage_result.json'):
    with open(file_path, 'w') as json_file:
        json.dump(branch_coverage, json_file, indent=4)


@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_show_server_banner_not_reloader(mock_echo, mock_reloader):
    mock_reloader.return_value = False

    show_server_banner(debug=True, app_import_path="test_app")
    mock_echo.assert_any_call(" * Serving Flask app 'test_app'")
    mock_echo.assert_any_call(" * Debug mode: on")


@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_show_server_banner_reloader(mock_echo, mock_reloader):
    mock_reloader.return_value = True

    show_server_banner(debug=False, app_import_path="test_app")
    mock_echo.assert_not_called()


@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_show_server_banner_no_import_path(mock_echo, mock_reloader):
    mock_reloader.return_value = False

    show_server_banner(debug=False, app_import_path=None)

    mock_echo.assert_any_call(" * Debug mode: off")
    assert mock_echo.call_count == 1


def test_branch_coverage():
    save_coverage_to_json()
    assert branch_coverage["show_server_banner_1"] == True
    assert branch_coverage["show_server_banner_2"] == True
    assert branch_coverage["show_server_banner_3"] == True
    