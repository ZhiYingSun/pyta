"""
Test suite for the AccumulationTable class on different
types of accumulator loops
"""

from python_ta.debug import AccumulationTable


def test_one_accumulator() -> None:
    test_list = [10, 20, 30]
    sum_so_far = 0
    with AccumulationTable(["sum_so_far"]) as table:
        for number in test_list:
            sum_so_far = sum_so_far + number

    assert table.loop_variables == {"number": ["N/A", 10, 20, 30]}
    assert table.loop_accumulators == {"sum_so_far": [0, 10, 30, 60]}


def test_two_accumulators() -> None:
    test_list = [10, 20, 30]
    sum_so_far = 0
    list_so_far = []
    with AccumulationTable(["sum_so_far", "list_so_far"]) as table:
        for number in test_list:
            sum_so_far = sum_so_far + number
            list_so_far = list_so_far + [number]

    assert table.loop_variables == {"number": ["N/A", 10, 20, 30]}
    assert table.loop_accumulators == {
        "sum_so_far": [0, 10, 30, 60],
        "list_so_far": [[], [10], [10, 20], [10, 20, 30]],
    }


class MyClass:
    items: list

    def __init__(self, items: list):
        self.items = items

    def get_total(self) -> None:

        sum_so_far = 0
        with AccumulationTable(["sum_so_far"]) as table:
            for item in self.items:
                sum_so_far = sum_so_far + item

        assert table.loop_variables == {"item": ["N/A", 10, 20, 30]}
        assert table.loop_accumulators == {"sum_so_far": [0, 10, 30, 60]}


def test_class_var() -> None:
    my_class = MyClass([10, 20, 30])
    my_class.get_total()


def test_two_loop_vars_one_accumulator() -> None:
    test_list = [10, 20, 30]
    sum_so_far = 0
    with AccumulationTable(["sum_so_far"]) as table:
        for index, item in enumerate(test_list):
            sum_so_far = sum_so_far + item

    assert table.loop_variables == {"index": ["N/A", 0, 1, 2], "item": ["N/A", 10, 20, 30]}
    assert table.loop_accumulators == {"sum_so_far": [0, 10, 30, 60]}


def test_two_loop_vars_two_accumulators() -> None:
    test_dict = {1: "I lo", 2: "ve CS", 3: "C110"}
    keys_so_far = 0
    values_so_far = ""
    with AccumulationTable(["keys_so_far", "values_so_far"]) as table:
        for key, value in test_dict.items():
            keys_so_far = keys_so_far + key
            values_so_far = values_so_far + value

    assert table.loop_variables == {
        "key": ["N/A", 1, 2, 3],
        "value": ["N/A", "I lo", "ve CS", "C110"],
    }
    assert table.loop_accumulators == {
        "keys_so_far": [0, 1, 3, 6],
        "values_so_far": ["", "I lo", "I love CS", "I love CSC110"],
    }
