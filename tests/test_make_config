import os
import pytest
from flask import Flask, Config
from flask.config import Config as FlaskConfig
from flask import branch_coverage

def test_make_config_default():
    app = Flask(__name__)
    config = app.make_config()
    assert isinstance(config, FlaskConfig)
    assert config["DEBUG"] == get_debug_flag()

def test_make_config_instance_relative():
    app = Flask(__name__)
    config = app.make_config(instance_relative=True)
    assert isinstance(config, FlaskConfig)
    assert config.root_path == app.instance_path
    assert config["DEBUG"] == get_debug_flag()

def get_debug_flag() -> bool:
    """Get whether debug mode should be enabled for the app, indicated by the
    :envvar:`FLASK_DEBUG` environment variable. The default is ``False``.
    """
    val = os.environ.get("FLASK_DEBUG")
    return bool(val and val.lower() not in {"0", "false", "no"})

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def test_branch_coverage():
    assert branch_coverage["make_config_1"] == True
    assert branch_coverage["make_config_2"] == True
