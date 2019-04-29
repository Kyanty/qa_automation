from pytest import mark

@mark.usefixtures("dict_fixture")
class TestDict:
    def test7_dict_update(self):
        """ Тест 'test7_dict_update'
        проверяет объединение двух словарей"""
        users = {"1": "Tom", "3": "Bob", "5": "Alice"}
        users2 = {"2": "Sam", "6": "Kate"}
        users.update(users2)
        key = "2"
        print(TestDict.test7_dict_update.__doc__)
        assert users.get(key) == "Sam"
        print("test7_dict_update passed")

    def test8_dict_pop(self):
        """ Тест 'test8_dict_pop'
        проверяет удаление элементе из словаря"""
        users = {"1": "Tom", "3": "Bob", "5": "Alice"}
        key = "5"
        user = users.pop(key, "Not found")
        print(TestDict.test8_dict_pop.__doc__)
        assert user == "Alice"
        assert users.get(key) == None
        print("test8_dict_pop passed")
