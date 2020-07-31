import pytest
from my_sumpy import my_sum


@pytest.fixture(scope='function')
def get_test_data():
    return [([3, 4, 5, 6], 18), ((1, 2, 3), 6)]


@pytest.fixture(autouse=True)
def setup_and_teardown():
    print('\n fetching data')
    yield
    print('\n finishing and cleaning')


def test_list_sum(get_test_data):
    for data in get_test_data:
        assert my_sum(data[0]) == data[1]
