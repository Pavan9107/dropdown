import pytest

def divide_num(a,b):
    return a/b

def test_divide_num():
    with pytest.raises(ZeroDivisionError):
        divide_num(4,0)

def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide_num(4, 0)

    assert "division by zero" in str(excinfo.value)