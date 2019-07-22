import pytest


@pytest.mark.usefixtures("string_fixture")
class TestString:
    def test2_strings_a_3(self):
        """  Тест 'test1_numbers_3_3' проверяет умножение строки"""
        print(TestString.test2_strings_a_3.__doc__)
        assert "a" * 3 == 'aaa'
        print("Test2_strings_'a'*3 passed")

    def test3_strings_len_3(self):
        """  Тест 'test3_strings_len_3' проверяет длину строки"""
        print(TestString.test3_strings_len_3.__doc__)
        assert len('aaa') == 3
        print("Test3__strings_check_len passed")

