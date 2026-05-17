
from project import validate_password
from project import get_special_chars
from project import password_strength


def test_get_special_chars():
    chars = get_special_chars()
    assert "@" in chars
    assert "!" in chars


def test_password_strength():
    assert password_strength("abc") == 1
    assert password_strength("Abc123!") >= 4


def test_validate_password():
    assert validate_password("Password1") == "Password1"