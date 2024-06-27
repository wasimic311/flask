import pytest
from unittest.mock import MagicMock, patch
import sys
from flask import Flask
from flask.ctx import AppContext

import json
from flask import branch_coverage

def save_coverage_to_json(file_path='coverage_result.json'):
    with open(file_path, 'w') as json_file:
        json.dump(branch_coverage, json_file, indent=4)

def mock_send(signal, *args, **kwargs):
    pass

class MockContextVar:
    def __init__(self, default):
        self.value = default
    
    def get(self, default=None):
        return self.value
    
    def set(self, value):
        self.value = value
    
    def reset(self, token):
        self.value = token.old_value

@patch('flask.signals.appcontext_pushed.send', side_effect=mock_send)
@patch('flask.signals.appcontext_popped.send', side_effect=mock_send)
def test_pop_with_single_token(mock_pushed, mock_popped):
    app = Flask(__name__)
    app.do_teardown_appcontext = MagicMock()
    ctx = AppContext(app)
    ctx._cv_tokens = [MagicMock()]
    
    mock_cv_app = MockContextVar(ctx)
    with patch('flask.ctx._cv_app', mock_cv_app):
        ctx.pop()
    
    assert branch_coverage["pop_1"] == True
    assert branch_coverage["pop_3"] == True
    assert branch_coverage["pop_5"] == True

@patch('flask.signals.appcontext_pushed.send', side_effect=mock_send)
@patch('flask.signals.appcontext_popped.send', side_effect=mock_send)
def test_pop_with_exception(mock_pushed, mock_popped):
    app = Flask(__name__)
    app.do_teardown_appcontext = MagicMock()
    ctx = AppContext(app)
    ctx._cv_tokens = [MagicMock()]
    
    mock_cv_app = MockContextVar(ctx)
    with patch('flask.ctx._cv_app', mock_cv_app), \
         patch('sys.exc_info', return_value=(None, Exception("Test Exception"), None)):
        ctx.pop()
    
    assert branch_coverage["pop_1"] == True
    assert branch_coverage["pop_2"] == True
    assert branch_coverage["pop_3"] == True
    assert branch_coverage["pop_5"] == True

@patch('flask.signals.appcontext_pushed.send', side_effect=mock_send)
@patch('flask.signals.appcontext_popped.send', side_effect=mock_send)
def test_pop_wrong_context(mock_pushed, mock_popped):
    app = Flask(__name__)
    app.do_teardown_appcontext = MagicMock()
    ctx = AppContext(app)
    wrong_ctx = AppContext(app)
    ctx._cv_tokens = [MagicMock()]
    
    mock_cv_app = MockContextVar(wrong_ctx)
    with patch('flask.ctx._cv_app', mock_cv_app):
        with pytest.raises(AssertionError):
            ctx.pop()
    
    assert branch_coverage["pop_1"] == True
    assert branch_coverage["pop_3"] == True
    assert branch_coverage["pop_4"] == True

def test_branch_coverage():
    save_coverage_to_json()
    assert branch_coverage["pop_1"] == True
    assert branch_coverage["pop_2"] == True
    assert branch_coverage["pop_3"] == True
    assert branch_coverage["pop_4"] == True
    assert branch_coverage["pop_5"] == True
