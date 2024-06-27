import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, Request
import json
from flask import branch_coverage

# Save coverage results to JSON
def save_coverage_to_json(file_path='coverage_result.json'):
    with open(file_path, 'w') as json_file:
        json.dump(branch_coverage, json_file, indent=4)

@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_create_url_adapter_with_request(mock_echo, mock_reloader):
    app = Flask(__name__)
    mock_request = MagicMock()
    mock_request.environ = {
        'wsgi.url_scheme': 'http',
        'HTTP_HOST': 'localhost',
        'REQUEST_METHOD': 'GET',
        'PATH_INFO': '/',
        'SCRIPT_NAME': '',
        'QUERY_STRING': ''
    }
    mock_reloader.return_value = False

    app.create_url_adapter(mock_request)
    assert branch_coverage["create_url_adapter_1"] == True
    assert branch_coverage["create_url_adapter_2"] == True or branch_coverage["create_url_adapter_3"] == True

@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_create_url_adapter_with_subdomain_matching(mock_echo, mock_reloader):
    app = Flask(__name__)
    app.subdomain_matching = True
    mock_request = MagicMock()
    mock_request.environ = {
        'wsgi.url_scheme': 'http',
        'HTTP_HOST': 'localhost',
        'REQUEST_METHOD': 'GET',
        'PATH_INFO': '/',
        'SCRIPT_NAME': '',
        'QUERY_STRING': ''
    }
    mock_reloader.return_value = False

    app.create_url_adapter(mock_request)
    assert branch_coverage["create_url_adapter_1"] == True
    assert branch_coverage["create_url_adapter_3"] == True

@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_create_url_adapter_without_request(mock_echo, mock_reloader):
    app = Flask(__name__)
    app.config["SERVER_NAME"] = "localhost"
    app.config["APPLICATION_ROOT"] = "/"
    app.config["PREFERRED_URL_SCHEME"] = "http"
    mock_reloader.return_value = False

    app.create_url_adapter(None)
    assert branch_coverage["create_url_adapter_4"] == True

@patch('flask.cli.is_running_from_reloader')
@patch('click.echo')
def test_create_url_adapter_no_server_name(mock_echo, mock_reloader):
    app = Flask(__name__)
    app.config["SERVER_NAME"] = None
    mock_reloader.return_value = False

    app.create_url_adapter(None)

    assert branch_coverage["create_url_adapter_5"] == True

def test_branch_coverage():
    save_coverage_to_json()
    assert branch_coverage["create_url_adapter_1"] == True
    assert branch_coverage["create_url_adapter_2"] == True
    assert branch_coverage["create_url_adapter_3"] == True
    assert branch_coverage["create_url_adapter_4"] == True
    assert branch_coverage["create_url_adapter_5"] == True
