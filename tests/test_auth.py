
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.auth import is_valid_token, get_user_role


def test_valid_token():
    assert is_valid_token("valid-token") is True


def test_invalid_token():
    assert is_valid_token("wrong-token") is False


def test_user_role():
    assert get_user_role("valid-token") == "user"
