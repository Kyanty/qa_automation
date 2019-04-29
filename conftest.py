import pytest


@pytest.fixture(scope="session", autouse=True)
def start_tests_fixture(request):
    print('\nTests are starting')

    def fin_tests_fixture():
        print('\nTests finished')

    request.addfinalizer(fin_tests_fixture)


@pytest.fixture(scope="function")
def numbers_fixture(request):
    print('\nTest numbers is starting')

    def numbers_fix_fin():
        print('Test numbers finished')

    request.addfinalizer(numbers_fix_fin)


@pytest.fixture(scope="module")
def string_fixture(request):
    print('\nTests strings are starting')

    def string_fixture_run_at_end():
        print('Tests strings finished')

    request.addfinalizer(string_fixture_run_at_end)


@pytest.fixture(scope="module")
def list_fixture(request):
    print('\nTests list are starting')

    def list_fixture_run_at_end():
        print('Tests list finished')

    request.addfinalizer(list_fixture_run_at_end)


@pytest.fixture(scope="module")
def tuples_fixture(request):
    print('\nTests tuples are starting')

    def tuples_fixture_run_at_end():
        print('Tests tuples finished')

    request.addfinalizer(tuples_fixture_run_at_end)


@pytest.fixture(scope="module")
def dict_fixture(request):
    print('\nTests dict are starting')

    def dict_fixture_run_at_end():
        print('Tests dict finished')

    request.addfinalizer(dict_fixture_run_at_end)


@pytest.fixture(scope="module")
def set_fixture(request):
    print('\nTests set are starting')

    def set_fixture_run_at_end():
        print('Tests set finished')

    request.addfinalizer(set_fixture_run_at_end)