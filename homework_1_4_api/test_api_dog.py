"""  Tests apiDoc"""

import json
import pytest
import requests


@pytest.mark.usefixtures
def test_lists(api_dog_url, lst_from_all):
    """Docstring"""
    print(lst_from_all)
    if lst_from_all != "https://dog.ceo/api/breed/":
        url = requests.get(lst_from_all)
    else:
        url = requests.get(lst_from_all + str(api_dog_url.return_random_breed()) + "/list")
    print(url.url)
    data = json.loads(url.content)
    print(data)
    assert data['status'] == 'success'


@pytest.mark.parametrize("test_input", ["1", "99999"])
def test_random_img_by_breed(api_dog_url, img_random_breed, test_input):
    """Docstring"""
    if img_random_breed == "https://dog.ceo/api/breeds/image/random/":
        url = requests.get(img_random_breed)
        print(url.url)
    else:
        url = requests.get(img_random_breed + str(api_dog_url.return_random_breed())
                           + "/images/random/" + test_input)
        print(url.url)
    data = json.loads(url.content)
    assert data['status'] == 'success'
    assert url.status_code == 200


@pytest.mark.parametrize("test_input", ["1", "99999"])
def test_random_img_by_subbreed(api_dog_url, img_random_subbreed, test_input):
    """Docstring"""
    subbreed = str(api_dog_url.return_random_subbreed())
    url = requests.get(img_random_subbreed + subbreed + "/images")
    print(url.url)
    url2 = requests.get(img_random_subbreed + subbreed + "/images/random/" + test_input)
    print(url2.url)
    data = json.loads(url.content)
    print(data)
    assert data['status'] == 'success'
    assert url.status_code == 200
    data2 = json.loads(url2.content)
    print(data2)
    assert data2['status'] == 'success'
    assert url2.status_code == 200
    assert len(data['message']) >= len(data2['message'])
