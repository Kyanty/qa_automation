"""  Tests apiBREWERY"""
import pytest
import requests

ENDPOINTS = ["", "?sort=name", "?sort=-name",]


@pytest.mark.usefixtures
@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_sort_brewery(api_brewery_url, endpoint):
    """  Tests api sort"""
    url = api_brewery_url.address + endpoint
    # print(url)
    response = requests.get(url)
    # print(response)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"


def test_name_brewery(api_brewery_url):
    """  Tests api by_name"""
    response = api_brewery_url.do_get_by_name()
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"


def test_city_brewery(api_brewery_url):
    """  Tests api by_city"""
    response = api_brewery_url.do_get_by_city()
    # print(response)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"


def test_state_brewery(api_brewery_url):
    """  Tests api by_state"""
    response = api_brewery_url.do_get_by_state()
    # print(response)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"


def test_type_brewery(api_brewery_url):
    """  Tests api by_type"""
    response = api_brewery_url.do_get_by_type()
    # print(response)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"


def test_ids_brewery(api_brewery_url):
    """  Tests api by_ids"""
    response = api_brewery_url.do_get_by_ids()
    # print(response)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json; charset=utf-8"
