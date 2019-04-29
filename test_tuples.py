import pytest


@pytest.mark.usefixtures("tuples_fixture")
class TestTuples:
    def test6_tuples_in(self):
        """  Тест 'test6_tuples_in' проверяет преобразование list в tuple """
        users_list = ["Tom", "Bob", "Kate"]
        users_tuple = tuple(users_list)
        print(TestTuples.test6_tuples_in.__doc__)
        assert "Kate" in users_tuple
        print("test6_tuples_in passed")

