import pytest

@pytest.mark.parametrize("x, y, result", [(1,2,3),(4,5,9),(6,2,7)])

def test_add(x, y, result):
    assert x + y == result


#
# import pytest
# import json
#
# with open("data/data.json") as f:
#     data = json.load(f)
#
# @pytest.mark.parametrize("entry", data)
# def test_login(entry):
#     assert "username" in entry

