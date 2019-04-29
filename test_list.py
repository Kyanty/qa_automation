import pytest

@pytest.mark.usefixtures("list_fixture")
class TestList:
    def test4_lists_min(self):
        """  Тест 'test4_lists_min' проверяет нахождение max элемента"""
        numbers_list = [2,5,10,7]
        print(TestList.test4_lists_min.__doc__)
        assert max(numbers_list) == 10
        print("test4_max_numbers_list passed")

    def test5_lists(self):
        """  Тест 'test5_lists' проверяет сортировку списка"""
        numbers = list(range(10, 2, -2))
        #  [10, 8, 6, 4]
        print(TestList.test5_lists.__doc__)
        assert min(numbers) == 4
        print("test5_min_numbers_list passed")
