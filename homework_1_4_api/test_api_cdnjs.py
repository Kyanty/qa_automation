"""  Tests api_cdnjs"""
import random
import requests
import pytest
SEARCH = ["?", "/jquery?", "?search=[query]&"]
FIELDS = ["version", "description", "homepage", "keywords", "license",
          "repository", "autoupdate", "author", "assets"]


@pytest.mark.usefixtures
@pytest.mark.parametrize("fields", ["?fields="])
def test_fields_lib(api_cdnjs_url, fields_fix, fields):
    """  Tests api_cdnjs"""
    library = requests.get(api_cdnjs_url + fields + fields_fix)
    print(library.url)
    assert library.status_code == 200
    assert library.headers['Content-type'] == "application/json; charset=utf-8"
    mlty_fields = requests.get(api_cdnjs_url + fields + fields_fix + "," + random.choice(FIELDS))
    print(mlty_fields.url)
    assert mlty_fields.status_code == 200
    assert mlty_fields.headers['Content-type'] == "application/json; charset=utf-8"


@pytest.mark.parametrize("search", SEARCH)
def test_search_lib(api_cdnjs_url, output_human, search):
    """  Tests api_cdnjs"""
    search = requests.get(api_cdnjs_url + search + output_human)
    print(search.url)
    assert search.status_code == 200
    if output_human == "output=human":
        assert search.headers['Content-type'] == "text/html; charset=utf-8"
    else:
        assert search.headers['Content-type'] == "application/json; charset=utf-8"
