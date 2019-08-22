__version__ = "0.0.1"


def func(a: int, b: int = 0, c: int = 0) -> int:
    """Test function.

    Args:
        a (int): Parameter A.
        b (int, optional): Parameter B.
        c (int, optional): Parameter C.

    Returns:
        sum: The sum of A, B, and C.

    """
    return a + b + c
