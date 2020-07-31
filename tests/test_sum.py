from src import my_sum


def test_list_sum():
    assert my_sum([1, 2, 3]) == 6, "should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 6"
