from src import my_sum
import pytest


@pytest.fixture
def get_test_data():
    return [([3, 4, 5, 6], 18), ((1, 2, 3), 6)]


def test_list_sum(get_test_data):
    for data in get_test_data:
        assert my_sum(data[0]) == data[1]

