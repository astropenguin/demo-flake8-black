import demo


def test_version():
    """Make sure the version is valid."""
    assert demo.__version__ == "0.0.1"


def test_func():
    """Make sure the return of func is valid."""
    assert demo.func(1) == 1
    assert demo.func(1, 1) == 2
    assert demo.func(1, 1, 1) == 3
