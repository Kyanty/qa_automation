import pytest


@pytest.mark.usefixtures("set_fixture")
class TestSet:
    def test9_set_diff(self):
        """ Тест 'test9_set_diff' проверяет нахождение различий в sets """
        users = {"Tom", "Bob", "Alice"}
        users2 = {"Sam", "Kate", "Bob"}
        print(TestSet.test9_set_diff.__doc__)
        assert users.difference(users2) == {"Tom", "Alice"}
        assert users2.difference(users) == {"Sam", "Kate"}
        print("test9_set_diff passed")

    def test10_set_in(self):
        """ Тест 'test10_set_in' проверяет создание set """
        months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug"])
        print(TestSet.test10_set_in.__doc__)
        assert "May" in months
        print("test10_set_in passed")
