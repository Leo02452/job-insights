import json
from unittest.mock import mock_open, patch
from src.counter import count_ocurrences


def test_counter():
    content = {"message": "The night is dark and full of terrors"}

    with patch("builtins.open", mock_open(read_data=json.dumps(content))):
        assert count_ocurrences("dummy", "T") == 3
    pass
